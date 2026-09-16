"""
EXERCÍCIO 03 - Closure para Criar Saudação

Tópicos: closure, função que retorna função, variáveis livres

Crie a função `criar_saudacao(saudacao: str)` que:

1. Receba uma string de saudação (ex: "Olá", "Bom dia")
2. Retorne uma função `saudar(nome: str) -> str`
3. A função retornada deve concatenar a saudação + " " + nome

Comportamento esperado:
    bom_dia = criar_saudacao("Bom dia")
    bom_dia("Ariel")   # 'Bom dia Ariel'

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def criar_saudacao(saudacao: str) -> Callable[[str], str]:
    def nome_saudacao(nome: str) -> str:
        return f"{saudacao}, {nome}"

    return nome_saudacao


if __name__ == "__main__":
    bom_dia = criar_saudacao("Bom dia")
    print(bom_dia("Ariel"))
