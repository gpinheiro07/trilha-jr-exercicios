from datetime import date


#3.
def mais_recente(textos: list[str]) -> date:
    datas = [date.fromisoformat(texto) for texto in textos]
    maior = datas[0]
    for data in datas:
        if data > maior:
            maior = data
    return maior


#4.
def resumir_mes(gastos: list[dict], hoje: date | None = None) -> dict[str, int]:
    if hoje is None:
        hoje = date.today()
    resumo: dict[str, int] = {}
    for gasto in gastos:
        if gasto["data"].year == hoje.year and gasto["data"].month == hoje.month:
            categoria = gasto["categoria"]
            resumo[categoria] = resumo.get(categoria, 0) + gasto["valor_centavos"]
    return resumo
"""
A função recebe uma lista de dicionários com as chaves data (um date ), categoria e valor_centavos , 
e uma data opcional, hoje.
Ela devolve um dicionário com o total em centavos de cada categoria, só com os gastos do mesmo mês e
ano de hoje . Sem hoje, a função usa a data do dia em que roda.
"""

#5.
"""
módulo é um arquivo .py e um pacote é uma pasta de módulos com __init__.py . O projeto roda da raiz porque o Python procura o pacote
gastos a partir da pasta do programa executado.
"""
