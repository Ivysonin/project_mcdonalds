from combos import combos_economicos, combos_especiais, combos_mcnuggets, combos_tradicionais
from combos.Listas import lista_mc

# organização
print ("\n========== Bem vindo ao McDonald's ==========")
print ("\n          ======= Cardápio =======")

# Números usados para o cliente fazer suas escolhas mais para frente
print ("\n           [ 1 ] \n")
combos_economicos.McLanche_Feliz()
print ("\n           [ 2 ] \n")
combos_economicos.Combo_Simples()
print ("\n           [ 3 ] \n")
combos_especiais.McCrispy_Chicken_Deluxe()
print ("\n           [ 4 ] \n")
combos_especiais.McFish()
print ("\n           [ 5 ] \n")
combos_especiais.McVeggie()
print ("\n           [ 6 ] \n")
combos_mcnuggets.McNuggets_10_peças()
print ("\n           [ 7 ] \n")
combos_mcnuggets.McNuggets_15_peças()
print ("\n           [ 8 ] \n")
combos_tradicionais.big_Mac()
print ("\n           [ 9 ] \n")
combos_tradicionais.Quarterao_com_queijo()
print ("\n           [ 10 ] \n")
combos_tradicionais.McChicken()
print ("\n           [ 11 ] \n")
combos_tradicionais.Cheddar_McMelt()
print ("\n           [ 12 ] \n")
combos_tradicionais.Duplo_quarterao_com_queijo()

# Lista para adicionar as escolhas do cliente
lista_usuario = []

while True :
    escolha_usuario = input("\n=== Escolha um número referente ao lanche(Digite 0 para sair): ")

    if escolha_usuario == "0" :
        print ("\n===== Você encerrou os pedidos =====\n           Suas escolhas :\n")
        break

    elif escolha_usuario == "1" :
        print("\n=== McLanche Feliz Adicionado ===")
        # Adicionando os ingredientes dos combos, a lista do usuario.
        lista_usuario.append(lista_mc.lista_McLanche_Feliz())