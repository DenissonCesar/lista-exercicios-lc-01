#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 05
#Encontrando os Números Ímpares

def numeros_pares(lista):
    return [num for num in lista if num % 2 == 1]


def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = numeros_pares(lista_numeros)

    if resultado is not None: 
        print("Os números ímpares são: ", resultado)
    else:
        print("Não há números ímpares")
 
main()
    
