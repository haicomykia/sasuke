from fastapi import status
import streamlit as st
import requests

from core.settings import Settings

settings = Settings()

def show_login_form():
    """"
    ログインフォームとログイン機構を返す
    """
    with st.form(key='login'):
        user_id: str = st.text_input('ユーザーID', max_chars=20)
        password: str = st.text_input('パスワード', type='password')
        data = {
            'username': user_id,
            'password': password
        }
        submit_button = st.form_submit_button(label='ログイン')

        if submit_button:
            url = '{location}/auth/jwt/login'.format(location=settings.AUTH_URL)
            res = requests.post(
                url,
                data=data
            )

            if res.status_code == status.HTTP_200_OK:
                # セッションに保存
                st.session_state['authentication_status'] = True
                st.session_state['access_token'] = res.json()['access_token']

            else:
                st.error('ユーザーID / パスワードが違います。')


def login_required(func):
    """
    ログインフォームを表示するデコレータを定義
    """
    def prepare_login_form():
        if 'access_token' in st.session_state:
            func()
        else:
            show_login_form()
    return prepare_login_form