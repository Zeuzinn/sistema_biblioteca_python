from models.book import Livro
from storage import save_to_json, load_from_json
from views.utilidades import linha


class Biblioteca:
    def __init__(self):
        self.bookcase = []
        self.load_books()


    def load_books(self):
        books_data = load_from_json('books.json')
        self.bookcase = [Livro.from_dict(b) for b in books_data]

    def save_books(self):
        books_data = [book.to_dict() for book in self.bookcase]
        save_to_json(books_data, 'books.json')

    def add_book(self, book: Livro):
        self.bookcase.append(book)
        self.save_books()
        print('✅  Livro adicionado!\n')

    def search_book(self, name: str):
        found = False
        for book in self.bookcase:
            if name.lower() in book.title.lower() or name.lower() in book.author.lower():
                print('\n📚 Livro encontrado!')
                book.show_info()
                print('-'*30)
                found = True
        if not found:
            print('🚫 Nenhum livro encontrado com esse título ou autor.')

    def search_borrow_book(self, title:str, cpf:str):
        from instances import system_user  # Import local, só quando chama o método
        
        for book in self.bookcase:
            if book.title.lower() == title.lower():
                if book.rented:
                    print('⚠️ - Livro já está alugado.')
                    return
                
                book.rented = True
                book.rented_for = cpf
                self.save_books()
                print(f'✅ Livro "{book.title}" alugado com sucesso.')
                return
        print('⚠️ Livro não encontrado.')

    def search_return_book(self, title:str, cpf:str):
        from instances import system_user 
        
        for book in self.bookcase:
            if book.title.lower() == title.lower():
                if not book.rented:
                    print('⚠️ Este livro não está alugado.')
                    return
                
                if book.rented_for != cpf:
                    print('⚠️ Você não pode devolver este livro. Ele foi alugado por outro usuário.')
                    return
                
                book.rented = False
                book.rented_for = None
                print(f'✅ Livro "{book.title}" devolvido com sucesso.')
                return
        print('⚠️ Livro não encontrado.')
                
    def list_books_by_status(self):
        if not self.bookcase:
            print('Biblíoteca vazia.\n')
            return

        print('📚 Livros Disponíveis:\n')
        for b in self.bookcase:
            if not b.rented:
                b.show_info()
                linha()

        print('\n📕 Livros Emprestados:\n')
        for b in self.bookcase:
            if b.rented:
                b.show_info()
                linha()

    def remove_book(self, name:str):
        found = False
        for book in self.bookcase:
            if name.lower() in book.title.lower():
                self.bookcase.remove(book)
                self.save_books()
                print(f'✅ Livro "{book.title}" removido com sucesso!')
                print('-'*30)
                found = True
                break
        if not found:
            print('🚫 Nenhum livro encontrado com esse título ou autor.')
