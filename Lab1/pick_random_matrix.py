import random

def dividir_matriz_por_percentagem(matriz, percentagem, seed):
    # Define a seed para a aleatoriedade ser reprodutível
    random.seed(seed)
    
    # Obtém o número total de elementos na matriz original
    elementos_totais = sum(len(linha) for linha in matriz)
    
    # Calcula quantos elementos serão colocados na matriz menor
    n_elementos_menor_matriz = int(elementos_totais * percentagem)
    
    # Lista plana com todos os elementos da matriz original
    todos_elementos = [valor for linha in matriz for valor in linha]
    
    # Seleciona aleatoriamente os elementos para a matriz menor
    elementos_menor_matriz = random.sample(todos_elementos, n_elementos_menor_matriz)
    
    # Cria a matriz maior e menor
    matriz_menor = []
    matriz_maior = []
    
    for linha in matriz:
        nova_linha_menor = []
        nova_linha_maior = []
        
        for valor in linha:
            if valor in elementos_menor_matriz:
                nova_linha_menor.append(valor)
                elementos_menor_matriz.remove(valor)  # Remove o elemento para evitar duplicações
            else:
                nova_linha_maior.append(valor)
        
        matriz_menor.append(nova_linha_menor)
        matriz_maior.append(nova_linha_maior)
    
    return matriz_maior, matriz_menor

# Exemplo de matriz original
matriz_original = [
    [1, 2, 3, 12],
    [4, 5, 6, 11],
    [7, 8, 9,10]
]

# Percentagem e seed
percentagem = 0.2  # 20% para a matriz menor
seed = 42  # Seed fixa para garantir resultados reprodutíveis

# Divide a matriz original
matriz_maior, matriz_menor = dividir_matriz_por_percentagem(matriz_original, percentagem, seed)

# Exibe as matrizes
print("Matriz Maior:")
for linha in matriz_maior:
    print(linha)

print("\nMatriz Menor:")
for linha in matriz_menor:
    print(linha)
