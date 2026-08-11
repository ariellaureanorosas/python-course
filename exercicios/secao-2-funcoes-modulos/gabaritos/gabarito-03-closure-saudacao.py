"""
Gabarito EXERCÍCIO 03 - Closure para Criar Saudação

Raciocínio sênior
-----------------
criar_saudacao é uma fábrica de funções: ela "congela" o valor de
saudacao no closure e a função interna saudar usa essa variável
livre. Cada chamada de criar_saudacao("X") gera UMA nova função
com o próprio closure — por isso bom_dia e boa_tarde não se
misturam.
A concatenação é literal (saudacao + ' ' + nome) para seguir o
enunciado e reforçar que o espaço é o separador explícito.
Alternativas descartadas: f-string — equivalente, mas o enunciado
pede concatenação com espaço.
"""


def criar_saudacao(saudacao: str):
    """Retorna uma função que saúda alguém com a saudação fixada.

    Parametros
    ----------
    saudacao : str
        Saudação a ser usada ("Olá", "Bom dia" etc.).

    Returns
    -------
    Callable[[str], str]
        Função saudar(nome) que retorna saudacao + ' ' + nome.

    Exemplos
    --------
    >>> bom_dia = criar_saudacao('Bom dia')
    >>> bom_dia('Ariel')
    'Bom dia Ariel'
    >>> ola = criar_saudacao('Olá')
    >>> ola('Maria')
    'Olá Maria'
    """
    def saudar(nome: str) -> str:
        return saudacao + ' ' + nome
    return saudar


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    bom_dia = criar_saudacao('Bom dia')
    print(bom_dia('Ariel'))

# Onde você provavelmente divergiu:
# - usou f"{saudacao}, {nome}" com vírgula (o enunciado pede
#   concatenação com espaço: "Bom dia Ariel", sem vírgula)
# - chamou a função interna criada cada vez (aqui a função retornada
#   é reutilizada: bom_dia('A') e bom_dia('B'))
# - retornou a string na hora (sem closure): a assinatura pede
#   retornar UMA FUNÇÃO, não a saudação pronta