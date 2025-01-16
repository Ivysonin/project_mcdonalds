# Importando
from combos import combos_economicos, combos_especiais, combos_mcnuggets, combos_tradicionais
from combos.Listas import lista_mc

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

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
        print (f"{cor_vermelho}\n===== Você encerrou os pedidos ====={reset_cor}")
        break

    elif escolha_usuario == "1" :
        print(f"{cor_verde}\n=== McLanche Feliz Adicionado ==={reset_cor}")
        # Adicionando os ingredientes dos combos, a lista do usuario.
        lista_usuario.append(lista_mc.lista_McLanche_Feliz())
    
    elif escolha_usuario == "2" :
        print (f"{cor_verde}\n=== Combo Simples Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_Combo_Simples())

    elif escolha_usuario == "3" :
        print (f"{cor_verde}\n=== McCrispy Chicken Deluxe Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McCrispy_Chicken_Deluxe())

    elif escolha_usuario == "4" :
        print (f"{cor_verde}\n=== McFish Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McFish())

    elif escolha_usuario == "5" :
        print (f"{cor_verde}\n=== McVeggie Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McVeggie())

    elif escolha_usuario == "6" :
        print (f"{cor_verde}\n=== McNuggets_10_peças Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McNuggets_10_peças())

    elif escolha_usuario == "7" :
        print (f"{cor_verde}\n=== McNuggets_15_peças Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McNuggets_15_peças())

    elif escolha_usuario == "8" :
        print (f"{cor_verde}\n=== Big Mac Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_big_Mac())

    elif escolha_usuario == "9" :
        print (f"{cor_verde}\n=== Quarterão com Queijo Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_Quarterao_com_queijo())

    elif escolha_usuario == "10" :
        print (f"{cor_verde}\n=== McChicken Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_McChicken())

    elif escolha_usuario == "11" :
        print (f"{cor_verde}\n=== Cheddar McMelt Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_Cheddar_McMelt())
    
    elif escolha_usuario == "12" :
        print (f"{cor_verde}\n=== Duplo Quarterão com Queijo Adicionado{reset_cor}")
        lista_usuario.append(lista_mc.lista_Duplo_quarterao_com_queijo())

    # Se surgir algum erro
    else:
        print (f"{cor_vermelho}\n========== ERRO ==========\n{reset_cor}")

# Organização
print(f'\n{cor_verde}           Suas escolhas :\n{reset_cor}')

# Com a variavel 'combos' Entro dentro da lista 'lista_usuario' e pego tudo dentro,
# Fazendo o mesmo com 'i' para exibir todos os itens separadamente.
for combos in lista_usuario :
    for i in combos :
        print (f"- {i}")

# Finalizando.
print (f"{cor_vermelho}\n===== Pedidos finalizados ====={reset_cor}")
print (f"{cor_verde}\n===== Obrigado, Volte sempre =====\n{reset_cor}")