import unittest

'''
1) Run entire test suite from command line with: python <filename>
2) Run test class from command line with: python <filename> <classname>
3) Run a single test from command line with: python <filename> <classname>.<testname>

Add new tests by adding to the test class and naming the function test_<testname>

Function declaration:
    *args:
        - allows the function to except an unknown list of positional arguements.
    **kwargs:
        - allows the function to except an unknown list of named arguments.

Function call:
    *args:
        - Explodes a list of arguments into positional arguments in the function's arguments.
    **kwargs:
        - Exploes a dictionary of arguments into named arguments in the function's arguments.
'''

def positional(a1, a2, a3):
    return (a1, a2, a3)

def unknown_positional(a1, *args):
    result = [a1]
    for a in args:
        result.append(a)
    return tuple(result)

def unknown_named(a1, **kwargs):
    result = {'a1':a1}

    for key in kwargs.keys():
        result[key] = kwargs[key]
    return result

def unknown_positional_and_named(a1, *args, **kwargs):
    # This gets funky as averything winds up in args.
    # ([args], {kwargs})
    result = {'a1':a1}

    for i, arg in enumerate(args[0]):
        result['a'+str(i+2)] = arg

    for key in args[1].keys():
        result[key] = args[1][key]

    return result

def fully_specified(a1, a2, a3, a4=None, a5=None):
    return {'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5}


class StarArg(unittest.TestCase):
    def test_positional(self):
        a1, a2, a3 = 1, 2, 3
        r = positional(a1, a2, a3)
        self.assertEqual((a1, a2, a3), (r[0], r[1], r[2]))

    def test_unknown_positional(self):
        '''
        Pass extra positional args that appear as *args in function.
        '''
        a1, a2, a3 = 1, 2, 3
        r = unknown_positional(a1, a2, a3)
        self.assertEqual((a1, a2, a3), (r))

    def test_exploed_positional(self):
        a1 = 1
        args = [2,3]
        r = unknown_positional(a1, *args)
        self.assertEqual((a1, args[0], args[1]), (r))

    def test_unknown_named(self):
        '''
        Pass extra named args that appear as **kwargs in function.
        '''
        a1 = 1
        r = unknown_named(a1, a2=2, a3=3)
        self.assertEqual({'a1': 1, 'a2': 2, 'a3': 3}, r)

    def test_exploded_named(self):
        '''
        Explode the named parameters.
        '''
        a1 = 1
        kwargs = {'a2':2, 'a3':3}
        r = unknown_named(a1, **kwargs)
        self.assertEqual({'a1': 1, 'a2': 2, 'a3': 3}, r)

    def test_unknown_positional_and_named(self):
        '''
        Call method with both *args and **kwargs in parameter list.
        It works fine on the calling side, but make sure to check out what
        happens on the method side when the arguments are unpacked.
        '''
        a1 = 1
        args = [2,3]
        kwargs = {'a4':4, 'a5':5}
        r = unknown_positional_and_named(a1, args, kwargs)
        self.assertEqual({'a1': 1, 'a2': 2, 'a3': 3, 'a4':4, 'a5':5}, r)

    def test_exploded_the_works(self):
        '''
        Explode list of positional and dictionary of parameters in call.
        '''
        a1 = 1
        args = [2,3]
        kwargs = {'a4':4, 'a5':5}
        r = fully_specified(a1, *args, **kwargs)
        self.assertEqual({'a1': 1, 'a2': 2, 'a3': 3, 'a4':4, 'a5':5}, r)

if __name__ == '__main__':
    unittest.main()
