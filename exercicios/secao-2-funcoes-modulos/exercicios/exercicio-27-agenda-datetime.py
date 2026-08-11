"""
EXERCÍCIO 27 - Agenda com datetime

Tópicos: datetime, strptime, strftime, timedelta, anotação 17

Implemente três funções:

1. `formatar_data_hora(iso: str) -> str`
   - Recebe "AAAA-MM-DD HH:MM" e devolve "DD/MM/AAAA HH:MM" usando
     datetime.strptime (entrada) e strftime (saída).

2. `dias_entre(inicio: str, fim: str) -> int`
   - Recebe duas datas "AAAA-MM-DD", converte com date.fromisoformat
     e devolve a diferença em dias, sempre positiva (abs de
     timedelta.days).

3. `calcular_idade(nascimento: str, hoje: str) -> int`
   - Recebe o nascimento e a data atual "AAAA-MM-DD" e devolve a
     idade, descontando 1 ano se o aniversário do ano ainda não
     aconteceu.

Comportamento esperado:
    formatar_data_hora("2026-08-11 14:30")      # '11/08/2026 14:30'
    dias_entre("2026-08-11", "2026-08-15")      # 4
    calcular_idade("2000-05-10", "2026-08-11")  # 26

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def formatar_data_hora(iso: str) -> str:
    ...


def dias_entre(inicio: str, fim: str) -> int:
    ...


def calcular_idade(nascimento: str, hoje: str) -> int:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(formatar_data_hora("2026-08-11 14:30"))
    print(dias_entre("2026-08-11", "2026-08-15"))
    print(calcular_idade("2000-05-10", "2026-08-11"))