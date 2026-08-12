"""
Gabarito EXERCÍCIO 10 - Jogo de Adivinhação com Número Secreto

Raciocínio sênior
-----------------
O número secreto é uma constante (NUMERO_SECRETO) — em um jogo de
verdade, viria de random.randint; aqui o foco é o laço, não o sorteador.
O while True + break é deliberado: o loop "vive até acertar", sem
condição de saída artificial no topo. continue descarta palpites
inválidos sem contar tentativa — o erro do usuário não pune o jogo.
Alternativas descartadas: while com flag acertou (mais estado para
gerenciar; o break no ponto exato do acerto é mais direto).
"""

NUMERO_SECRETO: int = 42
LIMITE_INFERIOR: int = 1
LIMITE_SUPERIOR: int = 100

tentativas: int = 0

print(f"Tente adivinhar o número secreto ({LIMITE_INFERIOR}-{LIMITE_SUPERIOR}).")

while True:
    try:
        palpite: int = int(input("Palpite: "))
    except ValueError:
        print("Erro: digite um número inteiro válido.")
        continue

    tentativas += 1

    if palpite < NUMERO_SECRETO:
        print("Maior!")
    elif palpite > NUMERO_SECRETO:
        print("Menor!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break

# Onde você provavelmente divergiu:
# - usou uma flag (acertou = True/False) para controlar o while —
#   funciona, mas adiciona estado; o break direto é mais claro aqui
# - colocou tentativas += 1 antes do try — palpite inválido
#   contaria como tentativa (aqui o continue pula antes do +1)
# - transformou o número secreto em input() (o enunciado define como
#   constante fixa — o sorteio aleatório vem na aula de random)
# - não validou o palpite dentro do jogo (digitar "abc" derrubava o
#   programa inteiro)
