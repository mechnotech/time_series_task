from pydantic import BaseModel


class Settings(BaseModel):
    random_state: int = 42
    app_port: int = 8050


config = Settings()
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
