# Operadores Lógicos

## Quando você vai usar isso?
Um acesso só é liberado se o usuário for admin E a senha estiver correta. Um desconto só vale se o cliente for VIP OU tiver mais de 60 anos. Um campo é obrigatório se NÃO estiver vazio. Operadores lógicos combinam condições simples em decisões compostas.

## Modelo mental
and é uma catraca de dois estágios: só passa se os dois portões estiverem abertos. or é uma porta com duas maçanetas: qualquer uma abre. not é um interruptor invertido: acende quando você desliga, apaga quando você liga.

## Em uma linha
and exige todas True, or basta uma True, not inverte o valor, in verifica pertencimento, e curto-circuito otimiza a avaliação.

## Na prática

### Caso simples
```python
# and — todas as condições precisam ser True para o bloco executar
if usuario == "admin" and senha == "123":   # ← se uma for False, o bloco não executa
    print("Login autorizado")

# or — qualquer condição True já basta
if idade < 18 or altura < 1.50:            # ← se qualquer uma for True, entra no bloco
    print("Não pode entrar")

# not — inverte o valor lógico (True vira False, False vira True)
if not senha:                               # ← not True = False, not False = True
    print("Senha vazia!")                    # ← executa se senha for vazia (falsy)
```

### Com variação
```python
# in / not in — verifica se um valor pertence a uma sequência (string, lista, tupla, etc.)
if "a" in nome:              # ← percorre a string nome e retorna True se encontrar "a"
    print("Tem letra 'a'")
if "z" not in nome:          # ← True se "z" NÃO estiver em nenhuma posição da string
    print("Não tem letra 'z'")
```

### Em uso real
```python
# Curto-circuito e valores Falsy — Python otimiza e você usa a seu favor
# Valores Falsy: 0, 0.0, "", '', False, None, [], {}, set(), range(0)
# Qualquer outro valor é Truthy
nome = input("Nome: ") or "Sem nome"   # ← se input devolver string vazia (Falsy), usa "Sem nome"

# Curto-circuito: and para na primeira condição falsa; or para na primeira verdadeira
# Python nem avalia a segunda condição se a primeira já decide o resultado
usuario_valido = usuario == "admin" and senha_valida(banco)  # ← se usuário não for admin, nem chama senha_valida
```

## O que NÃO fazer
```python
# Encadear comparações com and desnecessariamente — Python permite encadeamento direto
if idade >= 18 and idade <= 60:   # ← funciona, mas é repetitivo
if 18 <= idade <= 60:             # ← melhor: Python encadeia operadores de comparação naturalmente
# Esquecer que or retorna o primeiro valor Truthy, não True:
resultado = 0 or "" or "final"    # ← resultado = "final" (primeiro Truthy), não True
```

## Por que Python funciona assim?
Python avalia expressões lógicas preguiçosamente (lazy evaluation / curto-circuito): pra que calcular a segunda condição se a primeira já decide o resultado? Isso é uma otimização de performance e também um recurso — como no padrão `input() or "default"`. Os valores Falsy seguem o princípio de que tipos "vazios" devem ser False por convenção, tornando o código mais idiomático.

## Conexões
- Você já usou esse padrão quando: fez `if usuario:` pra checar se usuário existe — usou Truthy/Falsy sem saber
- Aparece também em: list comprehensions — `[x for x in lista if x > 0]` usa a mesma lógica bool
- Diferente de: operador bitwise (`&`, `|`) — `and`/`or` avaliam em curto-circuito e retornam o valor, `&`/`|` operam bit a bit e sempre retornam int

---

## Teste de recuperação — responda sem olhar para cima

1. O que é curto-circuito e como `and` e `or` se comportam diferentemente?
2. Escreva um código que pergunta usuário e senha e só libera acesso se ambos forem "admin" e "123", respectivamente.
3. Explique por que `"" or "fallback"` retorna `"fallback"` e não `True`.

---

**Frase-âncora:** "and exige tudo, or aceita qualquer, not inverte — lógica pura no código."
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
