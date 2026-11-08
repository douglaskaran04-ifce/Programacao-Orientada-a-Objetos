class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.faltas = 0

    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
            return True
        else:
            return False

    def registrar_falta(self):
        self.faltas = self.faltas + 1

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
            
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media

    def verificar_aprovacao(self, total_aulas):
        # Aproveitando o calcular_media() como pedido na dica
        media = self.calcular_media()
        limite_faltas = 0.25 * total_aulas
        
        if media >= 7.0 and self.faltas <= limite_faltas:
            return True
        else:
            return False

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, nova_matricula):
        # Tira os espaços para ver se ficou vazio
        if nova_matricula.strip() == "":
            return False
        else:
            self.matricula = nova_matricula
            return True
            
    def maior_e_menor_nota(self):
        # Desafio extra
        if len(self.notas) == 0:
            return (None, None)
        else:
            return (min(self.notas), max(self.notas))

    def __str__(self):
        media = self.calcular_media()
        return f"{self.nome} ({self.matricula}) | Média {media:.2f} | Faltas {self.faltas}"