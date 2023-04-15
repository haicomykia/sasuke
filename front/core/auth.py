from fastapi import status
import streamlit as st
import requests
import json

from core.settings import Settings
from exceptions.error_message import Error_Message

settings = Settings()

def show_login_form():
    """"
    ログイン機能を提供
    """
    st.markdown('# ログイン')
    with st.form(key='login'):
        user_id: str = st.text_input('ユーザーID', max_chars=20)
        password: str = st.text_input('パスワード', type='password')
        data = {
            'username': user_id,
            'password': password
        }
        submit_button = st.form_submit_button(label='ログイン')

        if not submit_button:
            return

        url = settings.LOGIN_URL
        res = requests.post(
            url,
            data=data
        )

        match res.status_code:
            case status.HTTP_200_OK:
                # セッションに保存
                st.session_state['authentication_status'] = True
                st.session_state['access_token'] = res.json()['access_token']
            case status.HTTP_400_BAD_REQUEST:
                # ユーザーIDかパスワードが違う
                st.session_state.clear()
                st.warning(Error_Message.INCORRECT_PASSWORD_OR_EMAIL.text)
            case status.HTTP_422_UNPROCESSABLE_ENTITY:
                # 未入力などのバリデーションエラー
                detail = res.json()['detail']
                for error in detail:
                    item = error['loc'][1]
                    match item:
                        case 'username':
                            st.warning(Error_Message.REQIURED_ITEM_IS_EMTPY.text.format('ユーザーID'))
                        case 'password':
                            st.warning(Error_Message.REQIURED_ITEM_IS_EMTPY.text.format('パスワード'))
                        case _:
                            st.warning(Error_Message.INTERNAL_SERVER_ERROR.text)
            case _:
                st.error(Error_Message.INTERNAL_SERVER_ERROR.text)


def has_authorized_user() -> bool:
    """
    Returns
    -------
    bool
        ユーザが認証されているか？
    """
    if 'access_token' not in st.session_state:
        return False

    access_token = st.session_state['access_token']

    if access_token is None:
        return False

    url = settings.GET_CURRENT_USER
    res = requests.get(url, headers={'Authorization' : f'Bearer {access_token}'})

    match res.status_code:
        case status.HTTP_200_OK:
            return True
        case _:
            return False


def login_required(func_authorized):
    """
    ユーザー認証が必須なメソッドに付与するデコレータ
    認証されていない場合はログインフォームを出力

    Parameters
    ----------
    func_authorized
        ユーザーが認証されてている場合の処理
    """
    def prepare_login_form():
        if has_authorized_user():
            func_authorized()
        else:
            show_login_form()

    return prepare_login_form