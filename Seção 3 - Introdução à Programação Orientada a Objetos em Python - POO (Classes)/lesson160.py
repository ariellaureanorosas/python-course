def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    except Exception as error:
        print("Ocorreu erro", error)
    finally:
        print("fechando arquivo")
        arquivo.close()


with my_open("aula148.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    print("WITH", arquivo)
