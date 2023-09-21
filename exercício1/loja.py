# Exercício 1: Consulta Complexa
# Considere um banco de dados de uma loja que possui as tabelas Produtos e Vendas. A tabela Produtos tem os campos: id, nome, preco. A tabela Vendas possui os campos: id, produto_id, quantidade, data.

# Escreva uma consulta SQL para encontrar o nome e o total de vendas (quantidade * preço) de cada produto vendido em 2023, ordenado pelo total de vendas em ordem decrescente.



import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Produtos(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT(50),
    Preço FLOAT(10)
)'''
)

cursor.execute('''
CREATE TABLE Vendas (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Produto_id  INTEGER NOT NULL,
    Quantidade INTEGER NOT NULL,
    Data TEXT(10) ,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
)'''
)

conexao.commit()
conexao.close()

