#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 14
#Calculando Média

def media_lista(lista):
    if len(lista) == 0:
        return 0  # Evitar divisão por zero
    return sum(lista) / len(lista)

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = media_lista(lista_numeros)

    print("A média dos números é:", resultado)
 
main()
    
