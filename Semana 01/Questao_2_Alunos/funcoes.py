def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 Adicionar aluno")
    print("2 Atualizar notas")
    print("3 Remover aluno")
    print("4 Exibir alunos e notas")
    print("5 Exibir médias")
    print("0 Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if nota >= 0.0 and nota <= 10.0:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")

def ler_quatro_notas():
    notas = []
    
    nota1 = ler_nota("Digite a nota N1: ")
    notas.append(nota1)
    
    nota2 = ler_nota("Digite a nota N2: ")
    notas.append(nota2)
    
    nota3 = ler_nota("Digite a nota N3: ")
    notas.append(nota3)
    
    nota4 = ler_nota("Digite a nota N4: ")
    notas.append(nota4)
    
    return notas

def ler_texto(mensagem):
    while True:
        texto = input(mensagem)
        texto = texto.strip()
        texto = texto.title()
        if texto != "":
            return texto
        else:
            print("Erro: O nome não pode ficar vazio.")

def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print("Aluno já cadastrado. Use a opção de atualizar notas.")
    else:
        alunos[nome] = notas
        print("Aluno adicionado com sucesso.")

def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print("Notas atualizadas com sucesso.")
    else:
        print("Aluno não encontrado.")

def remover_aluno(alunos, nome):
    if nome in alunos:
        del alunos[nome]
        print("Aluno removido com sucesso.")
    else:
        print("Aluno não encontrado.")

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / 4
    return media

def exibir_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos e Notas ---")
        for nome in alunos:
            notas = alunos[nome]
            print(nome + ": " + str(notas))

def exibir_medias(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Médias dos Alunos ---")
        for nome in alunos:
            notas = alunos[nome]
            media = calcular_media(notas)
            print(f"{nome}: Média = {media:.2f}")
