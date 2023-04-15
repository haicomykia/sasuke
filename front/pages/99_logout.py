from fastapi import status
import streamlit as st
import requests

from core.settings import Settings

settings = Settings()

def main():
    if 'access_token' not in st.session_state or (access_token := st.session_state['access_token']) is None:
        st.info('ログインしてください。')
        return

    url = '{location}/auth/jwt/logout'.format(location=settings.FRONT_URL)
    headers = {'Authorization': f'Bearer {access_token}'}

    res = requests.post(url, headers=headers)

    # セッションから削除
    for key in st.session_state.keys():
        del st.session_state[key]

    st.info('ログアウトしました。')


if __name__ == '__main__':
    main()