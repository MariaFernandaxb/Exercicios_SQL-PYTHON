import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

def insert_produtos():
    cursor = conexao.cursor()
    print('Insira o novo produto')
    nome = input('Digite o nome do produto: ')
    preco = float(input(f'Digite o valor do {nome}: R$ '))
    valor = [nome, preco]
    produto = 'insert into Produtos (Nome, Preço) values (? , ?) '
    print(f'{nome} cadastrado com sucesso')

    cursor.execute(produto,valor)
    conexao.commit()

    return_menu()

def insert_venda(): 
    cursor = conexao.cursor()
    consulta = cursor.execute('select id, Nome, Preço from Produtos')
    for consultar in consulta: 
        print(f'ID : {consultar[0]} | NOME: {consultar[1]} | PREÇO: {consultar[2]:.2f}')

    print('Digite os dados da venda')
    produto_id = int(input('Digite o ID do produto:'))
    qntd = int(input('Quantidade vendida: '))
    data = input('Data da venda: ')
    valor = [produto_id, qntd, data]
    venda = 'insert into Vendas (produto_id, quantidade, data) values (? , ? , ?)'
    print(f'Venda realizada com sucesso')

    cursor.execute(venda,valor)
    conexao.commit()

    return_menu()

def tot_vendas():
    cursor = conexao.cursor()
    print('Total de vendas de 2023')

    total = 'SELECT Nome,SUM(quantidade*preço) as totaldevendas from Produtos p inner join Vendas v WHERE v."Data" LIKE "%2023" and p.ID = v.Produto_id group by p.Nome order by totaldevendas DESC '
    
    resultados = cursor.execute(total)
    for  resultado in resultados:
        print(f'PRODUTO: {resultado[0]} TOTAL: {resultado[1]:.2f}')

    return_menu()

def return_menu():
    retornar_menu = input('Deseja voltar ao menu ?\n 1-Sim \n 2-Não \n ')
    if retornar_menu == '1':
        menu_loja()
    else: 
        sair()

def sair():
    print('Finalizando...')
    conexao.close()
    
def menu_loja():
    print('=- '*5,'LOJA TEM TUDO', '=- '*5)
    opcao = int(input('''
    Escolha a opção: 
    [1] Inserir produtos
    [2] Inserir venda
    [3] Total de vendas
    [0] Sair
    Digite a opção: '''))

    if opcao == 1:
        insert_produtos()
    elif opcao == 2:
        insert_venda()
    elif opcao == 3:
        tot_vendas()
    elif opcao == 0:
        sair()
    else:
        print('Opção inválida\n Tente novamente!')
        menu_loja()

menu_loja()