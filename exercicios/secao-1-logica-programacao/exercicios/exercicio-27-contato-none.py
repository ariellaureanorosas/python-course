"""
EXERCÍCIO 27 — None e o operador is

Tópicos: None, is, is not, flag de validação

Um cadastro de contatos tem telefone OPCIONAL. Quando o campo vem
vazio, o valor correto é None (dado ausente), não uma string vazia:

  - Receba o NOME e o TELEFONE do usuário. Se o telefone vier em
    branco (string vazia após .strip()), atribua None a ele.
  - Exiba "Nome: {nome}".
  - Para o telefone, use `telefone is None`: se for None, exiba
    "Telefone: não informado"; senão, exiba "Telefone: {telefone}".
  - Crie a flag contato_completo = telefone is not None e exiba
    "Cadastro completo." quando True, "Complete o cadastro." quando
    False.

Exemplo de saída esperada (nome: "Ana", telefone em branco):
Nome: Ana
Telefone: não informado
Complete o cadastro.

Dica: use `telefone is None` (e não `== None`) — comparação de
identidade é o padrão para None, e None é único.

Use seu próprio raciocínio — o gabarito não precisa ser igual,
apenas estar correto.
"""

# ========== ESCREVA SEU CÓDIGO A PARTIR DAQUI ==========