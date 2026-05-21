def verificar_resposta(pergunta: dict, resposta: str) -> bool:
    return resposta == pergunta["resposta"]


def executar_quiz(perguntas: list[dict]) -> int:
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
    PERGUNTAS = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": {"a": "Rio de Janeiro", "b": "Brasília", "c": "São Paulo"},
            "resposta": "b",
        },
    ]
    executar_quiz(PERGUNTAS)
