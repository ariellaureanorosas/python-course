"""
Gabarito EXERCÍCIO 08 - Calculadora de Tabuada com while

Raciocínio sênior
-----------------
Os limites da tabuada são constantes (INICIO_TABUADA, FIM_TABUADA)
para o laço expressar "de 1 até 10" sem números mágicos. O while
avança com contador += 1 — o mesmo padrão que você vai ver em
contadores de andar em jogos e paginação.
A formatação >2/>3 faz os alinhamentos do exemplo sem tabulação —
width fixo em vez de \t.
Alternativas descartadas: for range(1, 11) — o enunciado pede while.
"""

INICIO_TABUADA: int = 1
FIM_TABUADA: int = 10

try:
    numero: int = int(input("Digite um número: "))
except ValueError:
    print("Erro: digite um número inteiro válido.")
else:
    contador: int = INICIO_TABUADA
    while contador <= FIM_TABUADA:
        print(f"{contador:>2} x {numero:>2} = {contador * numero:>3}")
        contador += 1

# Onde você provavelmente divergiu:
# - usou for range() (mais natural, mas o enunciado exige while)
# - usou \t para alinhar (frágil: depende do terminal; aqui o >2/>3
#   garante o espaço com largura fixa)
# - não validou a entrada com try/except (o enunciado pede)
# - imprimiu sem incluir a validação; aqui o laço vive no else do try
