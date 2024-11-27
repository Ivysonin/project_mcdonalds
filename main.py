from combos import combos_economicos, combos_especiais, combos_mcnuggets, combos_tradicionais

# organização
print ("\n========== Bem vindo ao McDonald's ==========")
print ("\n          ======= Cardápio =======")

# Números usados para o cliente fazer suas escolhas mais para frente
print ("\n========== 1 ==========")
combos_economicos.McLanche_Feliz()
print ("\n========== 2 ==========")
combos_economicos.Combo_Simples()
print ("\n========== 3 ==========")
combos_especiais.McCrispy_Chicken_Deluxe()
print ("\n========== 4 ==========")
combos_especiais.McFish()
print ("\n========== 5 ==========")
combos_especiais.McVeggie()
print ("\n========== 6 ==========")
combos_mcnuggets.McNuggets_10_peças()
print ("\n========== 7 ==========")
combos_mcnuggets.McNuggets_15_peças()
print ("\n========== 8 ==========")
combos_tradicionais.big_Mac()
print ("\n========== 9 ==========")
combos_tradicionais.Quarterao_com_queijo()
print ("\n========== 10 ==========")
combos_tradicionais.McChicken()
print ("\n========== 11 ==========")
combos_tradicionais.Cheddar_McMelt()
print ("\n========== 12 ==========")
combos_tradicionais.Duplo_quarterao_com_queijo()

# Lista para adicionar as escolhas do cliente
lista_usuario = []

while True :
    escolha_usuario = input("\n=== Escolha um número referente ao lanche(Digite 0 para sair): ")

    if escolha_usuario == "0" :
        print ("\n===== Você encerrou os pedidos =====\n")
        break

    elif escolha_usuario == "1" :
        print("\n=== McLanche Feliz Adicionado ===\n")
        lista_usuario = lista_usuario.append(combos_economicos.McLanche_Feliz())
