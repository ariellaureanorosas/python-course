# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(BASE_PATH, "aula137.json")


class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = self.ano_atual - idade


p1 = Pessoa("Ariel", 19)
p2 = Pessoa("Laureano", 25)
p3 = Pessoa("Rosas", 30)
bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, "w", encoding="utf8") as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        print("Dump Feito")


if __name__ == "__main__":
    print("Esse arquivo é o:", __name__)
    fazer_dump()
