from typing import Optional
import pandas as pd
import json
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
"""
@app.get('/info-by-id/{show_id}')
def buscar_id(show_id:str):
    df_git = pd.read_json('https://raw.githubusercontent.com/GonzaloPosse/netflix_test/main/netflix_titles.json')
    df_git.set_index('show_id', drop=True, inplace=True)
    data = df_git.to_dict('index')
    # data = json.dumps(data, indent=4, separators=(',',':'))
    return {
        'Index':show_id, 
        'data': data[show_id]
    }
"""
