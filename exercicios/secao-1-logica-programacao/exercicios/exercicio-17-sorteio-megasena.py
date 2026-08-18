"""
EXERCÍCIO 17 — Sorteio da Mega-Sena com random

Use random.randint() para sortear 6 números aleatórios entre 1 e 60.
Regras:
    - Os números NÃO podem se repetir.
    - Use um laço while para garantir que cada novo número é único
      (use o operador in para verificar se já existe na lista).
    - Ao final, ordene os números com sorted() e exiba.

Exemplo de saída:
    Números sorteados: [05, 12, 23, 34, 45, 58]

Dica: comece com uma lista vazia e vá adicionando números com append()
      somente se o número ainda não estiver na lista.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
import random

QUANTIDADE_SORTEIO: int = 6
numeros_sorteados: list[int] = []

while len(numeros_sorteados) < QUANTIDADE_SORTEIO:
    numero_aleatorio: int = random.randint(1, 60)
    if numero_aleatorio not in numeros_sorteados:
        numeros_sorteados.append(numero_aleatorio)

numeros_formatados = sorted([f"{numero:02d}" for numero in numeros_sorteados])

print(f"Resultado: {', '.join(numeros_formatados)}")
