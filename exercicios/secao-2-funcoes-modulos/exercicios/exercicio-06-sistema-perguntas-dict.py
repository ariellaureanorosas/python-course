"""
Exercício 06 - Sistema de Perguntas e Respostas com Dict

Baseado na aula 79, crie uma função `executar_quiz(perguntas: list[dict]) -> int` onde:

Cada pergunta é um dict com:
    - 'pergunta': str com o enunciado
    - 'opcoes': dict com as alternativas (ex: {'a': 'Python', 'b': 'Java', ...})
    - 'resposta': str com a letra da resposta correta (ex: 'a')

A função deve:
    - Percorrer a lista de perguntas
    - Exibir cada pergunta e suas opções (use print)
    - Capturar a resposta do usuário com input()
    - Verificar se a resposta está correta
    - Contabilizar os acertos
    - Retornar o total de acertos

Tópicos da aula: dict, input, for, manipulação de dicts
"""


def verificar_resposta(pergunta: dict, resposta: str) -> bool:
    return resposta == pergunta["resposta"]


def executar_quiz(perguntas: list[dict]) -> int:
    acertos = 0
    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for alternativa, texto in pergunta["opcoes"].items():
            print(f"{alternativa}) {texto}")
        resposta = input("Digite a alternativa correta: ").strip().lower()
        if verificar_resposta(pergunta, resposta):
            acertos += 1
            print("Correta a resposta")
        else:
            print("Resposta Errada")
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
