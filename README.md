# Simulador de Dado em Python

Este repositório contém um script em Python que simula o lançamento de um dado. O usuário pode lançar o dado quantas vezes desejar e o programa exibirá o valor retornado pelo dado a cada lançamento.

## Funcionalidades

- Simulação do lançamento de um dado de 6 lados.
- Permite ao usuário lançar o dado repetidamente.
- Exibição do valor retornado pelo dado a cada lançamento.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter o Python 3.x instalado no seu sistema.
3. Execute o script.
4. O programa lançará o dado e exibirá o valor retornado.
5. O usuário pode optar por lançar o dado novamente ou encerrar o programa.

## Exemplo de Uso

```python
import random

def jogar_dado():
    return random.randint(1, 6) 

while True:
    print(f"O dado retornou o valor {jogar_dado()}.")
    jogar_novamente = input("Deseja jogar o dado novamente? (s/n) ")
    if jogar_novamente.lower() != "s":
        break

print("Fim do programa.")
