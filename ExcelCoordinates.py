alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",  "Z"]

def indexLetra (letra):
    for index, letraAlfabeto in enumerate(alfabeto):
        if(letra == letraAlfabeto):
            return index + 1 

def conversor(lista):
    soma = 0
    comprimento = len(lista)
    if(comprimento == 1):
        return indexLetra(lista[0]) - 1

    for index, letra in enumerate(lista):
        exponenciacao = 26**(comprimento - 1 - index)
        soma += indexLetra(letra) * exponenciacao 
    return soma - 1

while (True):
    coordenadas=input("Indique as coordenadas:")
    if(coordenadas == "sair"):
        print("Fim do Programa")
        break
    
    separar=coordenadas.split(' ')
    coluna=separar[0]
    linha=int(separar[1])
    dividida = list(coluna)
    conversor(dividida)

    print("Linha:", linha -1)
    print("Coluna:", conversor(dividida))





