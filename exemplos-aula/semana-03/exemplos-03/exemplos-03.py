from dataclasses import dataclass
from datetime import date


# Classes
class Categoria:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def gasto_categoria(self) -> str:
        return (f"Usou dinheiro para {self.nome}")

categoria_transporte = Categoria(nome="transporte")
categoria_lazer = Categoria(nome="lazer")

print(categoria_transporte.gasto_categoria())
print(categoria_lazer.gasto_categoria())


# Dataclasses
class Pessoa:
    def __init__(
            self,
            nome: str,
            sobrenome: str,
            telefone: int,
            email: str,
            documento: str,
            altura: int,
            peso: int,
            senha: str,
            signo: str,
            time: str,
            bolsonarista: bool = False,
            sabe_fazer_churrasco: bool = False,
            media_de_gols: float = 0.0
        ):
            self.nome = nome
            self.sobrenome = sobrenome
            self.telefone = telefone
            self.email = email
            self.documento = documento
            self.altura = altura
            self.peso = peso
            self.senha = senha
            self.signo = signo
            self.time = time
            self.bolsonarista = bolsonarista
            self.sabe_fazer_churrasco = sabe_fazer_churrasco
            self.media_de_gols = media_de_gols

@dataclass
class PessoaDataclass:
    nome: str
    sobrenome: str
    telefone: int
    email: str
    documento: str
    altura: int
    peso: int
    senha: str
    signo: str
    time: str
    bolsonarista: bool = False
    sabe_fazer_churrasco: bool = False
    media_de_gols: float = 0.0


pessoa_sem_dataclass = Pessoa(
     nome="Gabriel",
     sobrenome="Pinheiro",
     telefone="1999999999",
     email="email@email.com.br",
     documento="111.111.111-11",
     altura="1.40",
     peso="70",
     senha="1234",
     signo="escorpiao",
     time="palmeiras"
)
pessoa_dataclass = PessoaDataclass(
     nome="Gabriel",
     sobrenome="Pinheiro",
     telefone="1999999999",
     email="email@email.com.br",
     documento="111.111.111-11",
     altura="1.40",
     peso="70",
     senha="1234",
     signo="escorpiao",
     time="palmeiras"
)


# __post_init__ (somente dataclasses)
@dataclass
class Animal:
     nome: str

     def __post_init__(self) -> None:
          if self.nome.strip() == "":
               raise ValueError("Insira um nome válido")

try:
    sem_nome = Animal("    ")   
except ValueError as e:
     print(e)

# Módulos e pacotes (exemplo main.py)

# Como ler código (exemplo de algum código do git hub)
