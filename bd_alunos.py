# Exercício 1: Criar uma tabela
# Crie uma tabela chamada "alunos" com os campos: ID (inteiro), Nome (texto) e Idade (inteiro).

# Exercício 2: Inserir dados
# Insira três registros na tabela "alunos" com informações fictícias.

# Exercício 3: Consulta simples
# Escreva uma consulta SQL para selecionar todos os registros da tabela "alunos" e exibi-los.

# Exercício 4: Consulta com filtro
# Escreva uma consulta SQL para selecionar todos os alunos com idade superior a 20 anos.

# Exercício 5: Atualização de dados
# Atualize a idade de um aluno específico na tabela.

# Exercício 6: Exclusão de dados
# Exclua um aluno da tabela com base no ID.

import sqlite3 

conexao = sqlite3.connect('bd.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE ALUNOS (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT (100),
        Idade INTEGER
    )'''
)

conexao.commit()
conexao.close()
