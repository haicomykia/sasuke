from fastapi import status
import streamlit as st
import requests
import json

from core.settings import Settings
from core.auth import login_required
from exceptions.error_message import Error_Message

settings = Settings()

@login_required
def main():
    st.markdown('# ユーザー登録')

    with st.form(key='register'):
        email: str = st.text_input('ユーザーID', type='default', max_chars=128)
        password: str = st.text_input('パスワード', type='password')

        data = {
            'email': email,
            'password': password
        }
        submit_button = st.form_submit_button(label='ユーザー登録')

        if submit_button:
            front_url = settings.FRONT_URL
            url = f'{front_url}/auth/register'
            res = requests.post(
                url,
                data=json.dumps(data)
            )

            match res.status_code:
                case status.HTTP_201_CREATED:
                    st.info('ユーザーを作成しました。')
                case status.HTTP_400_BAD_REQUEST:
                    detail = res.json()['detail']

                    if 'reason' in detail:
                        st.error(detail['reason'])
                        return

                    match detail:
                        case 'REGISTER_USER_ALREADY_EXISTS':
                            st.error(Error_Message.ALREADY_REGISTERED_EMAL.text)
                        case _:
                            st.error(Error_Message.INTERNAL_SERVER_ERROR.text)
                case _:
                    st.error(Error_Message.INTERNAL_SERVER_ERROR.text)

if __name__ == '__main__':
    main()