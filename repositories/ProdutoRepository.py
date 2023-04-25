from entities.Produto import Produto
import mysql.connector

class ProdutoRepository:
    @staticmethod
    def create_produto(produto):
        conexao = ProdutoRepository.__conexao()
        cursor = conexao.cursor()
        comando = f'INSERT INTO produto (nome, preco, quantidade) VALUES ("{produto.nome}", {produto.preco}, {produto.quantidade});'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def exibir_produtos():
        conexao = ProdutoRepository.__conexao()
        cursor = conexao.cursor()
        comando = f'SELECT * FROM produto;'
        cursor.execute(comando)
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        for id, nome, preco, quantidade in dados:
            print('Nome: {} / Preco: R$ {} / Quantidade: {}'.format(nome, preco, quantidade))

    @staticmethod
    def buscar_produtos():
        conexao = ProdutoRepository.__conexao()
        cursor = conexao.cursor()
        comando = f'SELECT * FROM produto;'
        cursor.execute(comando)
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        lista_produtos = []
        for id, nome, preco, quantidade in dados:
            prodAux = Produto(nome, preco, quantidade)
            lista_produtos.append(prodAux)
        return lista_produtos

    @staticmethod
    def delete_produto(nomeProduto):
        conexao = ProdutoRepository.__conexao()
        cursor = conexao.cursor()
        comando = f'DELETE FROM produto WHERE nome="{nomeProduto}"'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def __conexao():
        return mysql.connector.connect(host='localhost', user='root', password='', database='atividadePython')
