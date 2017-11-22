from section5.test.staticmethod_example import X

if __name__ == '__main__':
    x = X()

    x.normalmethod()
    X.classmethod()
    X.staticmethod()
