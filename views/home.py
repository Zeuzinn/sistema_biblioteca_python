from views.client_menu import menu_client
from views.admin_menu import login_adm


def home():
    while True:
        print('\n==== SEJA BEM VINDO A BIBLIOTECA! ====\n')
        print('[1] - Sou cliente.')
        print('[2] - Sou bibliotecário.')
        print('[0] - Sair do sistema.')
        print('======================================')
        option = input('Escolha uma opção: ').strip()
        print()
        if option == '1':
            menu_client()
        elif option == '2':
            login_adm()
        elif option == '0':
            print('Encerrando Sistema...')
            break
