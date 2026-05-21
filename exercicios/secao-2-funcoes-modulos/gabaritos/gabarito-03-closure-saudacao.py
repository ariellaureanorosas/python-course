def criar_saudacao(saudacao: str):
    def saudar(nome: str) -> str:
        return f"{saudacao} {nome}"
    return saudar


if __name__ == "__main__":
    bom_dia = criar_saudacao("Bom dia")
    print(bom_dia("Maria"))
