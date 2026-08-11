# Métodos que mantêm estado (objeto com memória)

## Quando você vai usar isso?
Quando o objeto precisa LEMBRAR de coisas entre uma chamada e outra: uma câmera que sabe se está filmando, um player que sabe se está tocando, um semáforo que sabe em qual cor está. São atributos que MUDAM de valor conforme os métodos executam.

## Modelo mental
O objeto é uma pessoa com memória: você pergunta "você está filmando?" e ele consulta a própria cabeça (o atributo). A pessoa não "nasce" lembrando de tudo — o `__init__` define o estado inicial, e os métodos atualizam a memória conforme as ações acontecem.

## Em uma linha
Manter estado é usar atributos que os métodos lêem e MODIFICAM — a classe vira um pequeno sistema que responde de forma diferente dependendo do histórico de chamadas.

## Na prática

### Caso simples
```python
class Camera:
    def __init__(self, marca):
        self.marca = marca
        self.filmando = False    # ← estado inicial: desligada
        self.fotos_tiradas = 0   # ← contador começa em zero

    def filmar(self):
        if self.filmando:        # ← lê o estado
            return f'{self.marca} já está filmando'
        self.filmando = True     # ← MUDA o estado
        return f'{self.marca} começou a filmar'

    def parar_de_filmar(self):
        if not self.filmando:
            return f'{self.marca} não está filmando'
        self.filmando = False
        return f'{self.marca} parou de filmar'
```

### Com variação
```python
class Camera:
    def __init__(self, marca):
        self.marca = marca
        self.filmando = False
        self.fotos_tiradas = 0

    def fotografar(self):
        if self.filmando:        # ← regra de negócio: não fotografa filmando
            return 'Não é possível fotografar enquanto filma'
        self.fotos_tiradas += 1  # ← contador é estado que também muda
        return f'Foto {self.fotos_tiradas} capturada'

camera = Camera('Nikon')
print(camera.filmar())           # ← 'Nikon começou a filmar'
print(camera.fotografar())       # ← 'Não é possível fotografar enquanto filma'
print(camera.parar_de_filmar())  # ← 'Nikon parou de filmar'
print(camera.fotografar())       # ← 'Foto 1 capturada'
```

### Em uso real
```python
class Player:
    def __init__(self, musica_atual):
        self.musica_atual = musica_atual
        self.tocando = False

    def tocar_pausar(self):
        self.tocando = not self.tocando   # ← alterna o estado (toggle)
        return f'{self.musica_atual} {"tocando" if self.tocando else "pausada"}'
    # ← mesmo método, resposta depende do estado: isso é comportamento
    # ← de objeto, impossível de reproduzir com função pura
```

## O que NÃO fazer
```python
# ← ERRADO: método imprime em vez de retornar
def filmar(self):
    print(f'{self.marca} começou a filmar')   # ← trava testes e chamadas
# ← o certo: retornar a string e deixar quem chama decidir o print

# ← ERRADO: criar o estado "na mão" fora do __init__
def __init__(self, marca):
    self.marca = marca        # ← esqueceu de inicializar filmando por aqui
# ← depois: camera.filmando gera AttributeError no primeiro uso

# ← CUIDADO: guardar o estado em variável local do método
def filmar(self):
    filmando = True           # ← some quando o método termina!
    return 'Começou a filmar'
# ← o estado precisa ser ATRIBUTO (self.algo), não variável local
```

## Por que Python funciona assim?
Cada instância tem o próprio `__dict__` (um dicionário real de atributos, aula 136). Quando um método faz `self.filmando = True`, ele grava nesse dicionário — o atributo continua existindo entre chamadas porque o dicionário mora no objeto, não no stack da função. Funções puras não conseguem isso: elas só enxergam argumentos e morrem ao terminar. Métodos de instância, por serem ligados ao objeto via `self`, têm memória garantida por todo o ciclo de vida do objeto.

## Conexões
- Você já usou esse padrão quando: fez `contador = 0` no início do programa e um `while` alterando o contador — só que agora o estado mora no objeto
- Aparece também em: máquinas de estado, `itertools.count()`, iteradores (`__next__` guarda a posição), Django `request.user` logado ou não
- Diferente de: função com variável `global` (estado espalhado e perigoso), closure com `nonlocal` (estado escondido), atributo de classe (compartilhado por todos — próxima nota)

---

## Teste de recuperação — responda sem olhar para cima

1. Onde o estado precisa morar para sobreviver entre chamadas de método?
2. Escreva uma classe `Contador` com `incrementar()` e `zerar()`, lembrando o total a cada chamada.
3. Por que um método que retorna a mensagem é melhor que um que usa `print` direto?

---

**Frase-âncora:** Atributo que muda de valor é o estado; método que muda o atributo é a ação; objeto é a memória que liga os dois.
**Nível:** Básico
**Revisão sugerida:** amanhã → dia 3 → dia 7 → dia 14