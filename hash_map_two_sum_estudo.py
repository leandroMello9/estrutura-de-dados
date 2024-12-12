def two_sum(lista, item):
    conjunto_numeros = {}
    for i, numero in enumerate(lista):
        if item in conjunto_numeros:
            return [i - 1]
        if item - numero in conjunto_numeros:
            return [i, conjunto_numeros[item - numero]]
        conjunto_numeros[numero] = i

print(two_sum([1,2,3,4,5], 5))