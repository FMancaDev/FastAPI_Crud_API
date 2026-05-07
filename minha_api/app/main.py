from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi import HTTPException

# instancia da app com nome e versao
app = FastAPI(title="Learning_API", version="1.0.0")


# raiz apenas comfirmar que a API esta viva
@app.get("/")
def root():
    return {"message": "API online"}


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=17)


# base de dados por agora
items = [
    {"id": 1, "name": "Tesoura"},
    {"id": 2, "name": "Garrafa"},
    {"id": 3, "name": "Mesa de Jantar"},
    {"id": 4, "name": "PC Gamer"},
    {"id": 5, "name": "Teclado"}
]


# endpoint da lista - responde a GET e devolve a lista toda
@app.get("/items")
def read_items():
    return items


# endpoint de item individual - devolve item caso esse esteja em item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="item nao encontrado"
    )
