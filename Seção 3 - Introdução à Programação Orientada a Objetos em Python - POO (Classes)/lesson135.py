# Atributos de classe


class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa("Ariel", 19)
p2 = Pessoa("Helena", 12)

print(Pessoa.ano_atual)

print(p1.ano_nascimento())
print(p2.ano_nascimento())
