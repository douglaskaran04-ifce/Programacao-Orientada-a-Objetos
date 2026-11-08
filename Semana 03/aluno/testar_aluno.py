from aluno import Aluno

aluno1 = Aluno("Maria Silva", "2024001")
aluno2 = Aluno("João Souza", "2024002")
aluno3 = Aluno("Ana Lima", "2024003")

lista_alunos = [aluno1, aluno2, aluno3]

# Adicionando notas e faltas pelos metodos
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)
aluno1.registrar_falta()
aluno1.registrar_falta()

aluno2.adicionar_nota(5.5)
aluno2.registrar_falta()
aluno2.registrar_falta()
aluno2.registrar_falta()
aluno2.registrar_falta()
aluno2.registrar_falta()
aluno2.registrar_falta()

# A aluna Ana (aluno3) vai ficar sem notas para testar o media 0.0

# 3 testes invalidos (nota 11, nota -2, matricula vazia)
if aluno1.adicionar_nota(11) == False:
    print("Nota inválida: use um valor entre 0 e 10.")

if aluno1.adicionar_nota(-2) == False:
    print("Nota inválida: use um valor entre 0 e 10.")

if aluno2.set_matricula("   ") == False:
    print("Matrícula inválida: não pode ser vazia.")

print()

total_aulas = 40
maior_media = None # Campeão da quadra

for aluno in lista_alunos:
    print(aluno)
    
    if aluno.verificar_aprovacao(total_aulas):
        print("Situação: aprovado")
    else:
        print("Situação: reprovado")
        
    # Verificando a maior media (Campeão da quadra)
    media_atual = aluno.calcular_media()
    
    if maior_media == None or media_atual > maior_media.calcular_media():
        maior_media = aluno

print(f"\nMaior média: {maior_media.nome} ({maior_media.calcular_media():.2f})")