# Exercício 2: Atualização com Subconsulta
# Suponha que você tenha uma tabela chamada Estudantes com os campos: id, nome, idade, nota_final. Você deseja atualizar a coluna nota_final para 10 para todos os estudantes que têm uma idade maior que a média das idades de todos os estudantes.

# Escreva uma consulta SQL para calcular a média das idades e, em seguida, atualizar os registros apropriados na tabela Estudantes.

import sqlite3

conexao = sqlite3.connect('banco1.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE Estudantes(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    Nome TEXT(50),
    Idade INTEGER,
    Nota_Final FLOAT         
)'''
)