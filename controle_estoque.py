"""
@author: Pedro Vasconcelos
"""

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
class PessoaFis(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self.cpf = cpf
        
class PessoaJu(Pessoa):
    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self.cnpj = cnpj
        
class Produto:
    def __init__(self, nomePro, estoque, preco, estoqueMin=0):
        self.nomePro = nomePro
        self.estoque = estoque
        self.preco = preco
        self.estoqueMin = estoqueMin
        
class Compra(Produto):
    def __init__(self, dataCompra, nomePro, quantiCompra, preco, estoque):
        Produto.__init__(self, nomePro, quantiCompra, preco, estoque)
        self.dataCompra = dataCompra
        self.quantiCompra = quantiCompra
        
        if quantiCompra > estoque:
            print("Valor máximo de estoque atingido")
            return
        else:
            self.estoque = quantiCompra + estoque
            print("Histórico de compra: A compra foi efetuada na data: {}, do produto {}, no qual foi comprado {} produtos pelo preço de {} reais, novo estoque: {}". format(dataCompra, nomePro, quantiCompra, preco, self.estoque))
            
class Venda(Produto):
    def __init__(self, dataVen, nomePro, quantiVen, estoque, preco, ganhoVen):
        Produto.__init__(self, nomePro, estoque, preco)
        self.dataVen = dataVen
        self.quantiVen = quantiVen
        
        if quantiVen < self.estoqueMin:
            print("Estoque mínimo ultrapassado")
            return
        else:
            self.estoque = quantiVen + estoque
            self.ganhoVen = preco*quantiVen
            print("Histórico de venda: A compra foi efetuada na data: {}, do produto {}, no qual foi comprado {} produtos pelo preço de {} reais, novo estoque: {}". format(dataVen, nomePro, quantiVen, preco, self.estoque))
            
    
cliente1 = PessoaFis("Pedro", "00011122233")
print(cliente1.nome)
print(cliente1.cpf)
print("=_"*10)
cliente2 = PessoaJu("Bramil", "1991919")
print(cliente2.nome)
print(cliente2.cnpj)
print("=_"*10)
produto1 = Produto("Arroz", 10, 3)
print(produto1.nomePro)
print("Estoque inicial do Arroz: ", produto1.estoque)
print("Preço do Arroz: ", produto1.preco)
print("=_"*10)
produto2 = Produto("Feijão", 9, 2)
print(produto2.nomePro)
print("Estoque inicial do Feijão: ", produto2.estoque)
print("Preço feijão: ", produto2.preco)
print("=_"*10)
compra1 = Compra("10/11", "Arroz", 7, 3, 10)
print("Compra efetuada por: ", cliente2.nome)
print("Data da compra: ", compra1.dataCompra)
print("Produto: ", compra1.nomePro)
print("Quantidade Comprada: ", compra1.quantiCompra)
print("Preço: ", compra1.preco)
print("Novo estoque: ", compra1.estoque)
print("=_"*10)
venda1 = Venda("10/10", "Feijão", 3, 9, 2, 0)
print("Venda efetuada por: ", cliente1.nome)
print("Data da venda: ", venda1.dataVen)
print("Produto: ", venda1.nomePro)
print("Quantidade vendida: ", venda1.quantiVen)
print("Novo estoque: ", venda1.estoque)
print("Preço vendido: ", venda1.preco)
print("Total ganho com as vendas: ", venda1.ganhoVen)