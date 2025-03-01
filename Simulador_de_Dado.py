import random

def jogar_dado():
    return random.randint(1, 6) 

while True:
    print(f"O dado retornou o valor {jogar_dado()}.")
    jogar_novamente = input("Deseja jogar o dado novamente? (s/n) ")
    if jogar_novamente.lower() != "s":
        break

print("Fim do programa.")