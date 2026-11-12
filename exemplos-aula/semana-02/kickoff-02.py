"""
Preciso que a api de controle de gastos seja capaz de adicionar um dicionario{} em uma lista[] de gastos no formato:
[{"descricao": str, "valor_centavos": int, "categoria": str}]
para um gasto ser aceito o "valor_centavos" deve ser um inteiro positivo, caso não for, retornar uma mensagem de erro
para o usuario.

Preciso que a api de controle de gastos me retorne o total por categoria de cada gasto no formato:
{"categoria1": valor_total, "categoria2": valor_total}

Preciso que a api de controle de gastos me retorne o total geral de todos os gastos.
"""