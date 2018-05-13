import argparse
from typing import Dict, List


class CmdLineArgParser(object):
    """
    Command line parser.
    """

    def __init__(self, argv: List[str]):
        """
        Encapsulate the parasing and storage of the command line arguments.

        Args:
            argv: The command line arguments to parse.
        """
        # Create the parser.
        parser = argparse.ArgumentParser(description='Example command line parser.')

        # A simple command line argument that is stored in arg_v
        parser.add_argument('-a',
                            dest='arg_a',
                            required=True,
                            help='Value argument')

        # A simple command line flag that stores false if it isn't present or true if it is.
        parser.add_argument('-f',
                            dest='arg_f',
                            action='store_true',
                            default=False,
                            help='t-Flag argument')

        # An argument that can appear one or more times.
        parser.add_argument('-m',
                            dest='arg_list',
                            action='append',
                            required=True,
                            help='List argument can appear multiple times.')

        self._cfg = parser.parse_args(argv)

    @property
    def cfg_dict(self) -> Dict:
        """
        Get the command line arguments as a dictionary.

        Returns: dictionary of commandline arguments
        """
        return vars(self._cfg)


def max_default() -> None:
    print(f"\n{__file__}:max_default")

    argv = ["-a", "simple-arg",
            "-m", "value-1"]

    parser = CmdLineArgParser(argv)
    print("\t-a -m:", parser.cfg_dict)


def min_default() -> None:
    print(f"\n{__file__}:min_default")

    argv = ["-a", "simple-arg",
            "-f",
            "-m", "value-1",
            "-m", "value-2"]

    parser = CmdLineArgParser(argv)
    print("\t-a -f -m -m:", parser.cfg_dict)


if __name__ == '__main__':
    max_default()
    min_default()
