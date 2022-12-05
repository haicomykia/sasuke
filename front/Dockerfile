FROM python:3.10

WORKDIR /src/front

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.create false
# RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --with front; fi

ENTRYPOINT [ "streamlit"]

CMD ["run", "main.py"]

EXPOSE 8501