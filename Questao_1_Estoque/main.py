from dados import estoque
from funcoes import exibir_menu, ler_texto, ler_quantidade, adicionar_produto, remover_produto, atualizar_quantidade, exibir_estoque

while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        nome = ler_texto("Digite o nome do produto: ")
        quantidade = ler_quantidade("Digite a quantidade inicial: ")
        adicionar_produto(estoque, nome, quantidade)
        
    elif opcao == '2':
        nome = ler_texto("Digite o nome do produto que deseja remover: ")
        remover_produto(estoque, nome)
        
    elif opcao == '3':
        nome = ler_texto("Digite o nome do produto que deseja atualizar: ")
        quantidade = ler_quantidade("Digite a nova quantidade: ")
        atualizar_quantidade(estoque, nome, quantidade)
        
    elif opcao == '4':
        exibir_estoque(estoque)
        
    elif opcao == '0':
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
