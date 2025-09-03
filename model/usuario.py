import uuid
import bcrypt

class Usuario:
    def __init__(self, nome, cpf, email, senha, perfil="user", id=None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        self.perfil = perfil

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "perfil": self.perfil
        }
    
    def verificar_senha(self, senha):
        return bcrypt.checkpw(senha.encode("utf-8"), self.senha.encode("utf-8"))
    
    @staticmethod
    def from_dict(data):
        usuario = Usuario(
            data["nome"],
            data["cpf"],
            data["email"],
            "senha_temporaria",
            data.get("perfil", "user"),
            data["id"]
        )
        usuario.senha = data["senha"]
        return usuario