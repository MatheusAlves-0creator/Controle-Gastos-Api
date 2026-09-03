import sqlite3


def conectar():
    conexao = sqlite3.connect("gastos.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def inserir_despesa(descricao, valor, categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO despesas (descricao, valor, categoria)
        VALUES (?, ?, ?)
    """, (descricao, valor, categoria))

    conexao.commit()

    id_despesa = cursor.lastrowid

    conexao.close()

    return id_despesa


def listar_despesas_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM despesas")

    despesas = cursor.fetchall()

    conexao.close()

    return [dict(despesa) for despesa in despesas]


def buscar_despesa_banco(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM despesas WHERE id = ?",
        (id,)
    )

    despesa = cursor.fetchone()

    conexao.close()

    if despesa:
        return dict(despesa)

    return None


def deletar_despesa_banco(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM despesas WHERE id = ?",
        (id,)
    )

    conexao.commit()

    quantidade_excluida = cursor.rowcount

    conexao.close()

    return quantidade_excluida


def atualizar_despesa_banco(id, descricao, valor, categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE despesas
        SET descricao = ?, valor = ?, categoria = ?
        WHERE id = ?
    """, (descricao, valor, categoria, id))

    conexao.commit()

    quantidade_atualizada = cursor.rowcount

    conexao.close()

    return quantidade_atualizada