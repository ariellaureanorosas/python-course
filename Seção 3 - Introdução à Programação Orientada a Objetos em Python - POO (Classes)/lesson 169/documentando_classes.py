"""Exemplos de documentação (docstrings) em classes Python"""


class MinhaClasse:
    """Documentação da classe MinhaClasse

    Esta classe serve como exemplo para demonstrar o uso de docstrings
    em classes, métodos, propriedades, etc.
    """

    variavel_de_classe: str = "Valor da classe"

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma instância de MinhaClasse

        :param nome: Nome da pessoa
        :type nome: str
        :param idade: Idade da pessoa
        :type idade: int
        """
        self.nome = nome
        self.idade = idade

    def metodo_instancia(self) -> str:
        """Método de instância que retorna uma saudação

        :return: String com saudação personalizada
        :rtype: str
        """
        return f"Olá, meu nome é {self.nome}"

    @classmethod
    def metodo_classe(cls) -> str:
        """Método de classe que retorna a variável de classe

        :return: Valor de variavel_de_classe
        :rtype: str
        """
        return cls.variavel_de_classe

    @staticmethod
    def metodo_estatico() -> str:
        """Método estático que retorna uma mensagem fixa

        :return: Mensagem fixa
        :rtype: str
        """
        return "Este é um método estático"

    @property
    def nome_e_idade(self) -> str:
        """Propriedade que combina nome e idade

        :return: String com nome e idade
        :rtype: str
        """
        return f"{self.nome} tem {self.idade} anos"
