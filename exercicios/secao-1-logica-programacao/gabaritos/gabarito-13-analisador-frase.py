"""
GABARITO — EXERCÍCIO 13 — Analisador de Frase com split/join

Recebe uma frase, conta as palavras com split() e as junta com hífen
usando join().
"""

frase: str = input("Digite uma frase: ")

palavras: list = frase.split()
quantidade: int = len(palavras)

frase_hifen: str = "-".join(palavras)

print(f"Palavras: {quantidade}")
print(f"Frase com hífen: \"{frase_hifen}\"")
