from models.user import Usuario
from storage import save_to_json, load_from_json
from models.people import Pessoa
from views.utilidades import linha


class SistemaUsuarios:
    def __init__(self):
        self.list_users = []
        self.load_users()
        
    def load_users(self):
        users_data = load_from_json('users.json')
        self.list_users = [Usuario.from_dict(u) for u in users_data]

    def save_users(self):
        users_data = [user.to_dict() for user in self.list_users]
        save_to_json(users_data, 'users.json')    
    
    def list_user(self):
        if not self.list_users:
            print('Nenhum usuário cadastrado.\n')
            return
        else:
            print('\n=== Clientes ===\n')
            for user in self.list_users:
                user.show_user()
                linha()

    def register_user(self, name: str, cpf: str, age: int, password: str):
        for user in self.list_users:
            if user.pessoa.cpf == cpf:
                print(f'⚠️ CPF {cpf} já está cadastrado.\n')
                return None
            
        pessoa = Pessoa(name, age, cpf)
        new_user = Usuario(pessoa, password)
        self.list_users.append(new_user)
        self.save_users()
        print(f'✅ Usuário cadastrado: {name} - CPF: {cpf}\n')
        return new_user

    
    def verify_cpf(self, cpf:str, password:str):
        for user in self.list_users:
            if user.pessoa.cpf == cpf and user.password == password:
                print('✅ Login efetuado!')
                return user
            
        print('⚠️ CPF ou senha incorretos.')
        return None


    def find_user_by_cpf(self, cpf):
        for user in self.list_users:
            if user.pessoa.cpf == cpf:
                return user
        return None
