import os
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class ModelBase:
    """
    Modelの基底クラス
    """
