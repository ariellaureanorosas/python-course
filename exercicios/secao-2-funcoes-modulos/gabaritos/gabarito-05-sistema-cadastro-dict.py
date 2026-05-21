from copy import deepcopy


def criar_pessoa(nome: str, idade: int, email: str) -> dict:
    return dict(nome=nome, idade=idade, email=email)


def atualizar_pessoa(pessoa: dict, **dados) -> dict:
    copia = deepcopy(pessoa)
    copia.update(dados)
    return copia


def listar_chaves(pessoa: dict) -> list:
    return list(pessoa.keys())


if __name__ == "__main__":
    p1 = criar_pessoa("Ana", 25, "ana@email.com")
    p2 = atualizar_pessoa(p1, idade=26, email="ana.nova@email.com")
    print(p2)
    print(listar_chaves(p2))
