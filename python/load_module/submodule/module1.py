# Class to dynamically load.  This one doesn't take any constructor arguments.
class ClassNoArgs(object):
    def __init__(self):
        print('Loading {}'.format(type(self).__name__))

    def ping(self, string):
        print('Ping {}, {}'.format(type(self).__name__, string))

# Class to dynamically load.  This one takes a constructor argument.
class ClassArgs(object):
    def __init__(self, arg):
        self._arg = arg
        print('Loading {}, {}'.format(type(self).__name__, arg))

    def ping(self, string):
        print('Ping {}, {}, {}'.format(type(self).__name__, self._arg, string))
