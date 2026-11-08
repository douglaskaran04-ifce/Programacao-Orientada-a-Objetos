from televisao import Televisao

# Criando pelo menos 3 televisores
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

lista_tvs = [tv1, tv2, tv3]

# Ligando algumas e deixando a tv3 desligada
tv1.ligar()
tv2.ligar()

# Modificando usando os metodos agora (e nao direto nos atributos)
tv1.trocar_canal(5)
tv1.aumentar_volume(15)

tv2.trocar_canal(12)
tv2.aumentar_volume(60)

# Testando as operacoes invalidas (a classe devolve False)
resultado1 = tv3.trocar_canal(10)
if resultado1 == False:
    print("Trocar canal com a TV desligada: False")

resultado2 = tv1.ligar()
if resultado2 == False:
    print("Ligar de novo a TV 1: False")

resultado3 = tv2.trocar_canal(150)
if resultado3 == False:
    print("Canal 150 na TV 2: False")

print() # Só para pular linha e ficar igual ao exemplo

# Percorrendo a lista com o for e imprimindo tudo
for tv in lista_tvs:
    print(tv) # Isso chama o __str__ que criamos