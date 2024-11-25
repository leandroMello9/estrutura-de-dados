def binary_seach(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None
minha_lista = [1,3,5,7,9]
print(binary_seach(minha_lista, 5))
print(binary_seach(minha_lista, 9))
