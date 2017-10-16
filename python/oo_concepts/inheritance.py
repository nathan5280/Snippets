# Note that most of these examples come from https://www.safaribooksonline.com/library/view/python-in-a/9781491913833/ch04.html
import unittest

from io import StringIO
from sys import stdout

class ClassInheritance(unittest.TestCase):
    def test_inheritance(self):
        verbose = False
        if verbose:
            output = stdout
        else:
            output = StringIO()

        class Base(object):
            def greet(self, name):
                output.write('Welcome {}'.format(name))

        class Sub(Base):
            def greet(self, name):
                output.write('Well met and ')
                Base.greet(self, name)


        x = Sub()
        x.greet('Nate')

        if output != stdout:
            self.assertEqual('Well met and Welcome Nate', output.getvalue())

    def test_bound_methods(self):
        verbose = False
        if verbose:
            output = stdout
        else:
            output = StringIO()

        # Deal with the diamond pattern.
        # super manages everything to make sure that met is only called
        # once in each class.
        class A(object):
            def met(self):
                output.write('A.met,')

        class B(A):
            def met(self):
                output.write('B.met,')
                super().met()

        class C(A):
            def met(self):
                output.write('C.met,')
                super().met()

        class D(B, C):
            def met(self):
                output.write('D.met,')
                super().met()

        d = D()
        d.met()

        if output != stdout:
            self.assertEqual('D.met,B.met,C.met,A.met,', output.getvalue())


    def test_class_method(self):
        verbose = False
        if verbose:
            output = stdout
        else:
            output = StringIO()

        class ABase(object):
            def aclassmet(cls):
                output.write('a class method for {}\n'.format(cls.__name__))

            aclassmet = classmethod(aclassmet)

        class ADeriv(ABase): pass

        b_instance = ABase()
        d_instance = ADeriv()
        ABase.aclassmet()       # prints: a class method for ABase
        b_instance.aclassmet()  # prints: a class method for ABase
        ADeriv.aclassmet()      # prints: a class method for ADeriv
        d_instance.aclassmet()  # prints: a class method for ADeriv

        result = 'a class method for ABase\na class method for ABase\na class method for ADeriv\na class method for ADeriv'
        if output != stdout:
            self.assertEqual(result, output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
