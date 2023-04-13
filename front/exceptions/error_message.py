from typing import Optional
from fastapi import status

class Base_Error_Message:
    """
    エラーメッセージの基底クラス
    """
    text: str

    def __str__(self) -> str:
        return self.__class__.__name__


class Error_Message:
    """
    エラーメッセージクラス
    """
    class INTERNAL_SERVER_ERROR(Base_Error_Message):
        text = "システムエラーが発生しました。管理者までお問い合わせください。"

    class LOGIN_FAILURED(Base_Error_Message):
        text = "ログインに失敗しました。"

    class REQIURED_ITEM_IS_EMTPY(Base_Error_Message):
        text = "{}を入力してください。"

    class INCORRECT_PASSWORD_OR_EMAIL(Base_Error_Message):
        text = "ユーザーIDまたはパスワードが違います。"

    class ALREADY_REGISTERED_EMAL(Base_Error_Message):
        text = "登録済みのメールアドレスです。"

    class HAS_NO_PERMISSION(Base_Error_Message):
        text = "権限がありません。"