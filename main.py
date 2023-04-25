from entities.Produto import Produto
from repositories.ProdutoRepository import ProdutoRepository
opcao = 0
while opcao != 4:
    print('---MENU---')
    print('1 - Cadastrar Produto')
    print('2 - Exibir Produtos')
    print('3 - Excluir Produto')
    print('4 - SAIR')
    opcao = int(input('Informe a opção (numero): '))
    if opcao == 1:
        print('\n\n---Cadastro de Produto---')
        nome = input('Informe o nome do produto: ')
        preco = float(input('Informe o preco do produto: '))
        quantidade = int(input('Informe a quantidade: '))
        prod = Produto(nome, preco, quantidade)
        ProdutoRepository.create_produto(prod)

    elif opcao == 2:
        print('\n\n---Exibir Produtos---')
        for item in ProdutoRepository.buscar_produtos():
            print(item)
    elif opcao == 3:
        print('\n\n---Excluir Produto---')
        nomeProduto = input('Informe o nome do produto: ')
        ProdutoRepository.delete_produto(nomeProduto)
