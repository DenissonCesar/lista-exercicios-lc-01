#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 02
#Percorrendo uma lista 

def maior_numero(lista):
    return max(lista)

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    print("O maior número da lista é o número: ", maior_numero(lista_numeros))

main()
    
