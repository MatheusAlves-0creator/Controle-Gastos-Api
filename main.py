from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Despesa(BaseModel):
    descricao: str
    valor: float
    categoria: str


despesas = []


@app.get("/")
def inicio():
    return {"mensagem": "Controle de Gastos API funcionando!"}


@app.post("/despesas")
def cadastrar_despesa(despesa: Despesa):
    despesas.append(despesa)
    return despesa


@app.get("/despesas")
def listar_despesas():
    return despesas