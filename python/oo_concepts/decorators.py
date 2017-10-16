import unittest


class StaticMethod(object):
    @staticmethod
    def method(*argv):
        return argv

class ClassMethod(object):
    @classmethod
    def method(*argv):
        return argv

class Decorators(unittest.TestCase):
    def test_staticmethod(self):
        o = StaticMethod()
        r = o.method
        R = '<function StaticMethod.method at '
        self.assertTrue(r.__repr__().startswith(R), 'Class function.')

        r = o.method('arg1')
        self.assertEqual(('arg1',), r, 'Single argument.')

        r = StaticMethod.method('arg2')
        self.assertEqual(('arg2',), r, 'Direct on class')

    def test_classmethod(self):
        o = ClassMethod()
        r = o.method
        R = "<bound method ClassMethod.method of <class '__main__.ClassMethod'>>"
        self.assertEqual(R, r.__repr__(), 'Bound method.')

        r = o.method('arg1')
        self.assertEqual(r[1], 'arg1', 'With class reference.')

        r = ClassMethod.method('arg2')
        self.assertEqual(r[1], 'arg2', 'Direct on class')


if __name__ == '__main__':
    unittest.main()
