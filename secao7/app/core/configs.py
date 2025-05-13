from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    
    JWT_SECRET: str = 'LOB-VggKMl1pDElBfgQsbFq1w72x1aCswhbaayFthEQ'
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
