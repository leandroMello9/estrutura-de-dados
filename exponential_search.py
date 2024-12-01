def binary_seach(lista, item, inicio, fim):
   while inicio < fim:
       mid = int((inicio+fim)/2)
       if lista[mid] == item:
           return mid
       elif lista[mid] < item:
           inicio = mid + 1
       else:
           fim = mid
   return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return i
    return binary_seach(arr, target, i//2, min(i, n - 1))

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,10,32,33,34,35,36,37,38]
target = 5
result = exponential_search(arr, target)
print(f"Element found at index {result}")