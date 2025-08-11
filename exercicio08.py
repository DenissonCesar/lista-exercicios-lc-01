#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 08
#Somando os Valores da Lista

def soma_lista(lista):
    return sum(lista)

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = soma_lista(lista_numeros)

    print("A soma dos números é:", resultado)
 
main()
    
