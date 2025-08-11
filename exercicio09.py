#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 09
#Contando Ocorrências

def contar_ocorrencias(lista, valor):
    return lista.count(valor)

def main():
    entrada_lista = input("Digite os valores da lista separados por espaço: ")
    lista_valores = [int(num) for num in entrada_lista.split()]

    valor_busca = int(input("Digite o valor que deseja contar: "))

    resultado = contar_ocorrencias(lista_valores, valor_busca)

    print(f"O valor {valor_busca} aparece {resultado} vez(es) na lista.")
 
main()
    
