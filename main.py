import argparse
import pprint
from typing import Optional
from typing import Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    # positional
    # optional
    # short vs long opts
    # aliases
    # help
    # defaults
    # types
    # custom types
    # count
    # append
    # boolean options
    # choices
    # sub-commands

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))
    return 0

if __name__ == "__main__":
    exit(main())