let width = document.querySelector('.menu-list')
function abre(){
    width.style.width='70%'
}
function fecha(){
    width.style.width='0%'
}

let usuarios = []

function cadastrar(){
    let guardaNome = document.querySelector('#nome').value
    let guardaSenha = document.querySelector('#senha').value
    let usuario = {nome: guardaNome, senha: guardaSenha}
    usuarios.push(usuario)
    
    
    console.log(usuarios)
}
