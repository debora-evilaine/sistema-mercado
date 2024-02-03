from datetime import datetime

class Produto():
    def __init__(self, nome, categorias, fornecedores, quantidade_disponivel):
        self.nome = nome
        self.fornecedores = fornecedores
        self.quantidade_disponivel = quantidade_disponivel
        self.categorias = categorias
        self.lista_de_produtos =[]

class Cliente():
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Mercado():
    def __init__(self):
        self.lista_clientes = []
        self.lista_produtos = []
        self.lista_transacoes = []
    
    def cadastrar_cliente(self, cliente):
        if cliente.telefone not in self.lista_clientes:
            self.lista_clientes.append({"Nome do cliente": cliente.nome, "Telefone": cliente.telefone, "Endereço": cliente.endereco})
            print(f"O cliente {cliente.nome} foi cadastrado!")
        else:
            print("O cliente já está cadastrado!") 

    def cadastrar_produto(self, produto):
        if produto.nome not in self.lista_produtos:
            self.lista_produtos.append({"Nome do produto": produto.nome, "Quantidade": produto.quantidade_disponivel})
            print("O produto foi cadastrado!")
        else:
            produto["Quantidade"] += 1
            print("O produto aumentou de estoque!")
    
    def realizar_compra(self, produto, quantidade, cliente):
        for produtos in self.lista_produtos:
            print(produto.nome)
            if produtos["Nome do produto"] == produto.nome:
                if produtos["Quantidade"] >= quantidade:
                    produtos["Quantidade"] -= quantidade
                    self.lista_transacoes.append({"Nome do cliente": cliente.nome, "Quantidade": quantidade, "Data da compra": datetime.now()})
                    print(f"Você comprou {produto.nome}!")
                else:
                    print(f"Produto {produto.nome} fora de estoque!")
                
cliente = Cliente("Vanilza","4530982", "Rua das Flores")
produto = Produto("Pia", "banheiro", "fornecedor 3", 150)

mercado = Mercado()
mercado.cadastrar_cliente(cliente)
print(mercado.lista_clientes)
print()
print()
mercado.cadastrar_produto(produto)
print(mercado.lista_produtos)

print()
print()

mercado.realizar_compra(produto, 2, cliente)
print(mercado.lista_produtos)
mercado.realizar_compra(produto, 200, cliente)
print(mercado.lista_transacoes)