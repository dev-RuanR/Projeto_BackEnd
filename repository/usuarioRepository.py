import json
import os
from model.usuario import Usuario

class UsuarioRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self._criar_arquivo_se_nao_existir()
    
    def _criar_arquivo_se_nao_existir(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def _ler_usuarios(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    def _escrever_usuarios(self, usuarios):
        with open(self.file_path, 'w') as f:
            json.dump([u.to_dict() if hasattr(u, 'to_dict') else u for u in usuarios], f, indent=4)
    
    def salvar(self, usuario):
        usuarios = self._ler_usuarios()
        usuarios_existentes = [u for u in usuarios if u['id'] != usuario.id]
        usuarios_existentes.append(usuario.to_dict())
        self._escrever_usuarios(usuarios_existentes)
        return usuario
    
    def buscar_por_id(self, id):
        usuarios = self._ler_usuarios()
        for usuario_data in usuarios:
            if usuario_data['id'] == id:
                return Usuario.from_dict(usuario_data)
        return None
    
    def buscar_por_email(self, email):
        usuarios = self._ler_usuarios()
        for usuario_data in usuarios:
            if usuario_data['email'] == email:
                return Usuario.from_dict(usuario_data)
        return None
    
    def listar_todos(self):
        usuarios = self._ler_usuarios()
        return [Usuario.from_dict(usuario_data) for usuario_data in usuarios]
    
    def excluir(self, id):
        usuarios = self._ler_usuarios()
        usuarios = [u for u in usuarios if u['id'] != id]
        self._escrever_usuarios(usuarios)
        return True 