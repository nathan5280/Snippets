class X(object):
    def normalmethod(self):
        print('Normal method:')


    @classmethod
    def classmethod(cls):
        print('Class method: ', cls.__name__)


    @staticmethod
    def staticmethod():
        print('Static method')

if __name__ == '__main__':
    x = X()

    x.normalmethod()
    X.classmethod()
    X.staticmethod()

