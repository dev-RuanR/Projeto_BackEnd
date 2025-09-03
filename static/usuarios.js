
//
function preencherFormulario(button) {
    const funcionario = JSON.parse(button.getAttribute('data-funcionario'));
    document.getElementById('id').value = funcionario.id;
    document.getElementById('nome').value = funcionario.nome;
    document.getElementById('email').value = funcionario.email;
    document.getElementById('cpf').value = funcionario.cpf;
    document.getElementById('cargo').value = funcionario.cargo;
}

function atualizarFuncionario() {
    alert('Funcionário atualizado com sucesso!');
}

function excluirFuncionario(id, cpf) {
    if(confirm(`Tem certeza que deseja excluir o funcionário com CPF ${cpf}?`)) {
        document.getElementById(`linha-${id}`).remove();
        alert('Funcionário excluído com sucesso!');
    }
}


//Scripts da tela de login:
document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Validação básica
            if (!email.endsWith('@senaipark.com.br')) {
                showMessage('Por favor, use um email @senaipark.com.br', 'error');
                return;
            }
            
            if (password.length < 6) {
                showMessage('A senha deve ter pelo menos 6 caracteres', 'error');
                return;
            }
            
            // Simular login bem-sucedido
            showMessage('Login realizado com sucesso!', 'success');
            
           
        });
        
        function showMessage(text, type) {
            const messageDiv = document.getElementById('loginMessage');
            messageDiv.textContent = text;
            messageDiv.className = `message ${type}-message`;
            messageDiv.style.display = 'block';
            
            // Esconder a mensagem após 5 segundos
            setTimeout(() => {
                messageDiv.style.display = 'none';
            }, 5000);
        }