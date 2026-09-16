"""
Gabarito EXERCÍCIO 27 - None e o operador is

Raciocínio sênior
-----------------
None é o sentinela do "dado ausente": deixar o telefone como string
vazia misturaria "não informado" com "informado mas em branco". A
comparação é `telefone is None` — identidade, não igualdade: None é
um único objeto canônico, então `is` é correto E mais rápido. O
ternário `telefone_digitado if telefone_digitado else None` lê
como frase: dado existe → mantém, caso contrário None. A flag
contato_completo deriva de is not None — um booleano nomeado usado
uma vez, em vez de comparar de novo nos dois pontos de decisão.

Alternativas descartadas: `telefone == None` (funciona, mas quebra a
convenção; `is` é o padrão aceito); manter "" e comparar `if telefone`
(Truthy/Falsy funciona, mas o None torna o estado explícito).
"""

nome: str = input("Nome: ").strip()
telefone_digitado: str = input("Telefone (opcional): ").strip()
telefone: str | None = telefone_digitado if telefone_digitado else None

print(f"Nome: {nome}")

if telefone is None:
    print("Telefone: não informado")
else:
    print(f"Telefone: {telefone}")

contato_completo: bool = telefone is not None
if contato_completo:
    print("Cadastro completo.")
else:
    print("Complete o cadastro.")

# Onde você provavelmente divergiu:
# - usou `telefone == None` em vez de `telefone is None`
# - deixou " " (espaço) passar: o .strip() no input garante que
#   " " vire "" — sem strip, um espaço em branco viraria um telefone
# - tratou None como string, exibindo "Telefone: None"
# - inverteu a lógica do ternário ou usou if/else duplicado para a flag
# - reutilizou `if contato_completo:` checando `telefone is not None`
#   de novo em vez da variável nomeada
