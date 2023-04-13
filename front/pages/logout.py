from fastapi import status
import streamlit as st
import requests

from core.settings import Settings

settings = Settings()

def main():
    if 'access_token' in st.session_state:
        url = '{location}/auth/jwt/logout'.format(location=settings.AUTH_URL)
        res = requests.post(url)

        # セッションから削除
        for key in st.session_state.keys():
            del st.session_state[key]

        st.info('ログアウトしました。')
    else:
        st.info('ログインしてください。')


if __name__ == '__main__':
    main()