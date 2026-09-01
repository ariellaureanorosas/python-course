"""
Gabarito EXERCÍCIO 22 - Calculadora com while

Raciocínio sênior
-----------------
A arquitetura é a de qualquer CLI de menu: laço infinito (while True)
com saída EXPLÍCITA via break — a flag "executando" da nota 07 seria
equivalente, mas o break deixa o fluxo mais direto. A validação da
opção acontece ANTES de ler os números (evita leitura desperdiçada).
A divisão é a única operação que pode falhar em tempo de execução, e
os erros são capturados de forma ESPECÍFICA: ZeroDivisionError, não
um except genérico que esconderia bugs reais (como o usuário digitar
texto no lugar de número).

Alternativas descartadas: função para cada operação — organização só
chega com funções na Seção 2; dict de operadores — idem (funções como
valores são assunto da Seção 2).
"""

while True:
    print("\n=== CALCULADORA ===")
    print("1) Somar  2) Subtrair  3) Multiplicar  4) Dividir  5) Sair")

    opcao: str = input("Opção: ")

    if opcao == "5":
        print("Saindo...")
        break

    if opcao not in "1234":
        print("Opção inválida.")
        continue

    num1: float = float(input("Primeiro número: "))
    num2: float = float(input("Segundo número: "))

    if opcao == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcao == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcao == "3":
        print(f"Resultado: {num1 * num2}")
    else:
        try:
            print(f"Resultado: {num1 / num2}")
        except ZeroDivisionError:
            print("Erro: divisão por zero.")

# Onde você provavelmente divergiu:
# - usou "5" no mesmo if das operações e calculou antes de validar a opção
# - converteu a opção com int() (travava o menu com ValueError em texto)
# - fez try/except em torno de TODAS as operações — só a divisão precisa
# - tratou divisão por zero com if num2 == 0 (funciona, mas o tratamento
#   de erro nativo é mais idiomático e cobre casos futuros)
# - esqueceu o float() nos números, somando strings ("10" + "5" = "105")
