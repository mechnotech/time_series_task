from pydantic import BaseModel


class Settings(BaseModel):
    random_state: int = 42
    app_port: int = 8050


config = Settings()
