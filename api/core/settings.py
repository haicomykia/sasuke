from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    設定クラス
    メンバ変数名は.envファイルのキーと同じ名前にすると値がセットされる
    """
    DB_URL: str
    SECRET_KEY: str
    TITLE: str
    ENV: str
    EXPIRED_SECONDS: int

    class Config:
        env_file = '.env'