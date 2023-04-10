import streamlit as st

from core.settings import Settings
from core.functions import  login_required

settings = Settings()

@login_required
def main():
    st.markdown('# トップページ')

if __name__ == '__main__':
    main()