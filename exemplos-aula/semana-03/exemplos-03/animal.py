from dataclasses import dataclass
from datetime import date


@dataclass
class Animal:
    nome: str
    acao_gerundio: str

    def fazer_acao(self, data: date) -> None:
        print(f"{data}: {self.nome} esta {self.acao_gerundio}")
