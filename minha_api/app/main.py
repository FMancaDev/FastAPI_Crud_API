from fastapi import FastAPI

app = FastAPI(title="Learning_API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "API online"}


@app.get("/items")
def get_items():
    return [
        {"id": 1, "nome": "Filipe"},
        {"id": 2, "nome": "Marine"},
        {"id": 3, "nome": "Mariana"},
    ]
