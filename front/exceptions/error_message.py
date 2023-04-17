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

    class REQUIRED_LOGIN(Base_Error_Message):
        text = "認証情報の期限が切れています。ログインしてください。"

    class PASSWORD_NEEDS_AT_LEAST_STR_LEN(Base_Error_Message):
        text = "パスワードは{}文字以上必要です。"

    class INVALID_CHAR_TYPE_IN_PASSWORD(Base_Error_Message):
        text = "パスワードには半角英数字と記号をいれてください。"