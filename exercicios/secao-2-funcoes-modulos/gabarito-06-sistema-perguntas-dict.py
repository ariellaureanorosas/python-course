"""
Gabarito 06 - Sistema de Perguntas e Respostas com Dict
"""


def executar_quiz(perguntas: list[dict]) -> int:
    """Executa um quiz interativo e retorna o número de acertos.

    Cada pergunta é um dict com as chaves 'pergunta', 'opcoes' e 'resposta'.

    Exemplo de uso:
        >>> perguntas = [
        ...     {
        ...         'pergunta': 'Qual é a capital do Brasil?',
        ...         'opcoes': {'a': 'Rio de Janeiro', 'b': 'Brasília', 'c': 'São Paulo'},
        ...         'resposta': 'b',
        ...     },
        ...     {
        ...         'pergunta': 'Python é uma linguagem...',
        ...         'opcoes': {'a': 'Compilada', 'b': 'Interpretada', 'c': 'Assembly'},
        ...         'resposta': 'b',
        ...     },
        ... ]
        >>> total = executar_quiz(perguntas)  # execução interativa
    """
    acertos = 0

    for pergunta in perguntas:
        print(pergunta["pergunta"])

        for letra, texto in pergunta["opcoes"].items():
            print(f"{letra}) {texto}")

        resposta_usuario = input("Sua resposta: ").strip().lower()

        if resposta_usuario == pergunta["resposta"]:
            acertos += 1
            print("Correto!\n")
        else:
            print(f"Incorreto! A resposta era {pergunta['resposta']}\n")

    print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
    return acertos
