"""
EXERCÍCIO 07 — Analisador de Nome com Slicing

Tópicos: input(), strings, slicing, métodos de string

Receba um nome completo do usuário e exiba as seguintes informações:

  1. Nome em maiúsculas
  2. Nome em minúsculas
  3. Quantidade total de letras (desconsiderando espaços)
  4. Quantidade de letras do primeiro nome
  5. Último sobrenome (dica: use .split() ou combine slicing com
     .find() / .rfind())
  6. Nome invertido (ex.: "João Silva" → "avliS oãoJ")

ATENÇÃO: Você pode usar .split() (já ensinado implicitamente em
aulas de string), mas não pode usar listas de forma explícita.
Use fatiamento (slicing) e métodos de string (.upper(), .lower(),
.find(), .rfind(), .count(), len()).

Exemplo:
  Nome completo: Maria Clara Santos
  Maiúsculas: MARIA CLARA SANTOS
  Minúsculas: maria clara santos
  Total de letras: 16
  Primeiro nome: Maria (5 letras)
  Último sobrenome: Santos
  Nome invertido: sotnaS aralC airaM

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========