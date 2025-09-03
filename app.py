from flask import Flask, render_template, request, jsonify
import json
import os
import  uuid


app = Flask(__name__)

def carregar_usuarios():
    #FUNÇÃO PARA CARREGAR USUÁRIOS DO ARQUIVO JSON
    try:
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r") as file:
                return json.load(file)
        return []
    except:
        return []
    
def salvar_usuarios(usuarios):
    #FUNÇÃO PARA SALVAR USUÁRIOS NO ARQUIVO JSON
    usuarios = carregar_usuarios()

    try:  
        usuarios.append(usuarios)

        with open("usuarios.json", "w", enconding="utf-8") as file:
            json.dump(usuarios, file, indent=4)

        return True
    except:
        return False 
    
def deletar_usuarios(id):
    #FUNÇÃO PARA DELETAR USUÁRIOS DO ARQUIVO JSON
    usuarios = carregar_usuarios()
    usuarios_atualizados = [usuario for usuario in usuarios if usuario["id"] != id]
 
    if len(usuarios) == len(usuarios_atualizados):
        return False 
    try:
        with open("usuarios.json", "w", encoding="utf-8") as file:
            json.dump(usuarios_atualizados, file, indent=4)
        return True
    except:
        return False
    

@app.route("/") # ROTA PARA A PÁGINA DE CADASTRO
def home():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])#CAPTURE O FORMULÁRIO E CHAME A FUNÇÃO
def cadastrar_usuario():
    
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    senha = request.form.get("senha")

    funcionario = {
        "id" : str(uuid.uuid4()),
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha
    }

    if status := salvar_usuarios(funcionario):
        return f"Usuário '{nome}' cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar usuário", 500

@app.route("/usuarios/json") # ROTA PARA LISTAR USUÁRIOS EM JSON
def buscar_users_json():
    usuarios = carregar_usuarios()
    return jsonify(usuarios)

@app.route("/usuarios") # ROTA PARA LISTAR USUÁRIOS NA TELA
def buscar_usuarios():
    usuarios = carregar_usuarios()
    return render_template("funcionarios.html", usuarios=usuarios)

if __name__ == '__main__':
    # Inicia o servidor Flask em modo de desenvolvimento
    app.run(debug=True)