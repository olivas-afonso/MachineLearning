import random

def dividir_matriz_por_percentagem_linhas(matriz, percentagem, seed):
    # Define a seed para a aleatoriedade ser reprodutível
    random.seed(seed)
    
    # Calcula quantas linhas terão na matriz menor
    n_linhas_menor_matriz = int(len(matriz) * percentagem)
    
    # Seleciona aleatoriamente as linhas para a matriz menor
    linhas_selecionadas = random.sample(range(len(matriz)), n_linhas_menor_matriz)
    
    # Cria as matrizes maior e menor
    matriz_menor = [matriz[i] for i in linhas_selecionadas]
    matriz_maior = [matriz[i] for i in range(len(matriz)) if i not in linhas_selecionadas]
    
    return matriz_maior, matriz_menor

# Exemplo de matriz original com 200x200 elementos
matriz_original = [[(i * 200 + j + 1) for j in range(200)] for i in range(200)]

# Percentagem e seed
percentagem = 0.2  # 20% das linhas para a matriz menor
seed = 42  # Seed fixa para garantir resultados reprodutíveis

# Divide a matriz original
matriz_maior, matriz_menor = dividir_matriz_por_percentagem_linhas(matriz_original, percentagem, seed)

# Exibe as matrizes (limitando o print para as primeiras linhas, devido ao tamanho)
print("Matriz Maior (primeiras 5 linhas):")
for linha in matriz_maior[:5]:
    print(linha)

print("\nMatriz Menor (todas as linhas):")
for linha in matriz_menor[:5]:
    print(linha)
