# Lógica de Validação de CPF

## Quando você vai usar isso?
Sempre que um sistema brasileiro precisar validar CPF em cadastros, formulários ou emissão de notas. O algoritmo dos dígitos verificadores detecta erros de digitação — um caractere trocado e as "assinaturas" não batem.

## Modelo mental
O CPF é um cheque com duas assinaturas de segurança (os dois últimos dígitos) calculadas a partir dos 9 primeiros. Os pesos regressivos (10, 9, 8... 2) são como uma balança que dá mais importância aos primeiros dígitos. Se você errar um número, as assinaturas não conferem.

## Em uma linha
Valida CPF calculando dois dígitos verificadores com pesos regressivos (10→2 e 11→2) e módulo 11, rejeitando sequências repetidas.

## Na prática

### Caso simples

```python
cpf = "746824890"                     # ← 9 dígitos iniciais (sem formatação)
soma = 0
for i in range(9):                    # ← i = 0 a 8
    soma += int(cpf[i]) * (10 - i)    # ← 1º dígito × 10, 2º × 9 ... 9º × 2
resto = (soma * 10) % 11              # ← multiplica soma por 10, extrai resto
digito1 = 0 if resto > 9 else resto   # ← se resto > 9, dígito = 0
```

### Com variação

```python
cpf_10 = cpf + str(digito1)           # ← agora temos 10 dígitos
soma = 0
for i in range(10):                   # ← i = 0 a 9
    soma += int(cpf_10[i]) * (11 - i) # ← 1º × 11, 2º × 10 ... 10º × 2
resto = (soma * 10) % 11
digito2 = 0 if resto > 9 else resto

# ← CPF completo: "74682489070"
cpf_gerado = cpf + str(digito1) + str(digito2)
```

### Em uso real

```python
import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r"[^0-9]", "", cpf)   # ← remove pontos e traços

    if cpf == cpf[0] * len(cpf):       # ← rejeita 111.111.111-11 etc.
        return False

    # ← 1º dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 0 if (soma * 10) % 11 > 9 else (soma * 10) % 11

    # ← 2º dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 0 if (soma * 10) % 11 > 9 else (soma * 10) % 11

    return cpf == cpf[:9] + str(digito1) + str(digito2)
```

## O que NÃO fazer

```python
# ← ERRADO: pular a validação de sequência repetida
cpf = "11111111111"
# ← Os dígitos verificadores de 111.111.111 são 11 — passa no cálculo!
# ← Mas sequências repetidas são inválidas por regra do Ministério da Fazenda

# ← ERRADO: processar CPF com pontuação sem limpar
cpf = "746.824.890-70"
soma = sum(int(cpf[i]) * (10 - i) for i in range(9))  # ← ValueError!
# ← "." e "-" não podem ser convertidos para int

# ← ERRADO: confundir índice — range(9) vai de 0 a 8, que são os 9 primeiros dígitos
# range(10) vai de 0 a 9, que são os 10 primeiros (após adicionar digito1)
```

## Por que Python funciona assim?
`range(9)` com `10 - i` gera os pesos automaticamente (10, 9, 8... 2). `(soma * 10) % 11` implementa o módulo 11 definido pelo Ministério da Fazenda: resto 0-9 vira o próprio dígito, resto 10 vira 0. A verificação `cpf == cpf[0] * len(cpf)` funciona porque multiplicar string por inteiro replica o conteúdo — `"1" * 11` = `"11111111111"`. `re.sub(r"[^0-9]", "", texto)` substitui tudo que *não* for dígito por string vazia, limpando a formatação.

## Conexões
- Você já usou esse padrão quando: validou dígitos de conta bancária ou CNPJ (mesmo algoritmo de módulo 11)
- Aparece também em: máquinas de cartão, sistemas bancários, nota fiscal eletrônica, formulários gov.br
- Diferente de: validação por regex — regex só verifica formato `XXX.XXX.XXX-XX`, não a integridade matemática dos dígitos

---

## Teste de recuperação — responda sem olhar para cima

1. Por que os pesos do primeiro dígito vão de 10 a 2, e do segundo dígito de 11 a 2?
2. Escreva uma função que recebe "123.456.789-09" e retorna "12345678909".
3. Qual problema ocorre se você validar "000.000.000-00" sem a checagem de sequência repetida?

---

**Frase-âncora:** "Nove dígitos geram duas assinaturas matemáticas que autenticam o CPF."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
