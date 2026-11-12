"""Recapitulação

Perguntas de Checagem:
1. Quais são os três estados de um arquivo no Git e que comando leva de um ao
seguinte? 

2. Por que a semana-02 precisa nascer de uma main atualizada com git pull ?

3. Numa revisão, quando escolher "Approve", "Request changes" ou "Comment"?

### Dúvidas
git update-index --skip-worktree requests.py
"""

"""Extensões VS Code:
- Python
- Material Icon Theme
"""

# O que é uma venv?
# python3 -m venv .venv


# Tipos basicos + função isinstance()
idade: int = 25  # int (inteiro)
altura: float = 1.75  # float (ponto flutuante)
nome: str = "Maria"  # str (string / texto)
ativo: bool = True  # bool (booleano)
resposta = None  # NoneType (ausência de valor)

print(isinstance(idade, int))  # True
print(isinstance(altura, str))  # False
print(isinstance(nome, (str, int)))  # True (aceita tupla de tipos)


# Problema com float (imprecisão)
preco_float = 0.1 + 0.2
print(preco_float)  # 0.30000000000000004 (Ops!)


# Solução 1: Trabalhar em centavos (inteiros)
preco_em_centavos = 10 + 20
print(f"R$ {preco_em_centavos / 100:.2f}")  # R$ 0.30

# Solução 2: Usando a biblioteca Decimal
from decimal import Decimal

preco_decimal1 = Decimal("0.1")
preco_decimal2 = Decimal("0.2")
total = preco_decimal1 + preco_decimal2
print(total)  # 0.3 (Preciso)


# Operacões com string
nome = "  Gabriel ; BEnedito ; Pinheiro     "
numero = "12,5"
print(nome.strip())
print(nome.lower())
print(nome.upper())
print(nome.replace(";", ""))
print(numero.split(","))
print(numero.isdigit())


# f-string básica
nome = "Carlos"
idade = 30
mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos."
print(mensagem)

# Expressões dentro da f-string e formatação de casas decimais
preco = 49.9
print(f"O total com 10% de desconto é R$ {round(preco * 0.9, 2)}")


#Identação e condição if
idade = 18

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")  # Executado neste caso


#Lista + operações
frutas = ["maçã", "banana", "laranja"] # índices [0, 1, 2]

frutas.append("uva")  # Adiciona ao final
frutas.insert(1, "manga")  # Insere na posição 1
print(frutas)  # ['maçã', 'manga', 'banana', 'laranja', 'uva']

removida = frutas.pop()  # Remove e retorna o último elemento ('uva')
frutas.remove("banana")  # Remove pelo valor

print(len(frutas))  # Tamanho da lista: 3
print(frutas[0])  # Acessa o primeiro elemento: 'maçã'
print(frutas[-1])  # Acessa o último elemento


# Exemplo de FOR
print("--- FOR ---")
for fruta in ["maçã", "banana", "uva"]:
    print(fruta)

# Exemplo com range() de 0 a 3
for i in range(3):
    print(i)


# Exemplo de WHILE
print("--- WHILE ---")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1


#For + If + String
for carro in ["Golf - Wolkswagen", "Corolla - Toyota", "City - Honda"]:
    if "toyota" in carro.lower():
        print("Eu achei um carro da Toyota")


#tuple (Imutável) 
# Coordenada geográfica (latitude, longitude)
coordenada = (-23.5505, -46.6333) #índices [0, 1]

# Tentativa de alteração geraria erro (TypeError):
# coordenada[0] = 0.0

# Desempacotamento de tupla
lat, lon = coordenada
print(f"Latitude: {lat}, Longitude: {lon}")


#dict + operações
usuario = {"nome": "Ana", "idade": 28, "cidade": "São Paulo"}

# Acessar e alterar valores
print(usuario["nome"])  # Ana
usuario["idade"] = 29  # Atualiza valor
usuario["email"] = "ana@email.com"  # Adiciona nova chave

# .get() evita erros se a chave não existir
print(usuario.get("telefone", "Não cadastrado"))

# Iterar sobre chaves, valores e itens
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Criar uma chave em tempo de execução
usuario = {}
categorias_endereco = ["rua", "bairro"]
for categoria in categorias_endereco:
    usuario[categoria] = "nome_teste"
print(usuario)


#set (Não permite repetição)
emails = ["a@email.com", "b@email.com", "a@email.com"]
emails_unicos = set(emails)
print(emails_unicos)  # {'b@email.com', 'a@email.com'} (duplicata removida)

# Operações de conjuntos
grupo_a = {"Ana", "Bruno", "Carlos"}
grupo_b = {"Bruno", "Daniel", "Eva"}

print(grupo_a.intersection(grupo_b))  # {'Bruno'} (quem está nos dois)
print(grupo_a.union(grupo_b))  # Todos os nomes sem repetir


#list comprehension
# Maneira tradicional
numeros = [1, 2, 3, 4, 5]
quadrados_tradicional = []
for n in numeros:
    quadrados_tradicional.append(n**2)

# Com List Comprehension: [expressao for item in iteravel if condicao]
quadrados = [n**2 for n in numeros if n % 2 != 0]
print(quadrados)  # [1, 9, 25] (apenas os ímpares ao quadrado)


#funcoes
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return round(imc, 2)

resultado = calcular_imc(70, 1.75)
print(f"Seu IMC é {resultado}")


#type hints
# Parâmetros tipados e indicação de retorno (-> str)
def saudar(nome: str, vezes: int = 1) -> str:
    return f"Olá, {nome}! " * vezes

print(saudar("Carlos", 2))


#try/except
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você precisa digitar um número válido!")
else:
    print("Executado com sucesso (sem erros).")
finally:
    print("Bloco executado sempre (com ou sem erro).")

#raise
def sacar(saldo: float, valor: float) -> float:
    if valor > saldo:
        raise ValueError(
            f"Saldo insuficiente! Saldo atual: R$ {saldo:.2f}"
        )
    return saldo - valor

try:
    novo_saldo = sacar(100.0, 150.0)
except ValueError as e:
    print(f"Erro capturado: {e}")
