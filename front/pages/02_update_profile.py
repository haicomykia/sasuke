from typing import Union, Final, Any
from dataclasses import dataclass, asdict
from fastapi import status
import streamlit as st
import requests
import json

from core.auth import login_required, has_authorized_user, show_login_form
from core.settings import Settings
from exceptions.error_message import Error_Message

settings = Settings()


@login_required
def main():
    st.markdown('# ユーザー設定')

    with st.form(key='update_user_profile'):
        with st.container():
            new_your_password: str = st.text_input('新しいパスワード', type='password')
            st.caption('※ 半角の英大文字・小文字, 記号, 数字を使って8文字以上')

            access_token: Final[str] = st.session_state['access_token']
            headers: Final[dict[str, str]] = {
                'Authorization': f'Bearer {access_token}'}
            location: Final[str] = settings.FRONT_URL
            url: Final[str] = f'{location}/user/me'

            res = requests.get(url, headers=headers)
            st.text_input('ユーザー名',
                          placeholder=json.loads(res.text)['user_name'],
                          disabled=True)

            new_your_user_name = st.text_input('新しいユーザー名')

        old_your_password = st.text_input('現在のパスワード', type='password')

        submit_button = st.form_submit_button(label='変更')

        if submit_button:
            if not has_authorized_user():
                show_login_form()
                return

            # コマンドオブジェクトを生成
            command = UserSettingCommand(new_your_password, new_your_user_name)
            content = asdict(command, dict_factory=command_factory)

            if not any(content):
                st.info(Error_Message.REQIURED_ITEM_IS_EMTPY.text.format(
                    '変更する項目'))
                return

            # 現在のパスワードで認証
            if not len(old_your_password):
                st.error(Error_Message.REQIURED_ITEM_IS_EMTPY.text.format(
                    '現在のパスワード'))
                return

            auth_url = f'{location}/auth/authenticate'
            data = {
                'plain_password': old_your_password
            }
            res = requests.post(auth_url, data=data, headers=headers)

            res_json = res.json()

            match res.status_code:
                case status.HTTP_401_UNAUTHORIZED:
                    st.error(res_json['detail']['error_message'])
                    return
                case status.HTTP_422_UNPROCESSABLE_ENTITY:
                    st.error(Error_Message.INTERNAL_SERVER_ERROR.text)
                    return
                case _:
                    pass

            # 認証できれば変更
            res = requests.patch(url,
                                 data=json.dumps(content),
                                 headers=headers)

            match res.status_code:
                case status.HTTP_200_OK:
                    st.info('ユーザー設定の変更処理が完了しました。')
                case status.HTTP_400_BAD_REQUEST:
                    st.error(res_json['detail']['reason'])
                case _:
                    st.error(Error_Message.INTERNAL_SERVER_ERROR.text)


@dataclass(frozen=True)
class UserSettingCommand:
    """
    ユーザー設定の入力項目
    Attributes
    ----------
        password: str
            パスワード
        user_name :str
            ユーザー名
    """
    password: str
    user_name: str


def command_factory(form: list[tuple[str, Any]]) -> dict[str, Any]:
    """
    ユーザー設定の入力項目からFastAPIへのリクエスト用辞書を生成

    Parameters
    ----------
    form: list[tuple[str, Any]]
        リスト

    Returns
    --------
    dict: dict[str, Any]
        Noneと空文字を除去した辞書
    Notes
    ------
    dataclasses.asdict() の引数, dict_factoryでの使用を想定
    """
    dict = {}
    for k, v in form:
        if v is None:
            continue
        if isinstance(v, str) and len(v) == 0:
            continue
        dict[k] = v
    return dict


if __name__ == '__main__':
    main()
