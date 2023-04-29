import traceback
from fastapi import HTTPException, status
from exceptions.error_message import Error_Message

class APIException(HTTPException):
    """
    カスタム例外
    """
    default_status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, message: str,
                 status_code: int = default_status_code) -> None:
        self.message = message
        self.status_code = status_code

        self.detail = {'error_code': self.status_code, 'error_message': self.message}

        super().__init__(self.status_code, self.detail)


class SystemException(Exception):
    """
    システムエラー
    Note
    ----
    例. SystemExecption(e)
    """
    def __init__(self, e: Exception) -> None:
        self.exc = e
        self.stack_trace = traceback.format_exc()
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = {
            'error_code': self.status_code,
            'error_message': Error_Message.INTERNAL_SERVER_ERROR.text
        }
