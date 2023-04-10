from fastapi import status
import streamlit as st
import requests

from core.settings import Settings
from core.functions import  login_required

settings = Settings()

@login_required
def main():
    url = '{location}/auth/jwt/logout'.format(location=settings.AUTH_URL)
    res = requests.post(url)
    if res.status_code == status.HTTP_200_OK:
        # セッションから削除
        for key in st.session_state.keys():
            del st.session_state[key]
    else:
        st.error('ログアウトにて異常が発生しました。')


if __name__ == '__main__':
    main()