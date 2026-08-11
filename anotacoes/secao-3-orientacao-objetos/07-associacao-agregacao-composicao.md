# Associação, agregação e composição

## Quando você vai usar isso?
Assim que duas ou mais classes conversam entre si, você precisa decidir COMO elas se relacionam: uma apenas usa a outra (associação), uma contém várias partes que vivem sozinhas (agregação) ou uma cria a parte que não sobrevive sem ela (composição). Essa escolha define quem é dono de quem e quem apaga quem.

## Modelo mental
- Associação: você usa um táxi — o táxi não é seu, ele vive sem você. Os dois se conhecem só no momento do uso.
- Agregação: sua caixa de ferramentas contém ferramentas — mas as ferramentas existem na loja mesmo fora da caixa.
- Composição: seu coração nasceu dentro de você, morre com você — ninguém empresta um coração de outra pessoa para você.

## Em uma linha
Associação: referência temporária entre objetos independentes; agregação: o todo contém partes que existem fora dele; composição: a parte nasce dentro do dono e morre com ele.

## Na prática

### Caso simples (associação)
```python
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def escrever(self):
        return f'{self.nome} está escrevendo'

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None          # ← começa sem ferramenta

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):                 # ← associação: referencia outro objeto
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

caneta = FerramentaDeEscrever('Caneta Bic')   # ← caneta existe SOZINHA
escritor = Escritor('Machado de Assis')
escritor.ferramenta = caneta                  # ← liga os dois só aqui
```

### Com variação (agregação)
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []               # ← contém PARTES

    def adicionar(self, produto):
        self._produtos.append(produto)

camiseta = Produto('Camiseta', 49.90)     # ← vive fora do carrinho
carrinho = CarrinhoDeCompras()
carrinho.adicionar(camiseta)              # ← entra na relação
# ← se o carrinho sumir, a camiseta continua existindo na loja
```

### Em uso real (composição)
```python
class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

class Cliente:
    def __init__(self, nome, rua, numero, cidade):
        self.nome = nome
        self.endereco = Endereco(rua, numero, cidade)  # ← nasce DENTRO

cliente = Cliente('Maria', 'Rua das Flores', 123, 'São Paulo')
print(cliente.endereco.rua)   # ← 'Rua das Flores'
# ← NUNCA recebe um endereço pronto: o Cliente fabrica o próprio.
# ← dois Clientes têm dois endereços distintos — nunca compartilhados.
```

## O que NÃO fazer
```python
# ← ERRADO: composição que recebe a parte pronta (vira associação)
class Cliente:
    def __init__(self, nome, endereco):   # ← recebe de fora
        self.endereco = endereco
# ← na composição o dono CRIA a parte; recebê-la é outra relação

# ← ERRADO: agregação expondo a lista interna direto
class Carrinho:
    def __init__(self):
        self.produtos = []                # ← qualquer um faz lista.clear()
# ← o certo: _produtos + métodos adicionar/remover + cópia em listar()

# ← CUIDADO: confundir os graus — "cliente tem endereço" quase sempre é
# ← composição; "pedido tem produtos" (repetido entre pedidos) é agregação
# ← a pergunta que decide: a parte faz sentido SOZINHA?
```

## Por que Python funciona assim?
Python não tem palavras-chave para essas relações (diferente de UML/Java): elas são DECISÕES de código. Composição é simplesmente criar o objeto no `__init__` do dono; associação é guardar uma referência que vem de fora; agregação é guardar referências numa coleção privada. O ciclo de vida é definido por quem detém a referência: sem `__del__` garantido (Python tem GC), a regra prática é "se ninguém mais referencia a parte, ela morre com o dono" — por isso a composição costuma ser a mais segura: o dono é a única fonte da parte.

## Conexões
- Você já usou esse padrão quando: fez `lista = []` dentro de uma classe (agregação), recebeu um objeto pronto no `__init__` (associação), criou objeto em função que retorna outra (composição)
- Aparece também em: Django ForeignKey (agregação) e OneToOne (composição típica), SQLAlchemy relationships, ORMs em geral
- Diferente de: herança ("é um" — 08-heranca-super), composição × herança (a composição é preferida para reuso — "tem um" em vez de "é um" cego)

---

## Teste de recuperação — responda sem olhar para cima

1. Qual pergunta decide se uma relação é agregação ou composição?
2. Escreva associação entre `Aluno` e `Professor` (o aluno referencia o professor, os dois existem sozinhos).
3. Por que na composição o dono cria a parte dentro do `__init__` e não recebe pronta?

---

**Frase-âncora:** Usa é associação, contém partes que vivem fora é agregação, cria dentro e morre junto é composição.
**Nível:** Intermediário
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14