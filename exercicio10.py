#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 10
#Removendo Duplicadas

def valores_unicos(lista):
    return list(set(lista))

def main():
    entrada = input("Digite os valores separados por espaço: ")
    lista_valores = [int(num) for num in entrada.split()]

    resultado = valores_unicos(lista_valores)

    print("Valores únicos:", resultado)
 
main()
    
