from doctest import debug
from re import DEBUG
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    #data settings
    data_path: str = "data/drugs.csv"
    
    #API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True
    API_PREFIX: str = "/api"
    
    #Ollama API
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = ""
    
    class Config:
        env_file  = ".env"