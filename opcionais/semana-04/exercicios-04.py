#7.
#8.
import argparse
import logging
import os


logger = logging.getLogger(__name__)


def formatar_reais(valor_centavos: int) -> str:
    reais, centavos = divmod(valor_centavos, 100)
    return f"R$ {reais}, {centavos:02d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Divide um gasto entre pessoas")
    parser.add_argument("valor_centavos", type=int, help="valor total em centavos")
    parser.add_argument("--pessoas", type=int, default=1, help="quantas pessoas dividem; padrão: 1")
    args = parser.parse_args()
    logger.debug(f"Valor {args.valor_centavos}, pessoas {args.pessoas}")
    if args.pessoas <= 0:
        parser.error("O número de pessoas precisa ser positivo.")
    por_pessoa = args.valor_centavos // args.pessoas
    print(f"{formatar_reais(por_pessoa)} por pessoa")


if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOG_LEVEL", "WARNING"))
    main()
