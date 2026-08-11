"""
Gabarito EXERCÍCIO 30 - Gerenciador de Tarefas com Desfazer/Refazer

Raciocínio sênior
-----------------
As aulas 125/126 guardavam o estado em duas listas passadas como
argumento; aqui o estado é fechado por CLOSURES — a fábrica cria
`tarefas` e `refazer_pilha` e devolve funções que as "veem". Isso
remove o risco de qualquer código externo zerar as pilhas e permite
criar N gerenciadores independentes. desfazer é pop() de uma pilha
(último a entrar, primeiro a sair — LIFO) jogando para a outra;
refazer desfaz o desfazer. Quando a pilha está vazia, `if not
tarefas:` (Truthy/Falsy, anotação 19) responde None em vez de quebrar.

Alternativas descartadas: listas globais (vazamento de estado);
classe (a Seção 3 ainda não começou — a closure entrega o mesmo
encapsulamento com a ferramenta desta seção).
"""


def criar_gerenciador() -> dict:
    """Cria um gerenciador de tarefas com desfazer/refazer.

    Cada chamada cria pilhas independentes (closures).

    Retorna
    -------
    dict
        Chaves 'adicionar', 'desfazer', 'refazer' e 'listar'
        apontando para as funções do gerenciador.

    Exemplos
    --------
    >>> g = criar_gerenciador()
    >>> g["adicionar"]("fazer café")
    ['fazer café']
    >>> g["adicionar"]("caminhar")
    ['fazer café', 'caminhar']
    >>> g["desfazer"]()
    'caminhar'
    >>> g["listar"]()
    ['fazer café']
    >>> g["refazer"]()
    'caminhar'
    >>> g["listar"]()
    ['fazer café', 'caminhar']
    >>> g["desfazer"]()
    'caminhar'
    >>> g["desfazer"]()
    'fazer café'
    >>> g["desfazer"]() is None
    True
    """
    tarefas: list = []
    refazer_pilha: list = []

    def adicionar(tarefa: str) -> list:
        tarefas.append(tarefa)
        return tarefas

    def desfazer() -> str | None:
        if not tarefas:
            return None
        refazer_pilha.append(tarefas.pop())
        return refazer_pilha[-1]

    def refazer() -> str | None:
        if not refazer_pilha:
            return None
        tarefas.append(refazer_pilha.pop())
        return tarefas[-1]

    def listar() -> list:
        return tarefas

    return {
        "adicionar": adicionar,
        "desfazer": desfazer,
        "refazer": refazer,
        "listar": listar,
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    g = criar_gerenciador()
    g["adicionar"]("fazer café")
    g["adicionar"]("caminhar")
    print(g["desfazer"]())
    print(g["refazer"]())
    print(g["listar"]())

# Onde você provavelmente divergiu:
# - declarou tarefas/refazer fora da fábrica (global) — vazaria
#   estado entre gerenciadores
# - esqueceu de truncar a pilha de refazer ao adicionar um item NOVO
#   (editores reais invalidam o refazer após nova edição; as aulas
#   125/126 não fazem — mantive fiel ao curso, mas vale a melhoria)
# - usou pop(0) — índice 0 é O(n); pop() do fim é O(1) e LIFO, que
#   é a semântica certa do desfazer
# - retornou a lista interna em "listar" — quem recebe pode mutá-la;
#   devolver uma cópia (tarefas[:]) é o contrato mais seguro