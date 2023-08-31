while (sabor == 1 || sabor == 2) { 
  sabor = parseInt('Informe o tipo de sorvete desejado: 1-Para chocolate ou 2-Para morango:')
   quantidade = parseInt('Informe a quantidade desejada:')

    if (sabor == 1) {
        if (quantidade >= 3){
        
        alert('VOCÊ TEM O DESCONTO DE 10% ')

        }else {
            alert('VOCÊ TEM O DESCONTO DE 5% ')
        }
    }else if (sabor == 2){
        alert('VOCÊ NÃO TEM DESCONTO NENHUM')
    }
    alert('VOCÊ NÃO TEM DESCONTO NENHUM')
    sabor = parseInt('Informe o tipo de sorvete desejado: 1-Para chocolate ou 2-Para morango:')
    quantidade = parseInt('Informe a quantidade desejada:')
  
}