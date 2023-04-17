from fastapi import status
import requests
import streamlit as st

from core.settings import Settings
from core.auth import login_required
from exceptions.error_message import Error_Message

settings = Settings()

@login_required
def main():
    st.markdown('# 資金繰り表作成')

    with st.form(key='generate_shikinguri'):
        file = st.file_uploader("金融機関の入出金ファイルをアップロードしてください", type='csv')
        submit_button = st.form_submit_button(label='作成')
        if submit_button:
            if file is None:
                st.info('ファイルを添付してください。')
            else:
                location = settings.FRONT_URL
                post_url = f'{location}/predicate/uploadfile'

                # see:https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
                payload = {'file': (file.name, file.getvalue())}

                access_token = st.session_state['access_token']
                headers = {'Authorization': f'Bearer {access_token}'}

                res = requests.post(post_url, files=payload, headers=headers)

                match res.status_code:
                    case status.HTTP_200_OK:
                        st.info('ファイルをアップロードしました。')
                    case status.HTTP_401_UNAUTHORIZED:
                        st.error(Error_Message.REQUIRED_LOGIN.text)
                    case _:
                        st.error(Error_Message.INTERNAL_SERVER_ERROR.text)

if __name__ == '__main__':
    main()