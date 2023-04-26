from enum import Enum


class SousaTypesEnum(Enum):
    """
    操作ログの列挙体
    """
    REFERENCE = (1, '参照')
    ENTRY = (2, '新規作成')
    UPDATE = (3, '更新')
    DELETE = (4, '削除')
    EXPORT = (5, 'エクスポート')
    IMPORT = (6, 'インポート')

    def __init__(self, sousa_id: int, sousa_name: str):
        """
        Parameters
        ----------
        sousa_id: int
            操作ID
        sousa_name: str
            操作名
        """
        self.sousa_id = sousa_id
        self.sousa_name = sousa_name
