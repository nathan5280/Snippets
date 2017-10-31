# simple classes used for type checking examples.
class BaseClass(object):
    def announce(self):
        print('BaseClass')


class ChildClass(BaseClass):
    def announce(self):
        print('ChildClass')

