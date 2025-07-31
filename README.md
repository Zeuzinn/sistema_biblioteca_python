# Sistema de Biblioteca em Python

## 📚 Descrição

Este projeto é um sistema de biblioteca desenvolvido em Python.  
Ele permite o gerenciamento de usuários e livros, controle de empréstimos, devoluções e persistência dos dados usando arquivos JSON.  

O sistema possui duas áreas principais:  
- **Cliente:** cadastro, login, aluguel e devolução de livros.  
- **Administrador:** gerenciamento de livros e visualização dos usuários cadastrados.

---

## ⚙️ Funcionalidades

- Cadastro e autenticação de usuários (com validação de CPF e senha).
- Cadastro e remoção de livros pelo administrador.
- Busca de livros por título.
- Controle de empréstimos vinculado ao usuário que realizou o aluguel.
- Empréstimo e devolução de livros, permitindo apenas devolução pelo usuário correto.
- Listagem de livros disponíveis e alugados.
- Persistência dos dados em arquivos JSON para manter o estado entre execuções.

---

## 🗂️ Estrutura do Projeto

```
biblioteca/
│
├── controllers/
│   ├── biblioteca_controllers.py
│   └── user_system.py
│
├── models/    
│   ├── admin.py
│   ├── book.py
│   ├── people.py
│   └── user.py
│
├── views/
│   ├── admin_menu.py
│   ├── client_menu.py
│   ├── home.py
│   └── utilidades.py
│
├── data/
│   ├── books.json
│   └── users.json
│
├── instances.py 
├── storage.py
├── main.py
└── README.md    
```

---

## 🚀 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/Zeuzinn/sistema_biblioteca_python.git
cd sistema-biblioteca-python
```

2. **Certifique-se que tem Python 3 instalado:**  
```bash
python --version
```

3. **Execute o sistema:**
```bash
python main.py
```

---

## 🛠️ Tecnologias e conceitos usados

- Python 3
- Programação orientada a objetos (POO)
- Manipulação de arquivos JSON para persistência
- Estrutura modular e organizada (Models, Controllers, Views)
- Validação básica de dados (CPF, idade, senhas)
- Controle de acesso (área de cliente vs. administrador)

---

## 📈 Possíveis melhorias futuras

- Implementação de interface gráfica (GUI)
- Uso de banco de dados (SQLite, PostgreSQL) para maior robustez
- Criptografia de senhas para segurança dos usuários
- Validação avançada de CPF e outros dados pessoais
- Relatórios e estatísticas de empréstimos e devoluções
- Testes automatizados (unitários e de integração)
- Deploy em ambiente web para acesso remoto

---

## 👤 Sobre o autor

**Eliseu Rodrigues** 

---

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.