"""
Exercício 03 - Closure para Criar Saudação

Crie uma função `criar_saudacao(saudacao: str)` que:
- Receba uma string de saudação (ex: "Olá", "Bom dia")
- Retorne uma função `saudar(nome: str) -> str`
- A função retornada deve concatenar a saudação + " " + nome

Tópicos da aula: closure, função que retorna função, variáveis livres
"""


def criar_saudacao(saudacao: str):
    def saudar(nome: str):
        return f"{saudacao}, {nome}"

    return saudar


if __name__ == "__main__":
    bom_dia = criar_saudacao("Bom dia")
    print(bom_dia("Ariel"))
