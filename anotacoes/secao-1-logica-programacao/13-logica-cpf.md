# Lógica de Validação de CPF

Estrutura: `XXX.XXX.XXX-DD` (9 dígitos + 2 dígitos verificadores)

## 1º Dígito Verificador

```python
cpf = "746824890"  # 9 dígitos
soma = 0
for i in range(9):
    soma += int(cpf[i]) * (10 - i)
resto = (soma * 10) % 11
digito1 = 0 if resto > 9 else resto
```

## 2º Dígito Verificador

```python
cpf_10 = cpf + str(digito1)
soma = 0
for i in range(10):
    soma += int(cpf_10[i]) * (11 - i)
resto = (soma * 10) % 11
digito2 = 0 if resto > 9 else resto
```

## CPF Completo

```python
cpf_gerado = cpf + str(digito1) + str(digito2)
cpf_valido = cpf_gerado == cpf_enviado
```

## Validar Sequência

```python
if cpf == cpf[0] * len(cpf):
    print("CPF inválido (sequência)")
```

## Limpar Formatação

```python
import re
cpf_limpo = re.sub(r"[^0-9]", "", cpf_formatado)
```
