import argparse, sys

class CmdLineCfgMgr(object):
    '''
    Command line parser.
    '''
    def __init__(self, argv):
        '''
        Encapsulate the parasing and storage of the command line arguments.

        Args:
            argv: The command line arguments to parse.
        '''
        # Create the parser.
        parser = argparse.ArgumentParser(description='Example command line parser.')

        # A simple command line argument that is stored in arg_v
        parser.add_argument('-v', dest='arg_v', required=True,
                            help='Value argument')

        # A simple command line flag that stores false if it isn't present or true if it is.
        parser.add_argument('-t', dest='arg_t', action='store_true', default=False,
                            help='t-Flag argument')

        # A simple command line flag that stores false if it isn't present or true if it is.
        parser.add_argument('-f', dest='arg_f', action='store_true', default=False,
                            help='f-Flag argument')

        # An argument that can appear one or more times.
        parser.add_argument('-m', dest='arg_list', action='append', required=True,
                            help='List argument can appear multiple times.')

        self._cfg = parser.parse_args(argv)

    @property
    def cfg_dict(self):
        '''
        Get the command line arguments as a dictionary.

        Returns: dictionary of commandline arguments
        '''
        return vars(self._cfg)

if __name__ == '__main__':
    # When you call this with the systems argv you need
    # to strip off the first argument which is the filename of the python script.
    cmd_line_args = CmdLineCfgMgr(sys.argv[1:])