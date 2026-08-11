"""
Gabarito EXERCÍCIO 06 - Sistema de Perguntas e Respostas com Dict

Raciocínio sênior
-----------------
O quiz separa a LÓGICA (verificar_resposta: comparação pura, sem
I/O) da INTERAÇÃO (executar_quiz: prints e input). Essa separação é
o que permite testar verificar_resposta isoladamente com doctest —
e é o mesmo princípio que um sênior aplica ao separar regra de
negócio de interface. A resposta é normalizada (.strip().lower())
para 'A ' ou 'a' acertarem igual.
Alternativas descartadas: confirmar a resposta dentro do print
(mistura camadas); retornar bool em executar_quiz (o enunciado pede
o total de acertos como int).
"""


def verificar_resposta(pergunta: dict, resposta: str) -> bool:
    """Confere se a resposta corresponde à resposta correta.

    Parametros
    ----------
    pergunta : dict
        Dict com a chave 'resposta' (letra correta).
    resposta : str
        Letra escolhida pelo usuário.

    Returns
    -------
    bool
        True se a resposta está correta.

    Exemplos
    --------
    >>> p = {'responder': '...', 'resposta': 'b'}
    >>> verificar_resposta(p, 'b')
    True
    >>> verificar_resposta(p, 'a')
    False
    """
    return resposta == pergunta["resposta"]


def executar_quiz(perguntas: list[dict]) -> int:
    """Executa o quiz interativo e retorna o total de acertos.

    Parametros
    ----------
    perguntas : list[dict]
        Lista de perguntas, cada uma com 'pergunta', 'opcoes' e
        'resposta'.

    Returns
    -------
    int
        Quantidade de respostas corretas.
    """
    acertos = 0
    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for letra, texto in pergunta["opcoes"].items():
            print(f"{letra}) {texto}")
        resposta = input("Sua resposta: ").strip().lower()
        if verificar_resposta(pergunta, resposta):
            acertos += 1
            print("Correto!\n")
        else:
            print(f"Incorreto! A resposta era {pergunta['resposta']}\n")
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
    return acertos


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    PERGUNTAS = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": {"a": "Rio de Janeiro", "b": "Brasília", "c": "São Paulo"},
            "resposta": "b",
        },
    ]
    executar_quiz(PERGUNTAS)

# Onde você provavelmente divergiu:
# - colocou o print da opção/resultado junto do cálculo da resposta
#   (aqui verificar_resposta é uma função pura, testável)
# - não normalizou a resposta ('B' ou 'b ' falha sem .strip().lower())
# - usou pergunta['opcoes'].values() sem as letras (o print das
#   alternativas precisa de "a) ...", "b) ..." — items() entrega)