# Implemente um algoritmo em Python que calcule o fatorial de um número
# utilizando recursão. Após isso, determine a complexidade assintótica O(n)
# do algoritmo, incluindo a explicação do raciocínio. O objetivo é avaliar
# como o tempo de execução cresce em função do tamanho da entrada n.

# Instruções:

# - Escreva um programa em Python que:
# - Leia um número inteiro n.
# - Calcule o fatorial de n recursivamente.
# - Inclua comentários explicando cada parte do código.
# - Meça o tempo de execução do algoritmo para diferentes valores de n: 10, 100, 500, e 1000.
# - Submeta o código com os resultados do tempo de execução e uma breve explicação da análise de complexidade.



import time
import sys

#n=1000
sys.setrecursionlimit(2000)

def calcular_fatorial(n):
    if n <= 1:
        return 1
    
    #Passo recursivo n * fatorial(n - 1)
    return n * calcular_fatorial(n - 1)

def medir_execucao(valores_n):

    print(f"{'n':>10} | {'Tempo/s: ':>20}")
    print("_" * 35)
    
    for n in valores_n:
        inicio = time.perf_counter()
        resultado = calcular_fatorial(n)
        fim = time.perf_counter()
        
        tempo_total = fim - inicio
        print(f"{n:>10} | {tempo_total:>20.8f}")

if __name__ == "__main__":
    VALORES_TESTE = [10, 100, 500, 1000]
    
    medir_execucao(VALORES_TESTE)