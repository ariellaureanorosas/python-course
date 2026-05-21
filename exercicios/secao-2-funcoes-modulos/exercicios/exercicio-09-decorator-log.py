"""
Exercício 09 - Decorator de Log

Crie um decorator `@log_execucao` que:
- Imprima "Executando [nome_da_funcao] com argumentos ([args], [kwargs])"
- Execute a função decorada
- Imprima "Resultado: [resultado]"
- Retorne o resultado da função
- Use @wraps de functools para preservar os metadados da função

Tópicos da aula: decorators, @wraps, *args, **kwargs, print
"""


def log_execucao(func):
    ...
