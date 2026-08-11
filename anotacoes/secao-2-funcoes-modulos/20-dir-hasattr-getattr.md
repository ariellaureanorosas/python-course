# dir, hasattr e getattr (Introspecção)

## Quando você vai usar isso?
Quando você quer descobrir o que um objeto sabe fazer sem abrir a documentação: `dir()` lista os métodos; `hasattr()` pergunta "tem isso?"; `getattr()` busca o atributo pelo NOME (que pode ser uma string vinda de input, config ou dados). É a base de frameworks, ORMs, serialização dinâmica e forms que preenchem campos por nome.

## Modelo mental
`dir` é o olhar geral na vitrine (lista tudo). `hasattr` é tocar o vidro da vitrine perguntando "tem esse item?". `getattr` é o braço que PEGA o item pelo nome — e como o nome é uma string, o braço pode ser programado.

## Em uma linha
`dir(obj)` lista os atributos; `hasattr(obj, nome)` devolve bool; `getattr(obj, nome, padrao)` devolve o atributo ou o padrão.

## Na prática

### Caso simples — inspecionar uma string (aula 91)

```python
texto = "Ariel"
metodo = "upper"

if hasattr(texto, metodo):        # ← True — string tem o método upper?
    print(getattr(texto, metodo)())  # ← "ARIEL" — pega o método e CHAMA
else:
    print("não existe o método", metodo)
```

### Com variação — getattr com padrão (evita o hasattr duplicado)

```python
cor = getattr(objeto, "cor", "preta")
# ← se objeto não tem atributo cor, devolve "preta" — sem levantar erro
# hasattr + getattr fariam isso em dois passos; o padrão faz em um.

dir("abc")
# ← ['__add__', '__class__', ..., 'upper', ...] — TODOS os atributos
# de uma string, incluindo os internos com __ (dunder)
```

### Em uso real — chamar método por nome vindo do usuário

```python
def aplicar_transformacao(texto: str, nome_metodo: str) -> str:
    metodo = getattr(texto, nome_metodo, None)
    if metodo is None or not callable(metodo):
        return "método inválido"
    return metodo()

aplicar_transformacao("olá", "upper")  # ← 'OLÁ'
aplicar_transformacao("olá", "inexistente")  # ← 'método inválido'
```

## O que NÃO fazer

```python
# ← ERRADO: getattr sem padrão quando o atributo pode não existir
atributo = getattr(objeto, "não_existe")   # ← AttributeError!
atributo = getattr(objeto, "não_existe", None)  # ← correto

# ← CUIDADO: dir() mostra também privados e dunders — filtrar com
# [a for a in dir(obj) if not a.startswith("_")] para uso humano

# ← CUIDADO: getattr devolve o método SEM chamar; esquecer os
# parênteses devolve o objeto função, não o resultado
```

## Por que Python funciona assim?
Tudo em Python é objeto, e objetos guardam seus atributos em `__dict__` (nota da POO, Seção 3). `dir()` percorre essa cadeia de atributos (incluindo herança); `hasattr` faz `getattr` e captura o AttributeError; `getattr` resolve o nome em tempo de execução — o que permite código genérico: em vez de `if x == "upper": texto.upper()`, você escreve `getattr(texto, x)()`. Por isso frameworks web mapeiam campos de formulário para atributos do modelo usando o NOME do campo como string.

## Conexões
- Você já usou esse padrão quando: chamou `split` e `join` direto — sem saber, o "ponto" de `texto.split` é um getattr implícito
- Aparece também em: Django serializers, ORMs, argparse, testes com mock, geradores de documentação
- Diferente de: `dir` com argumento (lista do objeto) vs `dir()` sem (lista do escopo atual); `setattr` (o inverso — define) e `vars(obj)` (só `__dict__`, sem herança)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre hasattr e getattr? E como o padrão do getattr evita o hasattr?
2. O que `getattr(texto, "upper")` devolve — string ou função? O que falta para chamá-la?
3. Escreva um código que chama um método digitado pelo usuário, com mensagem de erro se não existir.

---

**Frase-âncora:** "dir mostra, hasattr confirma, getattr pega pelo nome."
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14