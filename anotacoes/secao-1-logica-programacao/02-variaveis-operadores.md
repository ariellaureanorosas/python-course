# Variáveis e Operadores

## Variáveis (PEP 8)
```python
nome_completo: str = "João Silva"  # snake_case + type hint
idade: int = 30
altura: float = 1.75
maior_de_idade: bool = idade >= 18
```

## Operadores Aritméticos
```python
+   # adição
-   # subtração
*   # multiplicação
/   # divisão (float)
//  # divisão inteira
**  # exponenciação
%   # módulo (resto da divisão)
```

## Precedência
1. `( )` parênteses
2. `**` exponenciação
3. `*`, `/`, `//`, `%`
4. `+`, `-`

## Concatenação e Repetição
```python
"a" + "b" + "c"   # "abc"
"A" * 10          # "AAAAAAAAAA"
"Oi\n" * 3        # "Oi\nOi\nOi\n"
```

## Exemplo: Cálculo de IMC
```python
peso = 80
altura = 1.75
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")
```
