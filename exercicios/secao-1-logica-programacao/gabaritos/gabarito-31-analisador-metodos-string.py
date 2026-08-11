"""
Gabarito EXERCÍCIO 31 - Analisador de texto com métodos de string

Raciocínio sênior
-----------------
A normalização em frase_normalizada = frase.lower() centraliza o
"padrão de comparação" — contar 'a' e achar 'python' ficam imunes a
maiúsculas sem duplicar chamadas .lower(). O projeto da letra mais
frequente percorre a string NORMALIZADA para que 'A' e 'a' contem
juntas, e o .count() (que é O(n) por chamada) roda uma vez por letra
— para strings curtas é aceitável; para textos grandes, um dict de
contadores (nota da Seção 2) é o jeito certo. O .find() devolve -1
quando não existe: a checagem `!= -1` é o ponto onde muita gente
esquece do caso de borda. O .zfill(5) completa com zeros à esquerda
— clássico de IDs de pedido.

Alternativas descartadas: .count() por letra com três versões
(maiúscula, minúscula, acentuada) — a normalização cobre tudo;
escanear com str.maketrans (avançado e desnecessário aqui).
"""

frase: str = input("Frase: ").strip()
frase_normalizada: str = frase.lower()

print(f"MAIÚSCULAS: {frase.upper()}")
print(f"minúsculas: {frase.lower()}")

print(f"Letras 'a': {frase_normalizada.count('a')}")

posicao_python: int = frase_normalizada.find("python")
if posicao_python != -1:
    print(f"'python' aparece na posição {posicao_python}.")
else:
    print("A palavra 'python' não aparece.")

letra_mais_frequente: str = ""
maior_quantidade: int = 0
for letra in frase_normalizada:
    if letra == " ":
        continue
    quantidade: int = frase_normalizada.count(letra)
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        letra_mais_frequente = letra
print(f"Letra mais frequente: '{letra_mais_frequente}' ({maior_quantidade}x)")

pedido: int = int(input("Número do pedido: "))
print(f"Pedido: {str(pedido).zfill(5)}")

# Onde você provavelmente divergiu:
# - contou 'a' sem normalizar (frase original.count('a') ignora os 'A')
# - usou `if posicao_python:` — -1 é Truthy! A checagem certa é `!= -1`
# - no projeto da letra, comparou letra a letra com a original (case
#   sensitive) ou contou o espaço como letra
# - usou {pedido:05d} no f-string (funciona só para números; o
#   enunciado pede o método .zfill)
# - esqueceu de exibir a frase em minúsculas (só normalizou por dentro)