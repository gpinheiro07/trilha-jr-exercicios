from collections import Counter


gastos = [
    {"descricao": "Uber para o trabalho", "valor_centavos": 2340,
    "categoria": "transporte"},
    {"descricao": "Almoço", "valor_centavos": 3550, "categoria":
    "alimentação"},
    {"descricao": "UBER volta", "valor_centavos": 1980, "categoria":
    "transporte"},
    {"descricao": "Cinema", "valor_centavos": 3000, "categoria": "lazer"},
]


# 1.
categorias = ["alimentação", "transporte", "alimentação", "lazer", "alimentação"]
contagem = {}
for categoria in categorias:
    contagem[categoria] = contagem.get(categoria, 0) + 1
print(contagem)

# 1. (collections.Counter)
contagem = Counter(categorias)
print(contagem)

# 2.
gasto_uber = [gasto for gasto in gastos if "uber" in gasto["descricao"].lower()]
print(len(gasto_uber))

#3. 
def para_centavos(texto: str) -> int:
    erro = f"Valor inválido: '{texto}'. Use o formato 12 ou 12,50."
    partes = texto.split(",")
    if len(partes) == 1:
        reais, centavos = partes[0], "00"
    elif len(partes) == 2 and len(partes[1]) == 2:
        reais, centavos = partes
    else:
        raise ValueError(erro)
    if not reais.isdigit() and centavos.isdigit():
        raise ValueError(erro)
    return int(reais) * 100 + int(centavos)

for texto in ["12,50", "7", "0,99", "doze", "12,5", "12.50", "-3,00"]:
    try:
        print(texto, "->", para_centavos(texto))
    except ValueError as erro:
        print(texto, "->", erro)
