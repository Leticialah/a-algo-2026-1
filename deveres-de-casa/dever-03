def eh_palindromo(arr):
    # Caso base: 0 ou 1 elemento
    if len(arr) <= 1:
        return True
    
    # Se primeiro e último forem diferentes
    if arr[0] != arr[-1]:
        return False
    
    # Chamada recursiva
    return eh_palindromo(arr[1:-1])


# Testes
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print("array1:", eh_palindromo(array1))
print("array2:", eh_palindromo(array2))
print("array3:", eh_palindromo(array3))
print("array4:", eh_palindromo(array4))
