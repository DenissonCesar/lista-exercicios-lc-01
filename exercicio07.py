#EXERCÍCIO LABORATÓRIO DE COMPUTACAO - QUESTAO 07
#Extraindo Nomes de Objetos 

def extrair_nomes(lista_objetos):
    return [obj['nome'] for obj in lista_objetos if 'nome' in obj]

def main():
    quantidade = int(input("Digite a quantidade de objetos: "))
    lista_objetos = []

    for i in range(quantidade):
        nome = input(f"Digite o nome do objeto {i+1}: ")
        lista_objetos.append({'nome': nome})

    resultado = extrair_nomes(lista_objetos)

    print("Lista de nomes extraídos:", resultado)
 
main()
    
