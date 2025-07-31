class Livro:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.available = True  
        self.rented = False
        self.rented_for = None


    def return_book(self):
        self.available = True

    def borrow_book(self):
        self.available = False
    
    def show_info(self):
        status = "✅" if self.available else "❌"
        print(f'Titulo: {self.title} \nAutor: {self.author} \nAno de publicação: {self.year} \nDisponível: {status}')


    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'available': self.available,
            'rented': self.rented,
            'rented_for': self.rented_for
        }

    @classmethod
    def from_dict(cls, data):
        livro = cls(data['title'], data['author'], data['year'])
        livro.available = data['available']
        livro.rented = data['rented']
        livro.rented_for = data['rented_for']
        return livro