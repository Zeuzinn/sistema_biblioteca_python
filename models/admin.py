class LoginAdmin:
    def __init__(self):
        self.login = 'admin'
        self.password = '1234'

    def verify_login(self, login:str, password:str):
        if login.lower() == self.login and password.lower() == self.password:
            print('✅ Acesso permitido.\n')
            return True
        else:
            print('❌ Login incorreto.\n')
            return False

