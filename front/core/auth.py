from functools import wraps

from fastapi import status
import streamlit as st
import requests

from core.settings import Settings
from exceptions.error_message import Error_Message

settings = Settings()


def show_login_form() -> None:
    """
    ログイン機能を提供

    Returns
    -------
    None
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

        front_url = settings.FRONT_URL
        url = f'{front_url}/auth/jwt/login'
        res = requests.post(
            url,
            data=data
        )

        match res.status_code:
            case status.HTTP_200_OK:
                # セッションに保存
                st.session_state['user_id'] = user_id
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
                            st.warning(
                                Error_Message.REQIURED_ITEM_IS_EMTPY.text.format(
                                    'ユーザーID'))
                        case 'password':
                            st.warning(
                                Error_Message.REQIURED_ITEM_IS_EMTPY.text.format(
                                    'パスワード'))
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

    front_url = settings.FRONT_URL
    url = f'{front_url}/user/me'
    res = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})

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

    @wraps(func_authorized)
    def prepare_login_form(*args, **kwargs):
        if has_authorized_user():
            func_authorized(*args, **kwargs)
        else:
            show_login_form()

    return prepare_login_form


def validate_password(password: str) -> bool:
    """
    パスワードのバリデーションチェック

    Parameters
    -----
    password
        パスワード

    Returns
    -----
    bool
        パスワードがルールを満たしているか？
    """
    if len(password) < 8:
        return False

    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    symbols = """ ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/ """
    digits = "0123456789"

    cnt_cap, cnt_small, cnt_symbol, cnt_digit = 0, 0, 0, 0

    for i in password:
        if i in capitalalphabets:
            cnt_cap = cnt_cap + 1
        if i in smallalphabets:
            cnt_small = cnt_small + 1
        if i in symbols:
            cnt_symbol = cnt_symbol + 1
        if i in digits:
            cnt_digit = cnt_digit + 1

    if cnt_cap > 0 and cnt_small > 0 and cnt_digit > 0 and cnt_symbol > 0 \
            and cnt_cap + cnt_small + cnt_digit + cnt_symbol == len(password):
        return True

    return False
