# Quick example of how to dynamically load a module and class from that
# module by module name and class name.

import importlib

def main():
    # Load the module by name.
    module = importlib.import_module('submodule.module1')

    print('ClassNoArgs')
    # Get the class definition from the module
    class_no_args_def = getattr(module, 'ClassNoArgs')

    # Instatntiate the classs
    class_no_args = class_no_args_def()

    # Test the instance of the class.
    class_no_args.ping('Class No Args Ping')

    print('\nClassArgs')
    class_args = getattr(module, 'ClassArgs')('Arg1')
    class_args.ping('Class Args Ping')

if __name__ == '__main__':
    main()
