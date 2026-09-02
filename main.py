from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Despesa(BaseModel):
    descricao: str
    valor: float
    categoria: str


despesas = []

proximo_id = 1


@app.get("/")
def inicio():
    return {"mensagem": "Controle de Gastos API funcionando!"}


@app.post("/despesas")
def cadastrar_despesa(despesa: Despesa):

    global proximo_id

    nova_despesa = {
        "id": proximo_id,
        "descricao": despesa.descricao,
        "valor": despesa.valor,
        "categoria": despesa.categoria
    }

    despesas.append(nova_despesa)

    proximo_id += 1

    return nova_despesa


@app.get("/despesas")
def listar_despesas():
    return despesas