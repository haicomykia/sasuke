import streamlit as st


def set_page_config():
    st.set_page_config(layout="wide")


def main_page():
    st.markdown('# Main Page')
    # ファイルアップロード
    st.file_uploader("ファイルをアップロード", type='csv')


def login_page():
    st.markdown('# Login Page')


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
