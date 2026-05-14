# __dict__ e vats para atributos de instância


class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {"nome": "Ariel", "idade": 19}
p1 = Pessoa(**dados)
print(vars(p1))
print(p1.nome)

# p1.__dict__["Qualquer"] = "Coisa"
# del p1.__dict__["nome"]
# print(p1.__dict__)
# print(vars(p1))
# print(p1.Qualquer)
