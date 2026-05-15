# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.


class Classe:
    @staticmethod
    def funcao_na_classe(*args, **kwargs):
        print("oi", args, kwargs)


def funcao(*args, **kwargs):
    print("oi - funcao", args, kwargs)


c1 = Classe()
c1.funcao_na_classe(123, nomeado="nomeado")
funcao(123, nomeado="Qualquer Coisa")
