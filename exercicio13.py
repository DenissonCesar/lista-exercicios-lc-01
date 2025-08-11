#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 13
#Retornando o Menor Número

def menor_numero(lista):
    return min(lista)

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = menor_numero(lista_numeros)

    print("O menor número é:", resultado)
 
main()
    
