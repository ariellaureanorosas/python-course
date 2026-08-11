"""
EXERCÍCIO 30 — Gerador de CPF

Tópicos: random, for, validação (módulo 11), formatação de string

Crie uma função gerar_cpf() que gera um CPF VÁLIDO:

  - Sorteie 9 dígitos (random.randint(0, 9)) e monte a string inicial.
  - Calcule o 1º dígito verificador com a lógica da anotação 13
    (pesos regressivos 10→2 + módulo 11).
  - Calcule o 2º dígito verificador com os pesos 11→2 sobre os
    10 primeiros dígitos.
  - Retorne o CPF FORMATADO "XXX.XXX.XXX-XX".
  - No final, gere e exiba 3 CPFs.

Para conferir que está certo, escreva também uma função
validar_cpf() com a MESMA lógica do gabarito do exercício 19 (copie
a lógica para dentro do seu arquivo) e imprima "válido" apenas se o
CPF gerado passar na validação.

Exemplo de saída esperada (varia a cada execução):
529.982.247-25 — válido
111.444.777-35 — válido
390.533.447-05 — válido

Dica: para formatar, use slicing: f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}".

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========