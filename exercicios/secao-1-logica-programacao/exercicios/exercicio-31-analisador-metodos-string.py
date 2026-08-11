"""
EXERCÍCIO 31 — Analisador de texto com métodos de string

Tópicos: upper/lower, count, find, zfill, projeto "letra que mais aparece"

Crie um analisador de uma FRASE digitada:

  1. Exiba a frase em maiúsculas e em minúsculas.
  2. Exiba quantas vezes a letra "a" aparece (maiúscula OU minúscula),
     usando .count() depois de normalizar com .lower().
  3. Exiba a posição da primeira ocorrência da palavra "python" com
     .find() — ou "A palavra 'python' não aparece." se ela não existir.
  4. Exiba qual é a LETRA mais frequente da frase, ignorando espaços
     e maiúsculas/minúsculas — o projeto da aula 42 (use .count()).
  5. Receba um número de pedido (int) e exiba-o com 5 dígitos usando
     .zfill(5) — ex.: 7 vira "00007".

Exemplo de saída esperada (frase: "Banana é Python", pedido 7):
MAIÚSCULAS: BANANA É PYTHON
minúsculas: banana é python
Letras 'a': 3
'python' aparece na posição 9.
Letra mais frequente: 'a' (3x)
Pedido: 00007

Dica: use uma frase_normalizada = frase.lower() para contar e buscar
sem se preocupar com maiúsculas, mas exiba a original.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========