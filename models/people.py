class Pessoa:
    def __init__(self, name:str, age:int, cpf: str):
        self.name = name
        self.age = age
        self.cpf = cpf
        
    def show_people(self):
        print(f'Nome: {self.name} \nCPF:{self.cpf} \nIdade:{self.age}')


