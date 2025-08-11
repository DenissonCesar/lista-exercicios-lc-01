#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 03
#Segundo maior

def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    return lista_unica[1] if len(lista_unica) > 1 else None 

def main():
    entrada = input("Digite os números separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]

    resultado = segundo_maior(lista_numeros)

    if resultado is not None: 
        print("O segundo maior número é: ", resultado)
    else:
        print("Não há segundo número maior")

        
main()
    
