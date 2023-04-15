import streamlit as st

from core.settings import Settings
from core.auth import login_required

settings = Settings()

@login_required
def main():
    st.markdown('# マスタメンテ画面')

if __name__ == '__main__':
    main()