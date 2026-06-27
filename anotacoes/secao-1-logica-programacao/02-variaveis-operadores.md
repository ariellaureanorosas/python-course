# Variáveis e Operadores

## Quando você vai usar isso?
Você precisa guardar um dado para usar depois — nome do usuário, preço do produto, resultado de uma conta. Variáveis são seus potes de armazenamento. Operadores são as ferramentas que transformam esses dados: somar, dividir, repetir.

## Modelo mental
Variável é um post-it grudado numa caixa — o nome é o que você vê, o conteúdo é o dado. Operador aritmético é o liquidificador: você joga ingredientes (números) e ele devolve algo processado.

## Em uma linha
Variáveis nomeiam valores na memória; operadores aritméticos transformam números; concatenação e repetição fazem o mesmo com strings.

## Na prática

### Caso simples
```python
# Declaração de variáveis seguindo PEP 8 — snake_case + type hint (opcional, mas clareza)
nome_completo: str = "João Silva"  # ← snake_case: minúsculas com underlines entre palavras
idade: int = 30                     # ← type hint diz que tipo você espera — não é obrigatório
altura: float = 1.75                # ← float para números com casas decimais
maior_de_idade: bool = idade >= 18  # ← a própria expressão já resolve True ou False
```

### Com variação
```python
# Operadores aritméticos — cada um faz uma transformação diferente nos números
soma = 10 + 5          # ← + adição: junta dois valores numéricos
diferenca = 10 - 5     # ← - subtração: tira o segundo do primeiro
produto = 10 * 5       # ← * multiplicação: repete o primeiro pelo segundo
quociente = 10 / 5     # ← / divisão real: sempre retorna float (mesmo que a divisão seja exata)
parte_inteira = 10 // 3  # ← // divisão inteira: trunca a parte decimal, resultado é int
exponencial = 2 ** 3   # ← ** exponenciação: 2 elevado à terceira potência = 8
resto = 10 % 3          # ← % módulo: resto da divisão de 10 por 3 = 1
```

### Em uso real
```python
# Cálculo de IMC — combina operadores e variáveis num cenário real
peso = 80               # ← peso em kg (int ou float)
altura = 1.75           # ← altura em metros (float — precisa ser float pra divisão funcionar)
imc = peso / (altura ** 2)  # ← IMC = peso ÷ (altura × altura); os parênteses garantem a ordem
print(f"IMC: {imc:.2f}")    # ← :.2f formata o float com exatamente 2 casas decimais

# Concatenação e repetição — operadores funcionam também com strings
nome = "João" + " " + "Silva"  # ← + concatena: junta strings numa só
eco = "A" * 10                  # ← * repete: string multiplicada vira repetição
```

## O que NÃO fazer
```python
# Ignorar a precedência de operadores e esquecer os parênteses
resultado = 10 + 5 * 2      # ← 10 + 10 = 20 (multiplicação vem primeiro)
resultado = (10 + 5) * 2    # ← 15 * 2 = 30 (parênteses forçam a soma primeiro)
# Sem os parênteses, a conta não é o que você esperava
```

## Por que Python funciona assim?
Python segue a precedência matemática padrão (PEMDAS) pra ser intuitivo pra quem vem da matemática. O type hint (`: int`) é só documentação — o Python não obriga, mas ferramentas como mypy usam pra pegar erros. A divisão `/` sempre retorna float porque perder a parte decimal silenciosamente causaria bugs em cálculos científicos.

## Conexões
- Você já usou esse padrão quando: definiu `contador = 0` num loop — variável guardando estado
- Aparece também em: listas — `[1, 2] * 3` gera `[1, 2, 1, 2, 1, 2]`, mesma lógica de repetição
- Diferente de: `+=` (atribuição aumentada) — `x += 1` é atalho pra `x = x + 1`, mas não é um operador aritmético novo

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `/` e `//` na divisão? Dê um exemplo numérico.
2. Escreva um código que calcula a área de um círculo dado o raio (use `pi = 3.14159` e `**`).
3. Por que `10 / 2` retorna `5.0` e não `5`?

---

**Frase-âncora:** "Variável nomeia o dado, operador transforma — juntos resolvem contas do mundo real."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
