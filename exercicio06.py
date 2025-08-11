#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 06
#Buscando um Número

def buscar_numero(numero, lista):
    return numero in lista


def main():
    entrada_lista = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada_lista.split()]

    entrada_numero = int(input("Digite o número que queira buscar: "))

    resultado = buscar_numero(entrada_numero, lista_numeros)

    print(resultado)
 
main()
    
