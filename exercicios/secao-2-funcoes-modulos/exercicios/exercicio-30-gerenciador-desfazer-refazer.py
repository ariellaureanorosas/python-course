"""
EXERCÍCIO 30 - Gerenciador de Tarefas com Desfazer/Refazer

Tópicos: closures, pilhas (listas), anotações 03 e 18;
         exercício das aulas 125-126

Reimplemente a lista de tarefas das aulas 125/126 usando CLOSURES:
o estado (tarefas e pilha de refazer) fica fechado dentro de uma
fábrica `criar_gerenciador()` — cada gerenciador é independente.

1. `criar_gerenciador() -> dict`
   - Internamente define as listas `tarefas` e `refazer_pilha`.
   - Retorna um dict com as funções:
       "adicionar": (tarefa: str) -> list   (appenda e devolve)
       "desfazer":  () -> str | None        (pop de tarefas p/ pilha)
       "refazer":   () -> str | None        (pop da pilha p/ tarefas)
       "listar":    () -> list              (cópia da lista atual)
   - desfazer/refazer devolvem None quando não há o que desfazer
     ou refazer (sem quebrar).

Comportamento esperado:
    g = criar_gerenciador()
    g["adicionar"]("fazer café")    # ['fazer café']
    g["adicionar"]("caminhar")      # ['fazer café', 'caminhar']
    g["desfazer"]()                 # 'caminhar' (lista: ['fazer café'])
    g["refazer"]()                  # 'caminhar' (lista completa de novo)
    g["listar"]()                   # ['fazer café', 'caminhar']
    g["desfazer"](); g["desfazer"](); g["desfazer"]()   # None (vazia)

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""


def criar_gerenciador() -> dict:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    g = criar_gerenciador()
    g["adicionar"]("fazer café")
    g["adicionar"]("caminhar")
    print(g["desfazer"]())
    print(g["refazer"]())
    print(g["listar"]())