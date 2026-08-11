"""
Gabarito EXERCÍCIO 29 - Curto-circuito com or e fallback

Raciocínio sênior
-----------------
`input(...) or padrao` explora duas regras de uma vez: strings vazias
são Falsy, e o `or` só avalia o 2º operando quando o 1º é Falsy.
Resultado: padrão em UMA expressão, sem if. A parte 4 demonstra os
dois lados do curto-circuito — `and` devolve o 2º operando se o 1º
for True (o it continuaria: senão devolve o 1º), e `or` devolve o 2º
quando o 1º é Falsy. O ".strip()" antes do or evita o caso clássico:
usar o `or` com um espaço digitado, que é Truthy e "engoliria" o
padrão.

Alternativas descartadas: if + else para cada campo (o exercício é
justamente substituir isso); `.strip() or padrao` no mesmo input? —
aqui o strip está na leitura, e o or logo em seguida na atribuição.
"""

cidade: str = input("Cidade (padrão São Paulo): ").strip() or "São Paulo"
profissao: str = input("Profissão (padrão Estudante): ").strip() or "Estudante"

print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")

print(True and "chegou aqui")
print("" or "fallback")

# Onde você provavelmente divergiu:
# - escreveu if/else para o padrão (funciona, mas o or é a lição)
# - usou or depois de converter para algo sempre Truthy
#   (ex.: int(input()) or 0 — 0 é o único falsy, o padrão morre)
# - esqueceu o .strip(): " " (só espaço) é Truthy e vira a cidade
# - escreveu a parte 4 como comparação e, em vez de exibir o retorno
#   do operador em print
# - confundiu a ordem: `padrao or input` usaria o padrão SEMPRE
#   (padrão é Truthy, o or nem lê o input)