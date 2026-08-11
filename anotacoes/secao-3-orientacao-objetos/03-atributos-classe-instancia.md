# Atributos de classe vs atributos de instância

## Quando você vai usar isso?
Quando existe um valor que é VERDADE para a classe inteira — o ano atual, o nome da escola, o imposto padrão — você não precisa repeti-lo em todo objeto. Ele fica na classe (uma cópia só) e todas as instâncias enxergam. Já os dados próprios de cada objeto (nome, idade) ficam por instância.

## Modelo mental
Atributo de classe é a regra do prédio afixada no quadro de avisos: uma única folha, todo morador lê a mesma. Atributo de instância é o armário pessoal de cada morador: cada um tem o próprio. Se alguém cola um bilhete novo de "regra do prédio", todos leem a mudança — mexer no próprio armário só muda a vida de quem mexeu.

## Em uma linha
Atributo de classe é compartilhado por todas as instâncias (e criado no corpo da classe); atributo de instância é exclusivo de cada objeto (e criado dentro do `__init__` com `self`).

## Na prática

### Caso simples
```python
class Aluno:
    escola = 'Escola Python'     # ← atributo de CLASSE (fora do __init__)
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome         # ← atributo de INSTÂNCIA
        self.idade = idade

    def ano_nascimento(self):
        return Aluno.ano_atual - self.idade  # ← acesso pela classe

aluno = Aluno('Ana', 20)
print(aluno.escola)              # ← 'Escola Python' (herdado da classe)
print(aluno.ano_nascimento())    # ← 2006
```

### Com variação
```python
# ← introspecção: vars() e __dict__ mostram o armário do OBJETO
p1 = Aluno('Ana', 20)
p2 = Aluno('Bia', 22)
print(vars(p1))        # ← {'nome': 'Ana', 'idade': 20}  (não tem escola!)
print(p1.__dict__)     # ← idem — é o mesmo dicionário
print(Aluno.__dict__)  # ← na classe: 'escola', 'ano_atual' e os métodos

# ← expandindo um dicionário na criação: Pessoa(**dados)
dados = {'nome': 'Carlos', 'idade': 35}
p3 = Aluno(**dados)    # ← Aluno(nome='Carlos', idade=35)
```

### Em uso real
```python
class Pedido:
    imposto_padrao = 0.1               # ← regra do negócio, única para todos

    def __init__(self, valor):
        self.valor = valor

    def total_com_imposto(self):
        return self.valor * (1 + Pedido.imposto_padrao)

# ← se a regra mudar, muda em UM lugar e todos os pedidos atualizam
Pedido.imposto_padrao = 0.12
print(Pedido(100.0).total_com_imposto())  # ← 112.0
```

## O que NÃO fazer
```python
# ← ERRADO: lista MUTÁVEL como atributo de classe e alterada pela instância
class Carrinho:
    itens = []                 # ← perigo: UMA lista para todos!

c1 = Carrinho()
c2 = Carrinho()
c1.itens.append('Camiseta')    # ← coloca na lista da CLASSE
print(c2.itens)                # ← ['Camiseta'] — vazamento entre objetos!

# ← o certo: criar a lista no __init__ (self.itens = []) ou usar
# ← default_factory em dataclasses (aula 175)

# ← ERRADO: acessar atributo de classe via self quando for mudar
def trocar_escola(self, nova):
    self.escola = nova         # ← cria um atributo SÓ NESTE objeto
# ← a classe continua com a antiga; use Aluno.escola = nova
```

## Por que Python funciona assim?
Ao ler `objeto.atributo`, Python busca primeiro no `__dict__` da instância; se não achar, sobe para a classe (e depois para a hierarquia, via MRO — aula 149). Por isso `p1.escola` funciona sem a instância ter `escola`: a busca cai na classe. O problema do "vazamento" da lista mutável acontece porque escrever em `c1.itens` usa a LISTA da classe — mas ATRIBUIR `c1.itens = [...]` criaria um armário próprio. Ler sobe, escrever/alterar é mais sutil: `c1.itens.append()` muta o objeto compartilhado; `c1.itens = []` cria um novo local.

## Conexões
- Você já usou esse padrão quando: definiu uma constante `ANO_ATUAL = 2026` no topo do módulo — o atributo de classe é a versão "dentro da classe"
- Aparece também em: `ClassVar` em dataclasses, `Enum` (membros são atributos de classe), Django `objects = Manager()`
- Diferente de: atributo de instância (exclusivo), variável local de método (morre no fim), propriedade de classe com `@classmethod` (recebe `cls` e enxerga a classe — próxima nota)

---

## Teste de recuperação — responda sem olhar para cima

1. Onde nasce um atributo de classe e onde nasce um atributo de instância?
2. Escreva uma classe `Config` com `versao = 1.0` na classe e método que a retorna.
3. Por que `lista = []` na classe é perigoso, mas `self.lista = []` no `__init__` é seguro?

---

**Frase-âncora:** Na classe fica o que é verdade para todos; na instância, o que é próprio de cada um; o `vars()` abre o armário e mostra a diferença.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14