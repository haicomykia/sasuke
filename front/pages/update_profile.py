from fastapi import status
import streamlit as st
import requests
import json

from core.settings import Settings
from core.auth import login_required, has_authorized_user, show_login_form
from exceptions.error_message import Error_Message

settings = Settings()

@login_required
def main():
    st.markdown('# ユーザー設定')

    with st.form(key='update_user_profile'):
        st.markdown('### パスワード変更')
        old_your_password: str = st.text_input('現在のパスワード', type='password')
        new_your_password: str = st.text_input('新しいパスワード', type='password')

        submit_button = st.form_submit_button(label='変更')

        if submit_button:
            if not has_authorized_user():
                show_login_form()
                return

            location = settings.FRONT_URL
            access_token = st.session_state['access_token']
            headers = {'Authorization': f'Bearer {access_token}'}

            # 現在のパスワードで認証
            auth_url = f'{location}/auth/authenticate'
            data = {
                'plain_password': old_your_password
            }
            res = requests.post(auth_url, data=data, headers=headers)

            if res.status_code == status.HTTP_400_BAD_REQUEST:
                st.error('現在のパスワードが違います。')
                return

            # 認証できれば変更
            url = f'{location}/user/me'
            res = requests.patch(url,
                                data=json.dumps({'password': new_your_password}),
                                headers=headers)

            match res.status_code:
                case status.HTTP_200_OK:
                    st.info('パスワードを変更しました。')
                case status.HTTP_400_BAD_REQUEST:
                    detail = res.json()['detail']
                    st.error(detail['reason'])
                case _:
                    st.error(Error_Message.INTERNAL_SERVER_ERROR.text)


if __name__ == '__main__':
    main()