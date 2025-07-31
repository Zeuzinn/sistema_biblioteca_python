from views.utilidades import create_password, search
from instances import system_user, library


def menu_client():
    while True:
        print('\n=== ÁREA DO CLIENTE ===')
        print('[1] - Criar cadastro')
        print('[2] - Efetuar login')
        print('[0] - Voltar ao início')
        option = input('Escolha uma opção: ')
        print()

        if option == '1':
            create_login()
        elif option == '2':
            login_client()
        elif option == '0':
            print('Voltando ao início...\n')
            break
        else:
            print('⚠️ - Opção inválida.\n')


def create_login():
    name = input('Nome completo: ').title().strip()
    cpf = input('CPF (Apenas dígitos): ').strip()
    cpf = validate_cpf(cpf)
    
    if not cpf:
        return  
    
    try:
        age = int(input('Idade:'))
        if age < 0:
            print('Idade deve ser maior que 0')
            return
    except ValueError:
        print('⚠️ - Idade deve ser apenas números')
        return
    
    password = create_password()
    system_user.register_user(name, cpf, age, password)

    
def validate_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        print('⚠️ CPF INVÁLIDO! Use apenas 11 dígitos numéricos.')
        return None
    return cpf


def login_client():
    print('\n=== LOGIN CLIENTE ===')
    cpf = input('CPF: ').strip()
    cpf = validate_cpf(cpf)
    if not cpf:
        return
    
    password = input('Senha: ').strip()

    user = system_user.verify_cpf(cpf, password)
    if user:
        print(f'\n✅ Login bem-sucedido. Bem-vindo(a), {user.pessoa.name}!')
        # ✅ Passa o CPF do usuário para rastrear quem faz as ações
        client_area(user.pessoa.cpf)
    else:
        print('⚠️ - Login falhou. Verifique CPF e senha.\n')


def client_area(cpf):
    while True:
        print('\n=== BIBLIOTECA ===')
        print('[1] - Alugar Livro')
        print('[2] - Devolver Livro')
        print('[3] - Exibir Livros')
        print('[0] - Sair')
        option = input('Escolha uma opção: ').strip()
        print()

        if option == '1':
            title = search()
            library.search_borrow_book(title, cpf)

        elif option == '2':
            title = search()
            library.search_return_book(title, cpf)
        
        elif option == '3':
            library.list_books_by_status()
        
        elif option == '0':
            print('Saindo da área do cliente...')
            break
        else:
            print('⚠️ - OPÇÃO INVÁLIDA\n')
        
