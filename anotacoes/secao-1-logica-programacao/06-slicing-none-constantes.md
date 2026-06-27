# Fatiamento, None, Constantes e Try/Except

## Quando você vai usar isso?
Você precisa extrair os dígitos de um CPF, o domínio de um e-mail, ou verificar se uma função retornou algo. Também: o usuário digitou letra onde esperava número e você precisa tratar sem quebrar o programa.

## Modelo mental
Fatiar é cortar uma fatia de bolo marcando início, fim e passo. None é uma placa de "vago" no estacionamento — a vaga existe, tá vazia. Try/except é o airbag: você não dirige esperando bater, mas ele tá lá.

## Em uma linha
Extraia partes com `[i:f:p]`, represente ausência com `None`, proteja erros com `try/except`.

## Na prática

### Caso simples — fatiamento de string
```python
texto = "Python"

# ← [início : fim : passo] — índices negativos contam do final
print(texto[0])      # 'P' ← índice 0 = primeiro caractere
print(texto[-1])     # 'n' ← -1 = último, -2 = penúltimo...
print(texto[0:3])    # 'Pyt' ← do 0 ao 3 (exclusive = não inclui 3)
print(texto[::2])    # 'Pto' ← do início ao fim pulando 2 em 2
print(texto[::-1])   # 'nohtyP' ← passo negativo inverte a string
print(len(texto))    # 6 ← quantos caracteres tem
```

### Com variação — None, `is`, constantes
```python
# ← None é differente de 0, False, "" — é a ausência de valor
variavel = None

# ← SEMPRE use `is` pra comparar com None (nunca ==)
if variavel is None:
    print("Variável ainda não foi definida")

# ← `is` compara identidade (mesmo objeto), `==` compara valor
# ← None é singleton: todo None no programa é o MESMO objeto
if variavel is not None:
    print("Tem valor!")

# ← Constante = convenção com letra maiúscula
VELOCIDADE_MAXIMA = 80   # ← Python não trava — é acordo entre devs
TAXA_JUROS = 0.05        # ← ninguém deve reatribuir depois
```

### Em uso real — entrada com proteção
```python
# ← try/except mantém o programa vivo mesmo com erro
try:
    entrada = input("Digite um número: ")
    numero = float(entrada)      # ← se digitar "abc", explode aqui
except ValueError:
    # ← só cai aqui se a exceção for ValueError
    print("Isso não é um número válido")
    numero = None                # ← marca como inválido

if numero is not None:
    print(f"Dobro: {numero * 2}")
else:
    print("Não posso calcular")
```

## O que NÃO fazer
```python
texto = "Python"
print(texto[10])      # ← IndexError: string tem 6 índices (0 a 5)

valor = None
if valor == None:     # ← funciona mas NÃO faça — use `is None`
    pass

try:
    x = 10 / 0
except:               # ← except sem tipo engole TUDO (inclusive Ctrl+C)
    pass              # ← erro silencioso = debug impossível
```

## Por que Python funciona assim?
Sequências armazenam itens em índices numéricos contíguos na memória. Fatiar cria uma NOVA sequência copiando os ponteiros dos elementos no intervalo. None é um singleton — o interpretador aloca um único objeto None e todo `None` no código aponta pra ele (por isso `is` funciona). Try/except inspeciona a exceção que subiu pela pilha de chamada: se o tipo casa com o except, executa; senão, continua subindo até o topo (e o programa morre).

## Conexões
- Você já usou esse padrão quando: acessou `lista[0]` pra pegar o primeiro item
- Aparece também em: slices em listas e tuplas; None em funções sem `return` explícito; try/except em arquivos, API, banco de dados
- Diferente de: `None` ≠ `False`, `0`, `""` (são falsy, mas NÃO são None); `[0:3]` ≠ `[0:2]` (o índice final é exclusivo — não entra)

---

## Teste de recuperação — responda sem olhar para cima

1. `texto[::-1]` produz o quê e por quê?
2. Escreva um bloco que tenta converter "42abc" para int, trata o erro e atribui None.
3. Qual a diferença prática entre `is None` e `== None`?

---

**Frase-âncora:** "Fatie com [i:f:p], marque vazio com None, proteja com try/except."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
