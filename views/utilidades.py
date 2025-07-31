from models.book import Livro

def create_password():
    while True:
        print('Crie uma senha (mínimo 8 dígitos).')
        password = input('Senha: ')
        if len(password) < 8:
            print('⚠️ - A senha deve ter no mínimo 8 dígitos.\n')
        else:
            return password
        linha()


def new_book():
    title = input('Título: ').title().strip()
    author = input('Autor: ').title().strip()
    try:
        year = int(input('Ano de lançamento: '))
        if year < 0:
            print('⚠️ - Ano deve ser maior que 0')
            return None
    except ValueError:
        print('❌ - Digite apenas números')
        return None
    
    return Livro(title, author, year)

def search():
    return input('\nTítulo do livro: ').strip()


def linha():
    print('-'*40)