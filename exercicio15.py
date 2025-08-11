#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 15
#Invertendo a Lista 

def inverter_lista(lista):
    return lista[::-1]

def main():
    entrada = input("Digite os elementos da lista separados por espaço: ")
    lista_elementos = [int(x) for x in entrada.split()]

    resultado = inverter_lista(lista_elementos)

    print("Lista invertida:", resultado)
 
main()
    
