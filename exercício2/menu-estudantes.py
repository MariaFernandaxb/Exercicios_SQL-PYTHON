import sqlite3

conexao = sqlite3.connect('banco1.sqlite3')
cursor = conexao.cursor()

def insert_estudantes():
    cursor = conexao.cursor()
    print('Bem vindo a Ultima.School')
    nome = input("Digite o nome do aluno: ")
    idade = int(input(f"Digite a idade do {nome}: "))
    nota = float(input(f"Digite a nota do {nome}: "))
    valor = [nome, idade, nota]
    inserir = 'insert into Estudantes (nome, idade, Nota_Final) values (? , ? , ?)'
    print('Dados inseridos com sucesso')

    cursor.execute(inserir, valor)
    conexao.commit()
   
    menu()

def update_nota():
    cursor = conexao.cursor()
     
    consulta = cursor.execute('select id, Nome, Idade from Estudantes')
    for consultar in consulta: 
        print(f'ID : {consultar[0]} | NOME: {consultar[1]} | IDADE: {consultar[2]}')

    print('Selecione o ID para atualizar a nota: ')
    aluno_id = int(input("Digite o ID: "))
    nota_atual = float(input("Atualize a nota: "))
    valor = [nota_atual, aluno_id]
    atualizar = 'UPDATE Estudantes set Nota_Final = ? where ID = ?'
    print('Dados atualizados com sucesso!')

    cursor.execute(atualizar, valor)
    conexao.commit()

    menu()

def media_idades():
    cursor = conexao.cursor()
    media_idade = 'SELECT AVG (Idade) AS media FROM Estudantes '        

    consulta = cursor.execute(media_idade)
    for consultar in consulta:
        print(f'Media de idade dos alunos: {consultar}')
        
    conexao.commit()

    menu()

def sair():
    print('Saindo...')

def menu():
    opcao = int(input(''' 
    Escolha a opção: 
    [1] Inserir aluno
    [2] Atualizar nota
    [3] Conferir média
    [0] Sair
    Digite a opção: '''))

    if opcao == 1:
        insert_estudantes()
    elif opcao == 2:
        update_nota()
    elif opcao == 3:
        media_idades()
    elif opcao == 0:
        sair()
    else:
        print('Opção inválida\n Tente novamente!')
        menu()

    
menu()
