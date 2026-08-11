"""
Gabarito EXERCÍCIO 13 - Analisador de Frase com split/join

Raciocínio sênior
-----------------
A frase é limpa com .strip() na entrada — um "espaço solto" no
começo ou fim mudaria a contagem e a junção. split() sem
argumentos já normaliza múltiplos espaços (divide em palavras
reais), então a contagem com len() é confiável.
join() recebe a palavra vazia "" como caso de borda? Não: a frase
vazia é tratada antes, no if not frase_original — guarda de
qualidade em vez de deixar o join devolver "" mudo.

Alternativas descartadas: split(" ") com espaço explícito — trataria
"Python  é  legal" (dois espaços) como palavra vazia no meio.
"""

SEPARADOR_HIFEN: str = '-'

frase_original: str = input('Digite uma frase: ').strip()

if not frase_original:
    print('Erro: a frase não pode estar vazia.')
else:
    lista_palavras: list[str] = frase_original.split()
    quantidade_palavras: int = len(lista_palavras)
    frase_hifenizada: str = SEPARADOR_HIFEN.join(lista_palavras)

    print(f'Palavras: {quantidade_palavras}')
    print(f'Frase com hífen: "{frase_hifenizada}"')

# Onde você provavelmente divergiu:
# - usou split(" ") com espaço — quebra com múltiplos espaços
#   ("a  b" vira ['a', '', 'b'])
# - não tratou a frase vazia (split() de "" devolve [] e o len
#   mostra `0` sem mensagem)
# - digitou `list` sem tipo (list[str] aqui)
# - imprimiu "Quantidade de palavras:" (o enunciado exemplifica
#   "Palavras: 4").