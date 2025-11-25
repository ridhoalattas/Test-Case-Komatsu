from pydantic import BaseModel


class Gemini(BaseModel):
    api_token: str  = ""
    model: str = ""
    temperature: float | int = ""


class Config(BaseModel):
    gemini: Gemini = Gemini()
