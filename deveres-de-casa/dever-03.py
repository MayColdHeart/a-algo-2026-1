# Implemente o código recursivo para verificar se um array é palíndromo.

# Ex:
# array1 = [0, 1, 2, 3, 2, 1, 0] -> É palíndromo
# array2 = ["a", "b", "b", "a"] -> É palíndromo
# array3 = ["a", "b", "c", "b", "a"] -> É palíndromo
# array4 = ["a", "b", "c", "f", "b", "a"] -> Não é palíndromo

def verificar_palindromo(lista):
    #Caso base
    if len(lista) <= 1:
        return True
    if lista[0] != lista[-1]:
        return False

    #lista[1:-1] cria uma nova fatia (slice) do array
    return verificar_palindromo(lista[1:-1])


def testar():
    testes = [
        [0, 1, 2, 3, 2, 1, 0],
        ["a", "b", "b", "a"],
        ["a", "b", "c", "b", "a"],
        ["a", "b", "c", "f", "b", "a"]]

    for i, array in enumerate(testes, 1):
        resultado = verificar_palindromo(array)
        status = "é palindromo" if resultado else "Não é palíndromo"
        print(f"array{i} = {array} -> {status}")


if __name__ == "__main__":
    testar()