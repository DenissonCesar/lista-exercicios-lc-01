#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 04
#Números Pares

def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]


def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = numeros_pares(lista_numeros)

    if resultado is not None: 
        print("Os números pares são: ", resultado)
    else:
        print("Não há números pares")
 
main()
    
