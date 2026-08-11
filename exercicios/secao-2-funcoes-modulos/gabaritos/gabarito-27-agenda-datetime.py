"""
Gabarito EXERCÍCIO 27 - Agenda com datetime

Raciocínio sênior
-----------------
O datetime exige converter texto ↔ objeto por máscaras EXPLÍCITAS:
strptime lê "2026-08-11 14:30" segundo "%Y-%m-%d %H:%M" e strftime
escreve segundo "%d/%m/%Y %H:%M" — o formato nunca é adivinhado.
date.fromisoformat é o atalho para datas ISO (a mais comum em APIs).
A subtração de dates devolve timedelta, cujo .days é a diferença
inteira — o abs() garante ordem irrelevante dos argumentos. A idade
desconta o ano quando o aniversário ainda não chegou no ano atual:
comparar TUPLAS (month, day) é a forma pythonica de comparar datas
parciais sem montar datetime.

Alternativas descartadas: manipular strings com split e aritmética
manual (replica o que o módulo já faz); timedelta em idade (meses
variam de tamanho — a comparação de tuplas é a certa).
"""

from datetime import date, datetime


def formatar_data_hora(iso: str) -> str:
    """Converte data-hora ISO para o formato brasileiro.

    Parâmetros
    ----------
    iso : str
        Data-hora "AAAA-MM-DD HH:MM".

    Retorna
    -------
    str
        Data-hora "DD/MM/AAAA HH:MM".

    Exemplos
    --------
    >>> formatar_data_hora("2026-08-11 14:30")
    '11/08/2026 14:30'
    """
    momento = datetime.strptime(iso, "%Y-%m-%d %H:%M")
    return momento.strftime("%d/%m/%Y %H:%M")


def dias_entre(inicio: str, fim: str) -> int:
    """Devolve a diferença em dias entre duas datas (sempre positiva).

    Parâmetros
    ----------
    inicio : str
        Data "AAAA-MM-DD".
    fim : str
        Data "AAAA-MM-DD".

    Retorna
    -------
    int
        |fim - inicio| em dias.

    Exemplos
    --------
    >>> dias_entre("2026-08-11", "2026-08-15")
    4
    >>> dias_entre("2026-08-15", "2026-08-11")
    4
    """
    d_inicio = date.fromisoformat(inicio)
    d_fim = date.fromisoformat(fim)
    return abs((d_fim - d_inicio).days)


def calcular_idade(nascimento: str, hoje: str) -> int:
    """Calcula a idade em anos completos.

    Parâmetros
    ----------
    nascimento : str
        Data de nascimento "AAAA-MM-DD".
    hoje : str
        Data de referência "AAAA-MM-DD".

    Retorna
    -------
    int
        Anos completos na data de referência.

    Exemplos
    --------
    >>> calcular_idade("2000-05-10", "2026-08-11")
    26
    >>> calcular_idade("2000-12-31", "2026-01-01")
    25
    """
    niver = date.fromisoformat(nascimento)
    atual = date.fromisoformat(hoje)

    idade = atual.year - niver.year
    if (atual.month, atual.day) < (niver.month, niver.day):
        idade -= 1
    return idade


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(formatar_data_hora("2026-08-11 14:30"))
    print(dias_entre("2026-08-11", "2026-08-15"))
    print(calcular_idade("2000-05-10", "2026-08-11"))

# Onde você provavelmente divergiu:
# - trocou strptime por strftime (um lê, o outro escreve)
# - montou a data com datetime.strptime mas retornou como str() —
#   o repr do datetime não é "DD/MM/AAAA HH:MM"
# - usou (d_fim - d_inicio).days sem abs() e quebrou na ordem inversa
# - calculou idade só com anos (2000→2026 = 26 mesmo antes do
#   aniversário) — o desconto da tupla (month, day) é o que corrige
# - assumiu fuso/horário: date() é suficiente para datas puras