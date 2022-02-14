from pydantic import BaseModel
from datetime import datetime

class Notebook(BaseModel):
    name: str
    description: str
    anotations = []

class Anotations(BaseModel):
    titulo: str
    data_criacao = datetime.today().strftime("%d/%m/%Y")
    data_mod = datetime.now().strftime("%d/%m/%Y %H:%M")
    tags: str