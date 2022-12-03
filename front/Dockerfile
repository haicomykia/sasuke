FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit"]

CMD ["run", "src/front/main.py"]

EXPOSE 8501