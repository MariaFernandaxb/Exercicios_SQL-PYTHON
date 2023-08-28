import sqlite3 
import time

conexao = sqlite3.connect('bd.sqlite3')

def insert_aluno():
    aluno = input('Digite o nome do aluno: ')
    idade = int(input(f'Digite a idade do(a){aluno}: '))

    dados = [aluno, idade]
    inserir = 'INSERT INTO ALUNOS (Nome, Idade) values (?,?)'
    print(f'{aluno} foi cadastrado(a) com sucesso!')        
  
    cursor = conexao.cursor()
    cursor.execute(inserir,dados)
    conexao.commit()

    return_menu()

def consult_aluno():
    cursor = conexao.cursor()
    alunos = 'select * from ALUNOS'

    consulta = cursor.execute(alunos)
    print('Lista dos alunos: ')
    for resultado in consulta: 
        print(f' {resultado} ')

    return_menu()  

def consult_filter():
    cursor = conexao.cursor()
    alunos = 'select * from ALUNOS Where idade > 20'

    consulta = cursor.execute(alunos)
    print('Lista dos alunos maiores de 20 anos: ')
    for resultado in consulta: 
        print(f' {resultado} ')
    
    return_menu()

def update_aluno():
    cursor = conexao.cursor()
    consulta = cursor.execute('select id, Nome, Idade from ALUNOS')
    for consultar in consulta: 
        print(f'ID : {consultar[0]} | NOME: {consultar[1]} | IDADE: {consultar[2]}')

    print('Selecione o ID do aluno que deseja atualizar a idade: ')
    aluno_id = int(input('Digite o ID do aluno: '))
    idade = int(input("Atualize a idade para: "))
    atualizar = 'UPDATE ALUNOS set idade = ? where id = ? '
    valor = [idade, aluno_id]
    print('Dados do atualizados com sucesso')

  
    cursor.execute(atualizar, valor)
    conexao.commit()
   
    return_menu()

def delete_aluno():
    cursor = conexao.cursor()
    print('Selecione o ID do aluno que deseja excluir:  ')
    consulta = cursor.execute('select id, Nome, Idade from ALUNOS')
    for consultar in consulta: 
        print(f'ID : {consultar[0]} | NOME: {consultar[1]} | IDADE: {consultar[2]}')

    print('Selecione o ID do aluno que deseja excluir: ')
    aluno_id = int(input('Digite o ID do aluno: '))
    atualizar = 'DELETE from ALUNOS where id = ? '
    valor = [aluno_id]
    print(f'Aluno com ID: {aluno_id} excluído com sucesso')

    cursor.execute(atualizar, valor)
    conexao.commit()

    return_menu()

def return_menu():
    retornar_menu = input('Deseja voltar ao menu ?\n 1-Sim \n 2-Não \n ')
    if retornar_menu == '1':
        menu()
    else: 
        exit_menu()


def exit_menu():
    print('Saindo da base de dados')
    time.sleep(1)
    print('Até mais! ')
  
def menu():
    menu_alunos = int(input('''BANCO DE DADOS - ULTIMA.SCHOOL 
    Escolha uma das opções:
    [1]Cadastrar aluno: 
    [2]Listar alunos:
    [3]Consultar alunos maiores de 20 anos:
    [4]Atualizar idade de aluno:
    [5]Excluir aluno:
    [0]Sair
    Digite a opção: '''))

    if menu_alunos == 1:
        insert_aluno()
    elif menu_alunos ==2:
        consult_aluno()
    elif menu_alunos == 3:
        consult_filter()
    elif menu_alunos == 4:
        update_aluno()
    elif menu_alunos == 5:
        delete_aluno()
    elif menu_alunos == 0:
       exit_menu()
    else: 
        print('Opção inválida')
        menu()

menu()