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


def executar_quiz(perguntas: list[dict]) -> int:
    ...


if __name__ == "__main__":
    PERGUNTAS = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": {"a": "Rio de Janeiro", "b": "Brasília", "c": "São Paulo"},
            "resposta": "b",
        },
    ]
    executar_quiz(PERGUNTAS)