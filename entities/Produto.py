class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'Nome: {self.nome} / Preco: R$ {self.preco} / Quantidade: {self.quantidade}'