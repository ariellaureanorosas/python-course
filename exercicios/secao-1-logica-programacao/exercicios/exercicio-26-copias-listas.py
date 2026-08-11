"""
EXERCÍCIO 26 — Mutabilidade e Cópias de Listas

Tópicos: mutabilidade, id(), variáveis como rótulos, .copy()

Em Python, listas são mutáveis e variáveis são RÓTULOS (referências),
não caixas. Prove isso com prints, nesta ordem:

  1. Crie lista_original = ["a", "b", "c"] e
     lista_alias = lista_original. Exiba o id() das duas — devem
     ser iguais (mesmo objeto).
  2. Adicione "d" em lista_alias (append) e exiba lista_original —
     ela muda junto!
  3. Crie lista_copia = lista_original.copy(). Adicione "e" em
     lista_copia e exiba lista_original — deve continuar sem "e".
  4. Para comparar com tipos imutáveis: x = 5; y = x; y += 1.
     Exiba "x = {x}, y = {y}" — x continua 5.

Exemplo de saída esperada (sem input, ids variam):
id lista_original: 2623456789
id lista_alias:    2623456789
Lista original após mudar a alias: ['a', 'b', 'c', 'd']
Lista original após mudar a cópia: ['a', 'b', 'c', 'd']
x = 5, y = 6

Dica: = nunca copia — apenas cria mais um rótulo para o mesmo objeto;
.copy() (ou [:] do slicing, nota 06) cria um objeto novo.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========