"""
Gabarito EXERCÍCIO 24 - else de loops (while/else e for/else)

Raciocínio sênior
-----------------
O else de loop é o "eu saí sem interrupção" embutido: o while/else
evita a flag `avanco = False` (colocá-la em cada except exige avisar
o loop externo); o for/else evita o `encontrado = False` + if final.
Ambos substituem a dupla "flag + checagem pós-loop" — menos estado
mutável, menos chance de esquecer de setar. A busca normaliza o nome
digitado (.strip().lower()) para comparar com a lista já minúscula:
normalizar a ENTRADA, não a lista, evita reescrever os dados.

Alternativas descartadas: flag booleana (funciona, mas é exatamente
o boilerplate que o else de loop existe para eliminar); procurar com
.upper() direto (frágil se a lista tiver acentos).
"""

SENHA_CORRETA: str = "python123"
tentativas: int = 0

while tentativas < 3:
    senha: str = input("Senha: ")
    if senha == SENHA_CORRETA:
        print("Acesso liberado.")
        break
    tentativas += 1
else:
    print("Acesso bloqueado.")

NOMES: list[str] = ["ana", "carlos", "maria", "joao"]
procurado: str = input("Nome para buscar: ").strip().lower()

for posicao, nome_atual in enumerate(NOMES):
    if nome_atual == procurado:
        print(f"Encontrado na posição {posicao}.")
        break
else:
    print("Nome não cadastrado.")

# Onde você provavelmente divergiu:
# - usou flags (encontrado = False + if pós-loop) — funciona, mas é
#   o boilerplate que o else de loop substitui
# - confundiu o else de loop com o else de if: no loop, só roda se
#   NÃO houve break
# - comparou o nome digitado sem .lower() — "Ana" não achava "ana"
# - esqueceu o else na senha e imprimiu "Acesso bloqueado" sempre
#   (mesmo após acerto) ou o print do break nunca era atingido
# - usou while True + contador manual de tentativas sem incremento
#   em um dos caminhos (loop infinito ou bloqueio prematuro)