"""
EXERCÍCIO 28 - Escopo Global

Tópicos: escopo global/local, global, anotação 23

No topo do arquivo existe a variável global `CONTADOR = 0`.
Implemente quatro funções:

1. `incrementar() -> int`
   - Declara `global CONTADOR`, soma 1 e devolve o novo valor.
     Cada chamada aumenta de verdade o valor global.

2. `zerar() -> None`
   - Declara `global CONTADOR` e o redefine como 0.

3. `consultar() -> int`
   - Apenas LÊ o CONTADOR global — comentário: ler global é livre,
     não precisa da palavra `global`.

4. `somar_local(a: int, b: int) -> int`
   - Soma usando apenas variáveis locais — deve funcionar sem
     tocar em nenhum nome global.

Comportamento esperado (começando com CONTADOR = 0):
    incrementar()   # 1
    incrementar()   # 2
    consultar()     # 2
    zerar()         # (nada — retorna None)
    consultar()     # 0

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

CONTADOR = 0


def incrementar() -> int:
    ...


def zerar() -> None:
    ...


def consultar() -> int:
    ...


def somar_local(a: int, b: int) -> int:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(incrementar())
    print(incrementar())
    print(consultar())
    zerar()
    print(consultar())