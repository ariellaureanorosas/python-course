"""
EXERCÍCIO 20 - Positional-Only e Keyword-Only

Tópicos: Positional-Only Parameters (/), Keyword-Only Arguments (*)
Aula: 128

Crie funções que utilizam os parâmetros / e * para restringir
como os argumentos podem ser passados.

1. Função `calcular(valor: float, /, taxa: float, *, desconto: float = 0) -> float`
   - valor: positional-only (não pode ser passado como keyword)
   - taxa: positional ou keyword
   - desconto: keyword-only (não pode ser passado posicionalmente)
   - Retorna: valor * taxa - desconto

2. Função `criar_usuario(
       nome: str,
       /,
       email: str,
       *,
       idade: int = 0,
       ativo: bool = True,
   ) -> dict`
   - nome: positional-only
   - email: positional ou keyword
   - idade: keyword-only (default 0)
   - ativo: keyword-only (default True)
   - Retorna dicionário com todos os dados

3. Função `registrar_venda(
       *,
       produto: str,
       quantidade: int,
       preco_unitario: float,
   ) -> dict`
   - TODOS os parâmetros estão DEPOIS de `*` — portanto TODOS são
     keyword-only (não há nenhum parâmetro posicional)
   - Retorna dicionário com produto, quantidade, preco_unitario, total
   - total = quantidade * preco_unitario

Desafio extra (opcional dentro da função 3):
   Não há argumentos posicionais nesta assinatura: chamar
   registrar_venda("Caneta", 10, 1.5) levanta TypeError. A única
   forma válida é passando os argumentos por nome:
   registrar_venda(produto="Caneta", quantidade=10, preco_unitario=1.50)
"""


def calcular(
    valor: float,
    /,
    taxa: float,
    *,
    desconto: float = 0,
) -> float:
    ...


def criar_usuario(
    nome: str,
    /,
    email: str,
    *,
    idade: int = 0,
    ativo: bool = True,
) -> dict:
    ...


def registrar_venda(
    *,
    produto: str,
    quantidade: int,
    preco_unitario: float,
) -> dict:
    ...
