from models.admin import LoginAdmin
from views.utilidades import new_book, search
from instances import system_user, library


def login_adm():
    print('\nINSIRA SEUS DADOS DE ACESSO.')
    login = input('Login: ').lower().strip()
    password = input('Senha: ').strip()
    admin = LoginAdmin()

    if admin.verify_login(login, password):
        menu_admin()


def menu_admin():
    while True:
        print('\n=== ÁREA DO ADMINISTRADOR ===')
        print('[1] - Adicionar livro')
        print('[2] - Exibir livros')
        print('[3] - Exibir clientes')
        print('[4] - Buscar livro.')
        print('[5] - Remover livro')
        print('[0] - Sair')
        option = input('Escolha uma opção: ')
        print()

        if option == '1':
            book = new_book()
            if book:
                library.add_book(book)

        elif option == '2':
            library.list_books_by_status()
        
        elif option == '3':
            system_user.list_user()

        elif option == '4':
            title = search()
            library.search_book(title)

        elif option == '5':
            title = search()
            library.remove_book(title)    
        
        elif option == '0':
            print('Voltando para página inicial...')
            break
        else:
            print('⚠️ - OPÇÃO INVÁLIDA.\n')
