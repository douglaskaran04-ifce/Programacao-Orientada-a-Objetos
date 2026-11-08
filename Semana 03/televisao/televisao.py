class Televisao:
    # Metodo Construtor da Aula 02 (com atributos extras para o desafio)
    def __init__(self, marca, polegadas):
        self.marca = marca
        self.polegadas = polegadas
        self.ligada = False
        self.canal = 1
        self.volume = 10
        self.canais_assistidos = [] # Desafio extra para voltar canal

    def ligar(self):
        if self.ligada == False:
            self.ligada = True
            return True
        else:
            return False

    def desligar(self):
        if self.ligada == True:
            self.ligada = False
            return True
        else:
            return False

    def aumentar_volume(self, quantidade):
        # Nao faz nada se a tv estiver desligada ou quantidade for invalida
        if not self.ligada or quantidade <= 0:
            return False
        
        # Se ja ta no maximo, nao muda
        if self.volume == 100:
            return False
            
        self.volume = self.volume + quantidade
        
        # Limitando em 100 usando max/min ou if (escolhi if)
        if self.volume > 100:
            self.volume = 100
        
        return True

    def diminuir_volume(self, quantidade):
        if not self.ligada or quantidade <= 0:
            return False
            
        if self.volume == 0:
            return False
            
        self.volume = self.volume - quantidade
        
        if self.volume < 0:
            self.volume = 0
            
        return True

    def trocar_canal(self, canal):
        if not self.ligada:
            return False
            
        if canal >= 1 and canal <= 100:
            # Salva o canal de agora antes de mudar pro novo (Desafio)
            self.canais_assistidos.append(self.canal)
            self.canal = canal
            return True
        else:
            return False

    def voltar_canal(self):
        # Desafio extra: voltar o canal
        if not self.ligada:
            return False
            
        if len(self.canais_assistidos) > 0:
            # tira o ultimo da lista e coloca como canal atual
            canal_anterior = self.canais_assistidos.pop()
            self.canal = canal_anterior
            return True
        return False

    def __str__(self):
        # O __str__ so devolve texto, nao usa print!
        if self.ligada:
            return f'{self.marca} {self.polegadas}" | Ligada | Canal {self.canal} | Volume {self.volume}'
        else:
            return f'{self.marca} {self.polegadas}" | Desligada'