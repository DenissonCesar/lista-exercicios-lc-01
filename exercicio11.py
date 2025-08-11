#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 11
#Verificando se a Lista está Vazia

def verificar_lista_vazia(lista):
    return len(lista) == 0

def main():
    entrada = input("Digite os valores separados por espaço (deixe vazio para testar lista vazia): ")
    if entrada.strip() == "":
        lista_valores = []
    else:
        lista_valores = [int(num) for num in entrada.split()]

    resultado = verificar_lista_vazia(lista_valores)

    print(resultado)
 
main()
    
