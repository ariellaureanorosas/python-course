# datetime — Trabalhando com Datas e Horas

## Quando você vai usar isso?
Sempre que o problema envolver tempo real: calcular idade a partir de uma data de nascimento, descobrir a diferença entre dois eventos, gerar um timestamp para log, agendar tarefas (amanhã, próximo mês). `time` serve para medir performances e pausas; `datetime` é a ferramenta para representar e calcular datas civis.

## Modelo mental
Datas são números com calendário por cima. `datetime` tem três relógios: `date` (dia/mês/ano), `time` (hora/minuto/segundo) e `datetime` (os dois juntos). `timedelta` é a régua que soma/subtrai dias — e o Python cuida sozinho de viradas de mês, fevereiro e anos bissextos.

## Em uma linha
`datetime` representa instantes e datas; `timedelta` faz aritmética entre eles; `strftime`/`strptime` convertem entre objeto e texto.

## Na prática

### Caso simples

```python
from datetime import datetime, date, timedelta

# datetime atual (data + hora)
agora = datetime.now()
print(agora)            # 2025-06-22 14:31:05.123456

# date atual (so dia/mes/ano)
hoje = date.today()

# timedelta: deslocar no tempo
depois = hoje + timedelta(days=7)   # 7 dias para frente
depois = hoje + timedelta(weeks=2)  # tambem aceita semanas
```

### Com variação

```python
from datetime import datetime

# strftime: objeto -> texto (formatar para exibir)
now = datetime.now()
print(now.strftime('%d/%m/%Y %H:%M'))     # 22/06/2025 14:31

# strptime: texto -> objeto (parsear entrada do usuario)
data = datetime.strptime('22/06/2025', '%d/%m/%Y')

# diferenca entre duas datas -> timedelta
nascimento = datetime(1990, 5, 10)
idade = now - nascimento
print(idade.days // 365)   # anos aproximados
```

### Em uso real

```python
from datetime import datetime, timedelta
import time

# apagar logs antigos: comparacao de datas real
limite = datetime.now() - timedelta(days=30)
print(f'apagando logs anteriores a {limite:%Y-%m-%d}')

# medir tempo de execucao: time.perf_counter() conta segundos
inicio = time.perf_counter()
# ... bloco caro ...
fim = time.perf_counter()
print(f'levou {fim - inicio:.3f} s')
```

## O que NÃO fazer

```python
# NUNCA some dias manualmente com matematica de calendario
# (hoje.month + 1) vira 31/02 se hoje for 31/01 — data inexistente.
# Use timedelta ou date.replace() com cuidado.

# NUNCA compare textos de data
# '2025-06-22' > '2025-01-01' so funciona com formato ISO;
# com '22/06/2025' a comparacao de texto erra.
# Converta com strptime antes de comparar.
```

## Por que Python funciona assim?
Datas são um problema clássico de caso de borda: meses têm tamanhos diferentes, anos bissextos existem, fusos horários mudam. O Python encapsula toda essa complexidade em `datetime`/`timedelta` para você pensar na pergunta (somar 30 dias?) e não em quantos dias tem fevereiro. O objeto é imutável — `now + timedelta(days=1)` cria um novo objeto, não altera o original.

## Conexões

- Você já usou esse padrão quando: comparou strings de entrada do usuário e viu o erro de formato — `strptime` é a ponte entre texto e dados estruturados.
- Isso se conecta com: `time` (`perf_counter` para medir), `calendar` (meses e semanas), e bibliotecas avançadas como `pendulum`/`dateutil` quando `datetime` não basta.
- Isso te prepara para: timestamps em APIs REST (ISO 8601), ORMs como SQLAlchemy que mapeiam colunas de data, e agendadores como APScheduler.

---

## Teste de recuperação — responda sem olhar para cima

1. Qual a diferença entre `date`, `datetime` e `timedelta`?
2. Como você transforma '25/12/2025' (texto) em um objeto `datetime`?
3. O que acontece se você somar `timedelta(days=1)` a `2025-12-31`?

---

**Frase-âncora:** *Datas são números com calendário por cima — deixe o Python fazer a matemática.*
**Nível:** Intermediário
**Revisão sugerida:** 30 dias