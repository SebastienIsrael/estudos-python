from random import choice


def binary_search(arr: list[int], target: int) -> int:
    """Realiza a busca binária em uma lista ordenada.

    Retorna o índice do target se encontrado, ou -1 caso contrário.
    """
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = arr[meio]

        if chute == target:
            return meio

        if chute < target:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


# --- Teste do algoritmo ---
lista_numeros = list(range(1, 101))
numero_procurado = choice(lista_numeros)

resultado_indice = binary_search(lista_numeros, numero_procurado)

print(f"O número {numero_procurado} está no índice: {resultado_indice}")