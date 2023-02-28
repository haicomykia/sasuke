import os
from dotenv import load_dotenv
import streamlit as st
import requests
import json

def set_page_config():
    st.set_page_config(layout="wide")


def main_page():
    st.markdown('# Main Page')
    # ファイルアップロード
    st.file_uploader("ファイルをアップロード", type='csv')


def login_page():
    st.markdown('# Login Page')
    load_dotenv()
    with st.form(key='login'):
        content: str = st.text_input('ユーザーID', max_chars=20)
        password: str = st.text_input('パスワード', type='password')
        data = {
            'user_name': content,
            'password': password
        }
        submit_button = st.form_submit_button(label='ログイン')

        if submit_button:
            url = '{location}/user/auth'.format(location=os.getenv('AUTH_URL'))
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            st.write(res.json())


def main():
    page_names_to_funcs = {
        'Login Page': login_page,
        'Main Page': main_page
    }
    selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs)
    page_names_to_funcs[selected_page]()


if __name__ == '__main__':
    set_page_config()
    main()
