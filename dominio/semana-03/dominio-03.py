from dataclasses import dataclass


#1.
@dataclass
class ContaBancaria:
    titular: str
    saldo_centavos: int = 0

    def __post_init__(self) -> None:
        if self.titular.strip() == "":
            raise ValueError("O titular deve ser um nome válido")
        if not isinstance(self.saldo_centavos, int) or self.saldo_centavos < 0:
            raise ValueError("O saldo deve ser um valor inteiro e positivo")

    #2.
    def depositar(self, valor_centavos: int) -> None:
        if isinstance(valor_centavos, int) and valor_centavos >= 0:
            self.saldo_centavos += valor_centavos
        raise ValueError("O deposito deve ser um inteiro positivo")

    def sacar(self, valor_centavos: int) -> None:
        if not isinstance(valor_centavos, int) and valor_centavos < 0:
            raise ValueError("O saque deve ser um inteiro positivo")
        if self.saldo_centavos - valor_centavos < 0:
            raise ValueError("Saldo insuficiente")
        self.saldo_centavos -= valor_centavos
