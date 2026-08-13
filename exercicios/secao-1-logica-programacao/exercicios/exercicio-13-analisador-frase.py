"""
EXERCÍCIO 13 — Analisador de Frase com split/join

Tópicos: split(), join(), len()

Receba uma frase (string) do usuário.
Use o método split() para separar as palavras.
Mostre quantas palavras a frase contém.
Depois, use o método join() para juntar as palavras com hífen (-) entre elas.
Exiba o resultado.

Exemplo:
    Frase: "Python é muito legal"
    Palavras: 4
    Frase com hífen: "Python-é-muito-legal"

Dica: split() sem argumentos separa por espaços em branco.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========

frase: str = input("Digite uma frase: ")
if not frase:
    print("ERRO: A frase não deve ser enviada vazia")
else:
    frase_repartida: list[str] = frase.split()
    frase_com_hifen = "-".join(frase_repartida)
    print(f"Frase: {frase}")
    print(f"palavras: {len(frase_repartida)}")
    print(f"Frase com hífen: {frase_com_hifen}")
