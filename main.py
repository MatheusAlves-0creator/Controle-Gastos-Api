from fastapi import FastAPI, HTTPException
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


@app.get("/despesas/{id}")
def buscar_despesa(id: int):

    for despesa in despesas:
        if despesa["id"] == id:
            return despesa

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )
@app.delete("/despesas/{id}")
def deletar_despesa(id: int):

    for despesa in despesas:
        if despesa["id"] == id:
            despesas.remove(despesa)

            return {"mensagem": "Despesa excluída com sucesso"}

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )
@app.put("/despesas/{id}")
def atualizar_despesa(id: int, despesa_atualizada: Despesa):

    for despesa in despesas:

        if despesa["id"] == id:

            despesa["descricao"] = despesa_atualizada.descricao
            despesa["valor"] = despesa_atualizada.valor
            despesa["categoria"] = despesa_atualizada.categoria

            return despesa

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )