# Controle de Gastos API

API REST desenvolvida em Python para gerenciamento de despesas.

## Funcionalidades

- Cadastrar despesas
- Listar despesas
- Buscar despesa por ID
- Atualizar despesas
- Excluir despesas
- Validação de dados
- Persistência com banco de dados SQLite

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Métodos da API

| Método | Rota | Função |
|---|---|---|
| GET | / | Verificar se a API está funcionando |
| POST | /despesas | Cadastrar uma despesa |
| GET | /despesas | Listar todas as despesas |
| GET | /despesas/{id} | Buscar despesa por ID |
| PUT | /despesas/{id} | Atualizar uma despesa |
| DELETE | /despesas/{id} | Excluir uma despesa |

## Exemplo de despesa

```json
{
  "descricao": "Uber",
  "valor": 35.50,
  "categoria": "Transporte"
}
```

## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/MatheusAlves-0creator/Controle-Gastos-Api.git
```

Entre na pasta:

```bash
cd Controle-Gastos-Api
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Git Bash:

```bash
source venv/Scripts/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
python -m uvicorn main:app --reload
```

Acesse a documentação:

```text
http://127.0.0.1:8000/docs
```

## Banco de dados

O projeto utiliza SQLite.

O arquivo `gastos.db` é criado automaticamente quando a aplicação é executada.

## Autor

Projeto desenvolvido para estudo de Python, APIs REST e banco de dados.