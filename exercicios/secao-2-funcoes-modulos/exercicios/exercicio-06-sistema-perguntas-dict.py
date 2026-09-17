"""
EXERCÍCIO 06 - Sistema de Perguntas e Respostas com Dict

Tópicos: dict, input, for, manipulação de dicts

Crie a função `executar_quiz(perguntas: list[dict]) -> int`:

Cada pergunta é um dict com:
    - 'pergunta': str com o enunciado
    - 'opcoes': dict com as alternativas (ex: {'a': 'Python', ...})
    - 'resposta': str com a letra da resposta correta (ex: 'a')

A função deve:
1. Percorrer a lista de perguntas
2. Exibir cada pergunta e suas opções (use print)
3. Capturar a resposta do usuário com input()
4. Verificar se a resposta está correta
5. Contabilizar os acertos
6. Retornar o total de acertos

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from typing import cast


def verificar_resposta(
    pergunta: dict[str, str | dict[str, str]], resposta: str
) -> bool:
    return resposta == pergunta["resposta"]


def executar_quiz(perguntas: list[dict[str, str | dict[str, str]]]) -> int:
    acertos = 0
    for pergunta in perguntas:
        print(pergunta)
        texto = cast("dict[str, str]", pergunta["opcoes"])
        for letra, conteudo in texto.items():
            print(f"{letra}) {conteudo}")
        resposta = input("Digite a opção correta: ").strip().lower()
        if verificar_resposta(pergunta, resposta):
            acertos += 1
        else:
            print(f"Incorreto! A resposta era {pergunta['resposta']}\n")
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
    return acertos


if __name__ == "__main__":
    PERGUNTAS = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": {"a": "Rio de Janeiro", "b": "Brasília", "c": "São Paulo"},
            "resposta": "b",
        },
    ]
    executar_quiz(PERGUNTAS)
