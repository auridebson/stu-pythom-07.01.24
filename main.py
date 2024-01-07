from dados import *


# BLOCO DE FUNÇÕES
def ln(x):
    print("-"*30)

def add_fruta():
    fruta = str(input("Digite o nome da fruta: "))
    frutas_tropicais.append(fruta)

def lista_frutas():
    for fruta in frutas_tropicais:
        print(fruta)

    

# FIM BLOCO DE FUNÇÕES

print("Programa para estudar listas")
ln(45)

while True:
    escolha = int(input("""Escolha a opção:
    1 - Adicionar fruta
    2 - Excluir fruta
    3 - Listar as frutas
    0 - Sair
    """))

    match escolha:
        case 1:
            add_fruta()
        case 2:
            print("Escolha 2 feita")
        case 3:
            lista_frutas()
        case 0:
            break
        case _:
            print("Opção inválida")
        
        