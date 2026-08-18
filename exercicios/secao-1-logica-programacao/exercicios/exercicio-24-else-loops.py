"""
EXERCÍCIO 24 — else de loops (while/else e for/else)

Tópicos: while/else, for/else, break

Parte 1 — Senha: o usuário tem 3 tentativas para acertar a senha
"python123". Se acertar antes, imprima "Acesso liberado." e saia
com break. Se as tentativas acabarem sem acerto, o else do while
deve imprimir "Acesso bloqueado.".

Parte 2 — Busca: com a lista ["ana", "carlos", "maria", "joao"],
receba um nome e procure na lista usando for + break. Se encontrar,
exiba "Encontrado na posição X." (X é o índice). Se NÃO encontrar,
o else do for deve exibir "Nome não cadastrado.".

Exemplo de saída esperada (senha errada 3 vezes, busca por "bia"):
Senha: 123
Senha: abc
Senha: errada
Acesso bloqueado.
Nome para buscar: bia
Nome não cadastrado.

Dica: o else de um loop executa apenas quando o loop termina SEM
break — é o "não encontrei" que você não precisa de flag.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========
SENHA = "python123"
tentativas = 0

while tentativas < 3:
    input_senha = input("Digite a senha: ")
    if input_senha == SENHA:
        print("Acesso Concedido")
        break
    else:
        print("Acesso Negado")
    tentativas += 1
else:
    print("Acesso bloqueado")


NOMES: list[str] = ["ana", "carlos", "maria", "joao"]
input_nomes = input("Digite o nome que quer procurar: ").strip().lower()
for posicao, nome in enumerate(NOMES):
    if input_nomes == nome:
        print(f"Nome encontrado na posição {posicao}")
        break
else:
    print("nome não encontrado")
