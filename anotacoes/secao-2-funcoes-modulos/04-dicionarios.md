# Dicionários (`dict`)

## Quando você vai usar isso?
Quando precisa buscar um valor por uma chave — como um catálogo telefônico onde você acha o número pelo nome. Ideal para dados com labels (campos) em vez de posições numéricas.

## Modelo mental
Um fichário de gavetas: cada chave é o nome da gaveta, você puxa direto pelo nome sem precisar revirar nada.

## Em uma linha
Coleção mutável que mapeia chaves únicas e imutáveis a valores quaisquer com acesso O(1).

## Na prática

### Caso simples
```python
usuario = {"nome": "João", "idade": 30}
# ← chaves: "nome", "idade"; valores: "João", 30
usuario["email"] = "joao@email.com"
# ← se a chave existe, atualiza; se não, cria (adiciona ou altera)
print(usuario.get("nome"))
# ← .get() retorna None se a chave não existir (sem levantar KeyError)
print(usuario.get("cargo", "indefinido"))
# ← .get() com valor padrão caso a chave não exista
```

### Com variação
```python
for chave in usuario:
    print(chave, usuario[chave])
    # ← itera sobre as chaves; cada acesso é O(1)

for chave, valor in usuario.items():
    print(chave, valor)
    # ← .items() devolve tuplas evita acesso extra ao dict

del usuario["idade"]
# ← remove a chave; KeyError se a chave não existir
```

### Em uso real
```python
def agrupa_por_cargo(usuarios):
    grupos = {}
    for u in usuarios:
        # ← setdefault: se "cargo" não existe como chave, define com []
        grupos.setdefault(u["cargo"], []).append(u["nome"])
    return grupos

time = [{"nome": "Ana", "cargo": "dev"}, {"nome": "Bob", "cargo": "dev"}]
# agrupa_por_cargo(time) → {"dev": ["Ana", "Bob"]}
```

## O que NÃO fazer
```python
usuario = {"nome": "João"}
chaves_lista = {[1, 2]: "valor"}
# ← ERRO: listas são mutáveis → não são hashable → não podem ser chave
chaves_tupla = {(1, 2): "valor"}
# ← OK: tupla é imutável, hash é estável
```
A chave precisa ser imutável porque o hash (índice interno) é calculado no momento da inserção. Se o objeto mudar, o hash muda e Python não encontra o valor.

## Por que Python funciona assim?
Internamente, `dict` usa uma tabela hash (sparse array). A chave passa por `hash()`, o resultado vira um índice, e o par (hash, chave, valor) é armazenado lá. Acesso é O(1) médio. Quando a ocupação passa de ~2/3, Python realoca e rehash tudo. Desde Python 3.7, a ordem de inserção é preservada como característica da linguagem.

## Conexões
- Você já usou esse padrão quando: trabalhou com JSON (que vira dict nativo no Python `json.load`)
- Aparece também em: `**kwargs` (coleta argumentos nomeados em dict), `collections.Counter` (dict de contagens), `defaultdict` (dict com valor padrão automático)
- Diferente de: listas (acessam por índice numérico, não por chave), sets (só chaves sem valores associados), `NamedTuple` (imutável, campos fixos)

---

## Teste de recuperação — responda sem olhar para cima

1. Por que listas podem ser chave de dict, mas tuplas sim? Qual propriedade está por trás disso?
2. Escreva o código que acessa `"cargo"` do dict `usuario` e retorna `"não definido"` se a chave não existir.
3. Qual a diferença entre `d["chave"]` e `d.get("chave")`?

---

**Frase-âncora:** Mapa chave-valor com acesso instantâneo e chaves únicas e imutáveis.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14
