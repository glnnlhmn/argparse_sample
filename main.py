import argparse
import pprint
from typing import Optional
from typing import Sequence

def positive_int(s: str) -> int:
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{s} is not an integer")

    if value <= 0:
        raise argparse.ArgumentTypeError(f"{s} is not a positive integer")

    return value

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description='Process some integers.')

    """\
    # positional
    # - help
    # parser.add_argument("filename", help="input filename")

    # optional
    # - short vs long opts
    # - aliases
    # - defaults
    parser.add_argument("-c", "--config", "--config-file",
                        default="config.json",
                        help="specify the config file (default: %(default)s)",
    )

    # type
    # parser.add_argument(
    #     "-w", "--week", type=int,
    # )

    # custom type
    # parser.add_argument(
    #     "-w", "--week", type=positive_int,
    # )


    # count
    parser.add_argument(
        "-v", "--verbose", action="count", default=0,
    )

    # boolean options
    parser.add_argument(
        "--force", action="store_true",
    )

    # append
    parser.add_argument(
        "-w", "--week", action="append", type=positive_int
    )

    # choices
    parser.add_argument(
        "--mode", choices=["train", "test"],
    )
    """

    # # sub-commands
    # subparsers = parser.add_subparsers(dest="command")
    #
    # status_parser = subparsers.add_parser("status")
    # status_parser.add_argument("-f", "--force", action="store_true")
    #
    # checkout_parser = subparsers.add_parser("checkout")
    # checkout_parser.add_argument("-v", "--verbose", action="count", default=0)


    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args(argv)

    pprint.pprint(vars(args))

    print(args.accumulate(args.integers))
    return 0

if __name__ == "__main__":
    exit(main())