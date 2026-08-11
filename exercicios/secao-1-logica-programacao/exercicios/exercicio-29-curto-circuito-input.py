"""
EXERCÍCIO 29 — Curto-circuito com or e fallback

Tópicos: or, and, curto-circuito, truthy/falsy, input()

O operador or avalia a 1ª expressão; se ela for Truthy, usa-a e NÃO
avalia a 2ª (curto-circuito); se for Falsy (ex.: string vazia),
usa a 2ª. Isso permite valores padrão sem if:

  1. Receba a CIDADE com o padrão: a cidade digitada ou, se vazio,
     "São Paulo" — usando `input(...) or "São Paulo"`.
  2. Receba a PROFISSAO com o padrão "Estudante", mesma técnica.
  3. Exiba "Cidade: {cidade}" e "Profissão: {profissao}".
  4. Demonstre o curto-circuito exibindo o retorno de:
       True and "chegou aqui"   →  o 2º operando (and só segue se True)
       "" or "fallback"         →  o 2º operando (vazio é Falsy)
     Em uma linha de print para cada.

Exemplo de saída esperada (entradas: "Porto Alegre" e vazio):
Cidade: Porto Alegre
Profissão: Estudante
chegou aqui
fallback

Dica: "" (string vazia), 0 e None são Falsy; qualquer string com
conteúdo é Truthy.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========