from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    設定クラス
    メンバ変数名は.envファイルのキーと同じ名前にすると値がセットされる
    """
    AUTH_URL: str
    REGISTER_URL: str
    LOGIN_URL: str


    class Config:
        env_file = '.env'