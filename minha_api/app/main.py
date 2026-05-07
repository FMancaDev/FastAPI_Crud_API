from fastapi import FastAPI
from fastapi import HTTPException

# instancia da app com nome e versao
app = FastAPI(title="Learning_API", version="1.0.0")

# raiz apenas comfirmar que a API esta viva
@app.get("/")
def root():
    return {"message": "API online"}

# base de dados por agora
items = [
    {"id": 1, "nome": "tesoura"},
    {"id": 2, "nome": "garrafa"},
    {"id": 3, "nome": "mesa"}
]

# endpoint da lista - responde a GET e devolve a lista toda
@app.get("/items")
def get_items():
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
