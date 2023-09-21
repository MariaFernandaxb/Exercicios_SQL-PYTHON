
# Exercício 3: Exclusão com Junção
# Imagine um banco de dados para um blog com tabelas Posts e Comentários. A tabela Posts possui os campos: id, titulo, conteúdo. A tabela Comentários possui os campos: id, post_id, texto.

# Você quer excluir todos os posts que não têm nenhum comentário. Escreva uma consulta SQL que realize essa exclusão

import sqlite3

conexao = sqlite3.connect('banco2.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
Create table Posts(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT(50),
    Conteudo TEXT(200)     
 )
''')

cursor.execute('''
Create table Comentários (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Post_id INTEGER, 
    Texto TEXT(200),
    FOREIGN KEY (Post_id) REFERENCES Posts(id)             
)
''')