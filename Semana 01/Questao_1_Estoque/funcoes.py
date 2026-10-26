'''Equipe: Douglas, Fernando, Nathiara e Mario'''

def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 Adicionar produto")
    print("2 Remover produto")
    print("3 Atualizar quantidade")
    print("4 Exibir estoque")
    print("0 Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def ler_quantidade(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd >= 0:
                return qtd
            else:
                print("Erro: A quantidade não pode ser negativa.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem)
        texto = texto.strip()
        texto = texto.title()
        if texto != "":
            return texto
        else:
            print("Erro: O campo não pode ficar vazio.")

def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print("Produto já cadastrado. Use a opção de atualizar quantidade.")
    else:
        estoque[nome] = quantidade
        print("Produto adicionado com sucesso.")

def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")

def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print("Quantidade atualizada com sucesso.")
    else:
        print("Produto não encontrado.")

def exibir_estoque(estoque):
    if len(estoque) == 0:
        print("Estoque vazio.")
    else:
        print("\n--- Produtos em Estoque ---")
        for nome in estoque:
            qtd = estoque[nome]
            print(nome + ": " + str(qtd) + " unidade(s)")
