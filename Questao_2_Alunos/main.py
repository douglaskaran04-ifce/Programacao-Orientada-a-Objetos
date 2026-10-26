from dados import alunos
from funcoes import exibir_menu, ler_texto, ler_quatro_notas, adicionar_aluno, atualizar_notas, remover_aluno, exibir_alunos, exibir_medias

while True:
    opcao = exibir_menu()
    
    if opcao == '1':
        nome = ler_texto("Digite o nome do aluno: ")
        notas = ler_quatro_notas()
        adicionar_aluno(alunos, nome, notas)
        
    elif opcao == '2':
        nome = ler_texto("Digite o nome do aluno que deseja atualizar: ")
        if nome in alunos:
            notas = ler_quatro_notas()
            atualizar_notas(alunos, nome, notas)
        else:
            print("Aluno não encontrado.")
            
    elif opcao == '3':
        nome = ler_texto("Digite o nome do aluno a ser removido: ")
        remover_aluno(alunos, nome)
        
    elif opcao == '4':
        exibir_alunos(alunos)
        
    elif opcao == '5':
        exibir_medias(alunos)
        
    elif opcao == '0':
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
