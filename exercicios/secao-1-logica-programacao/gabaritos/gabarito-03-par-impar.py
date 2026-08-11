"""
Gabarito EXERCÍCIO 03 - Par ou Ímpar com Validação

Raciocínio sênior
-----------------
int(input()) lança ValueError quando o texto não é numérico — por
isso o except captura exatamente ValueError (nunca exceção genérica
ou TypeError). O operador % é a forma exata de testar paridade e
funciona para negativos: o resto de -4 % 2 também é 0.
O else do try garante que só calculamos paridade se a conversão
funcionou — validação e cálculo nunca se misturam.
"""

try:
    numero: int = int(input('Digite um número: '))
except ValueError:
    print('Erro: digite um número inteiro válido.')
else:
    paridade: str = 'par' if numero % 2 == 0 else 'ímpar'
    print(f'{numero} é {paridade}.')

# Onde você provavelmente divergiu:
# - capturou TypeError ou exceção genérica (a conversão falha com
#   ValueError — capturar demais esconde bugs reais)
# - escreveu "impar" sem acento (o enunciado pede "ímpar")
# - usou if/else em vez do ternário para a paridade (as duas funcionam;
#   aqui o ternário deixa a leitura alinhada à intenção)
# - esqueceu o "." no final da mensagem