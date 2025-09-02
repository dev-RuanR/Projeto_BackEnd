# # 📌 Mini Sistema - Parque Senai em Python

Este projeto é um **mini sistema em Python** que permite **cadastrar, validar e gerenciar registros**, seguindo uma arquitetura organizada em **Controller** e **Service**.

## 🚀 Tecnologias utilizadas
- **Python 3.10+**
- **Flask** (para criação das rotas)

---

## 📂 Parque Senai

├── app.py # Arquivo principal do Flask
├── requirements.txt # Lista de dependências
├── users.json # Nosso "banco de dados"
├── controller/
│ └── usuario_controller.py
├── model/
│ └── usuario.py
├── repository/
│ └── usuario_repository.py
├── service/
│ └── usuario_service.py
└── templates/ # Pasta para os arquivos HTML
 ├── login.html
 ├── cadastro.html
 └── lista_usuarios.html
