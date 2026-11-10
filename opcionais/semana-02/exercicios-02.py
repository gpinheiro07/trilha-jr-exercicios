gastos = [
    {"descricao": "Uber para o trabalho", "valor_centavos": 2340,
    "categoria": "transporte"},
    {"descricao": "Almoço", "valor_centavos": 3550, "categoria":
    "alimentação"},
    {"descricao": "UBER volta", "valor_centavos": 1980, "categoria":
    "transporte"},
    {"descricao": "Cinema", "valor_centavos": 3000, "categoria": "lazer"},
]


# 4.
def maior_gasto(gastos: list[dict]) -> dict | None:
    maior = None
    for gasto in gastos:
        if maior is None or gasto["valor_centavos"] > maior["valor_centavos"]:
            maior = gasto
    return maior

#5.
print(sorted(set([gasto["categoria"] for gasto in gastos])))
