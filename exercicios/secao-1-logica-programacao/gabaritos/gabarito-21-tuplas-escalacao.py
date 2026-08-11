"""
Gabarito EXERCÍCIO 21 - Tuplas: Dados Imutáveis

Raciocínio sênior
-----------------
A escalação é o dado certo para tupla por natureza: uma partida não
pode trocar jogadores a meio do jogo. Com a tupla, o código que
tentaria "corrigir" um defeito acaba sendo capturado pelo TypeError
no lugar certo. Os dois try/except são direcionados às DUAS únicas
falhas possíveis: ValueError (nome fora da escalação) e TypeError
(atribuição em tupla). O desempacotamento com *restantes devolve uma
lista automaticamente — o tamanho do time não precisa ser conhecido.

Alternativas descartadas: usar lista — funcionaria, mas eliminaria a
lição de imutabilidade e permitiria mudanças acidentais.
"""

ESCALACAO: tuple[str, ...] = ("João", "Maria", "Carlos", "Ana", "Pedro")

jogador: str = input("Jogador para buscar: ")
try:
    posicao: int = ESCALACAO.index(jogador)
    print(f"{jogador} está na posição {posicao}.")
except ValueError:
    print(f"{jogador} não está na escalação.")

try:
    ESCALACAO[1] = "Novato"
except TypeError:
    print("A escalação é imutável!")

titular1, titular2, *restantes = ESCALACAO
print(f"Principais: {titular1} e {titular2}")
print(f"Reservas: {restantes}")

# Onde você provavelmente divergiu:
# - usou uma lista em vez de tupla (perde a proteção que o enunciado pede)
# - usou `except:` genérico ou capturou só o TypeError, deixando o
#   ValueError "escapar" quando o nome não existe
# - tentou "alterar a tupla" com append (AttributeError, não TypeError)
# - desempacotou os 3 primeiros em vez de 1º, 2º e o resto com *
# - esqueceu de formatar a saída idêntica ao enunciado ("posição 1.")