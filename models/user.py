from models.people import Pessoa


class Usuario:
    def __init__(self, pessoa: Pessoa, password: str):
        self.pessoa = pessoa
        self.password = password
        self._rented = []

    def show_user(self):
        self.pessoa.show_people()
    
    def to_dict(self):
        return {
            'name': self.pessoa.name,
            'cpf': self.pessoa.cpf,
            'age': self.pessoa.age,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        pessoa = Pessoa(data['name'], data['age'], data['cpf'])
        return cls(pessoa, data['password'])

