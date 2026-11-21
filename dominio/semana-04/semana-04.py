"""
#1.
git clone http://github.com/gpinheiro07/exemplo-semana-04
cd exemplo-semana-04/dados
cp gastos-jan.txt gastos-jan.bak
cd ..
mkdir backup
mv dados/gastos-jan.bak backup/
ls backup # gastos-jan.bak
ls dados # gastos-fev.txt gastos-jan.txt

#2.
grep -rn "TODO" app/
# app/calculo.py:2: # TODO: tratar a lista vazia
# app/exportar.py:2: # TODO: incluir a categoria na exportação
grep -rin "uber" dados/
# dados/gastos-fev.txt:2:2026-02-15;uber aeroporto;5600
# dados/gastos-jan.txt:1:2026-01-06;Uber para o trabalho;2340
# dados/gastos-jan.txt:3:2026-01-20;UBER volta;1980

#3.
./relatorio.sh 
# bash: ./relatorio.sh: Permission denied
ls -l relatorio.sh 
# -rw-r--r-- ... relatorio.sh
chmod +x relatorio.sh
./relatorio.sh 
# Arquivos de dados: gastos-fev.txt gastos-jan.txt

#4.
KeyError (bugs.py, linha 18) -> Correção: gasto["valor_centavos"]

Valor padrão para objetos mutaveis  (bugs.py, linha 1)-> Correcão:
def registrar(gasto: dict, lista: list[dict] | None = None) -> list[dict]:
    if not lista:
        lista = []
    lista.append(gasto)
    return lista

Redefinindo variavel total dentro de cada iteração do for (bugs.py, linha 10) -> Correção:
def total_da_categoria(gastos: list[dict], categoria: str) -> int:
    total = 0
    for gasto in gastos:
        if gasto["categoria"] == categoria:
            total += gasto["valor_centavos"]
    
    return total
"""