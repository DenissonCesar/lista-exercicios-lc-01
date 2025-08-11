#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 01
#Percorrendo uma lista 

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    imprimir_lista(lista_numeros)

main()
    
#numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

#imprimir_lista(numeros)