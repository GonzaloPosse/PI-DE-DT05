from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/validar/{numero}')
def validar_capicua(numero:str):
    respuesta = 'No es capicua'

    if numero == numero[::-1]:
        respuesta = 'Si es capicua'

    return {
        'numero':numero,
        'validacion':respuesta
    }
