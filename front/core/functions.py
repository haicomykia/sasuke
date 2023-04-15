from fastapi import status
import streamlit as st
import requests
import json

from core.settings import Settings
from exceptions.error_message import Error_Message

settings = Settings()