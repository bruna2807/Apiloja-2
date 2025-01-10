from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Banco de dados simulado com dados fictícios
produtos_db = [
    {"id": 1, "nome": "Blusa de Seda", "descricao": "Blusa feminina de seda elegante.", "preco": 120.50, "categoria": "Roupas Casuais"},
    {"id": 2, "nome": "Vestido Longo", "descricao": "Vestido longo ideal para festas.", "preco": 250.00, "categoria": "Roupas de Festa"},
    {"id": 3, "nome": "Saia Jeans", "descricao": "Saia jeans casual para o dia a dia.", "preco": 89.90, "categoria": "Roupas Casuais"},
]

categorias_db = [
    {"id": 1, "nome": "Roupas Casuais"},
    {"id": 2, "nome": "Roupas de Festa"},
    {"id": 3, "nome": "Acessórios"},
]

clientes_db = [
    {"id": 1, "nome": "Maria Silva", "email": "maria.silva@example.com", "telefone": "(11) 91234-5678"},
    {"id": 2, "nome": "Ana Costa", "email": "ana.costa@example.com", "telefone": "(21) 99876-5432"},
    {"id": 3, "nome": "Juliana Souza", "email": "juliana.souza@example.com", "telefone": "(31) 98765-4321"},
]

# Rotas para Produtos
@app.get("/produtos/")
def listar_produtos():
    return produtos_db

@app.get("/produtos/{id}")
def obter_produto(id: int):
    for produto in produtos_db:
        if produto["id"] == id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

@app.post("/produtos/")
def criar_produto(id: int, nome: str, descricao: str, preco: float, categoria: str):
    if any(p["id"] == id for p in produtos_db):
        raise HTTPException(status_code=400, detail="Produto com este ID já existe.")
    produtos_db.append({"id": id, "nome": nome, "descricao": descricao, "preco": preco, "categoria": categoria})
    return {"msg": "Produto criado com sucesso!"}

@app.put("/produtos/{id}")
def atualizar_produto(id: int, nome: str = None, descricao: str = None, preco: float = None, categoria: str = None):
    for produto in produtos_db:
        if produto["id"] == id:
            if nome: produto["nome"] = nome
            if descricao: produto["descricao"] = descricao
            if preco: produto["preco"] = preco
            if categoria: produto["categoria"] = categoria
            return {"msg": "Produto atualizado com sucesso!"}
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

@app.delete("/produtos/{id}")
def excluir_produto(id: int):
    for produto in produtos_db:
        if produto["id"] == id:
            produtos_db.remove(produto)
            return {"msg": "Produto excluído com sucesso!"}
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

# Rotas para Categorias
@app.get("/categorias/")
def listar_categorias():
    return categorias_db

@app.get("/categorias/{id}")
def obter_categoria(id: int):
    for categoria in categorias_db:
        if categoria["id"] == id:
            return categoria
    raise HTTPException(status_code=404, detail="Categoria não encontrada.")

@app.post("/categorias/")
def criar_categoria(id: int, nome: str):
    if any(c["id"] == id for c in categorias_db):
        raise HTTPException(status_code=400, detail="Categoria com este ID já existe.")
    categorias_db.append({"id": id, "nome": nome})
    return {"msg": "Categoria criada com sucesso!"}

@app.put("/categorias/{id}")
def atualizar_categoria(id: int, nome: str = None):
    for categoria in categorias_db:
        if categoria["id"] == id:
            if nome: categoria["nome"] = nome
            return {"msg": "Categoria atualizada com sucesso!"}
    raise HTTPException(status_code=404, detail="Categoria não encontrada.")

@app.delete("/categorias/{id}")
def excluir_categoria(id: int):
    for categoria in categorias_db:
        if categoria["id"] == id:
            categorias_db.remove(categoria)
            return {"msg": "Categoria excluída com sucesso!"}
    raise HTTPException(status_code=404, detail="Categoria não encontrada.")

# Rotas para Clientes
@app.get("/clientes/")
def listar_clientes():
    return clientes_db

@app.get("/clientes/{id}")
def obter_cliente(id: int):
    for cliente in clientes_db:
        if cliente["id"] == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

@app.post("/clientes/")
def criar_cliente(id: int, nome: str, email: str, telefone: str):
    if any(c["id"] == id for c in clientes_db):
        raise HTTPException(status_code=400, detail="Cliente com este ID já existe.")
    clientes_db.append({"id": id, "nome": nome, "email": email, "telefone": telefone})
    return {"msg": "Cliente criado com sucesso!"}

@app.put("/clientes/{id}")
def atualizar_cliente(id: int, nome: str = None, email: str = None, telefone: str = None):
    for cliente in clientes_db:
        if cliente["id"] == id:
            if nome: cliente["nome"] = nome
            if email: cliente["email"] = email
            if telefone: cliente["telefone"] = telefone
            return {"msg": "Cliente atualizado com sucesso!"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

@app.delete("/clientes/{id}")
def excluir_cliente(id: int):
    for cliente in clientes_db:
        if cliente["id"] == id:
            clientes_db.remove(cliente)
            return {"msg": "Cliente excluído com sucesso!"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")
