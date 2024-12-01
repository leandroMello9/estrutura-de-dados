def binary_seach(lista, item):
    inicio = 0
    fim = len(lista) - 1
    passos = 0
    while inicio <= fim:
        passos = passos + 1
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            print("Steps: ", passos)
            return meio
        if chute < item:
            inicio = meio + 1
        else:
            fim = meio
    return -1
minha_lista = [1,3,5,7,8,9,10,11]
#binary_seach(minha_lista, 5)
binary_seach(minha_lista, 9)
