from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    criar_tabela,
    inserir_despesa,
    listar_despesas_banco,
    buscar_despesa_banco,
    deletar_despesa_banco,
    atualizar_despesa_banco
)


app = FastAPI()

criar_tabela()


class Despesa(BaseModel):
    descricao: str
    valor: float
    categoria: str


@app.get("/")
def inicio():
    return {
        "mensagem": "Controle de Gastos API funcionando!"
    }


@app.post("/despesas")
def cadastrar_despesa(despesa: Despesa):

    id_despesa = inserir_despesa(
        despesa.descricao,
        despesa.valor,
        despesa.categoria
    )

    return {
        "id": id_despesa,
        "descricao": despesa.descricao,
        "valor": despesa.valor,
        "categoria": despesa.categoria
    }


@app.get("/despesas")
def listar_despesas():
    return listar_despesas_banco()


@app.get("/despesas/{id}")
def buscar_despesa(id: int):

    despesa = buscar_despesa_banco(id)

    if despesa:
        return despesa

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )


@app.delete("/despesas/{id}")
def deletar_despesa(id: int):

    quantidade_excluida = deletar_despesa_banco(id)

    if quantidade_excluida > 0:
        return {
            "mensagem": "Despesa excluída com sucesso"
        }

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )


@app.put("/despesas/{id}")
def atualizar_despesa(id: int, despesa_atualizada: Despesa):

    quantidade_atualizada = atualizar_despesa_banco(
        id,
        despesa_atualizada.descricao,
        despesa_atualizada.valor,
        despesa_atualizada.categoria
    )

    if quantidade_atualizada > 0:

        return {
            "id": id,
            "descricao": despesa_atualizada.descricao,
            "valor": despesa_atualizada.valor,
            "categoria": despesa_atualizada.categoria
        }

    raise HTTPException(
        status_code=404,
        detail="Despesa não encontrada"
    )