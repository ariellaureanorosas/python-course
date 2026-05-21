"""
Analisador de Frase com split/join

Recebe uma frase digitada pelo usuário, conta a quantidade de
palavras utilizando split() e as reexibe unidas por hífen com join().
"""

SEPARADOR_HIFEN: str = "-"

frase_original: str = input("Digite uma frase: ").strip()

if not frase_original:
    print("Erro: a frase não pode estar vazia.")
else:
    lista_palavras: list = frase_original.split()
    quantidade_palavras: int = len(lista_palavras)
    frase_hifenizada: str = SEPARADOR_HIFEN.join(lista_palavras)

    print(f"Quantidade de palavras: {quantidade_palavras}")
    print(f"Frase com hífen: \"{frase_hifenizada}\"")
