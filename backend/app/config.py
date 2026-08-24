import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "NOVA Agent"
    version: str = "1.0.0"
    debug: bool = True
    
    # We will expand this with more config 
    
    class Config:
        env_file = ".env"

settings = Settings()
