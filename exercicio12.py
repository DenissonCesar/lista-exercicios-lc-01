#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 12
#Juntando Duas Listas 

def concatenar_listas(lista1, lista2):
    return lista1 + lista2

def main():
    entrada1 = input("Digite os valores da primeira lista separados por espaço: ")
    lista1 = [int(num) for num in entrada1.split()]

    entrada2 = input("Digite os valores da segunda lista separados por espaço: ")
    lista2 = [int(num) for num in entrada2.split()]

    resultado = concatenar_listas(lista1, lista2)

    print("Lista concatenada:", resultado)
 
main()
    
