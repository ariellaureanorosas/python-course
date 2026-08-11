"""
EXERCÍCIO 24 - Tratamento de Erros Completo (try/except/else/finally)

Tópicos: try, except, else, finally, exceções específicas

Implemente três funções:

1. `converter_numero(texto: str) -> int | None`
   - Tenta int(texto); devolve o int ou None se ValueError.
     O except precisa ser ESPECÍFICO (ValueError), não genérico.

2. `divisao_segura(a: float, b: float) -> str`
   - try com a divisão; except ZeroDivisionError devolve
     "divisão por zero"; else devolve f"{resultado:.2f}". O else
     só roda quando NÃO houve exceção — ponha o "sucesso" nele.

3. `analisar_numero(texto: str) -> tuple`
   - Converte com try (sucesso=True) e trata ValueError com valor 0
     e sucesso=False; usa FINALLY para imprimir
     "validacao concluida" — o finally roda SEMPRE, com erro ou não.

Comportamento esperado:
    converter_numero("42")     # 42
    converter_numero("abc")    # None
    divisao_segura(10, 2)      # '5.00'
    divisao_segura(10, 0)      # 'divisão por zero'
    analisar_numero("42")
    # imprime "validacao concluida" e retorna (42, True)

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def converter_numero(texto: str) -> int | None:
    ...


def divisao_segura(a: float, b: float) -> str:
    ...


def analisar_numero(texto: str) -> tuple:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(converter_numero("42"))
    print(converter_numero("abc"))
    print(divisao_segura(10, 2))
    print(divisao_segura(10, 0))
    print(analisar_numero("42"))