import sqlite3

conexao = sqlite3.connect('banco2.sqlite3')
cursor = conexao.cursor()

def insert_post():
    cursor = conexao.cursor()
    titulo = input('TÍTULO: ')
    conteudo = input('CONTEÚDO: ')    
    valor = [titulo, conteudo] 
    inserir_posts = 'Insert into Posts (titulo, conteudo) values (? , ?)'
    print('Dados inseridos com sucesso!')


    cursor.execute(inserir_posts, valor)
    conexao.commit()
    conexao.close()

def insert_coment():
    cursor = conexao.cursor()
    post_id = int(input('Digite o ID do post: '))
    texto = input('TEXTO: ')
    valor = [post_id, texto]
    inserir_coment = 'Insert into Comentários (post_id, texto) values (? , ?)'
    print('Dados inseridos com sucesso!')
    
    cursor.execute(inserir_coment, valor)
    conexao.commit()
    conexao.close()    


def delete_post():
    cursor = conexao.cursor()
    post_id = 'DELETE FROM posts WHERE ID NOT IN (SELECT DISTINCT post_id FROM Comentários)'
    print('Dados excluídos com sucesso!')

    cursor.execute(post_id)
    conexao.commit()
    conexao.close()

def sair():
    print('Finalizando...')

def menu():
    opcao = int(input('''
    Escolha uma opção: 
    [1] Postar 
    [2] Comentar 
    [3] Excluir Post
    [0] Sair 
                  
    Digite aqui a opção: '''))

    if opcao == 1:
        insert_post()
    elif opcao == 2:
        insert_coment()
    elif opcao == 3:
        delete_post()
    elif opcao == 0:
        sair()
    else:
        print('Opção inválida\n Tente novamente!')
        menu()


menu()