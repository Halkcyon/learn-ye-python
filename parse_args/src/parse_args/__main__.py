from pathlib import Path

# alternative arg parsers for more complex use-cases:
# - https://pypi.org/project/click/
# - https://pypi.org/project/typer/

# https://docs.python.org/3/library/argparse.html?highlight=argparse
if __name__ == "__main__":
    import sys

    print(sys.argv)

    import argparse

    def parse_hex(v: str) -> int:
        try:
            return int(v, base=16)
        except ValueError:
            raise argparse.ArgumentTypeError("received invalid hex value")

    parser = argparse.ArgumentParser(
        prog="python -m parse_args",
        # important! defaults only display when you have `help=` defined
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("path", type=Path, help="path to a csv")
    parser.add_argument("-V", "--value", type=parse_hex, help="a hexidecimal value")
    parser.add_argument("-o", "--output", required=True)

    parser.add_argument("-f", "--flag", action="store_true")
    parser.add_argument("-v", "--verbose", action="count")

    parser.add_argument("-e", "--environment", choices=["dev", "test", "prod"], default="dev", help="blahblah")

    args = parser.parse_args()

    print(args)

# from parse_args import __main__

# __${NAME}__
# ^ dunder name (method)
# ^ protocol
# ^ trait or interface

# class Iterable:
#     def __next__(self) -> "Value":
#         raise StopIteration
