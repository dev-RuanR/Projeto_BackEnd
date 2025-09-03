
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


