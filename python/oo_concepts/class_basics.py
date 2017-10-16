# Note that most of these examples come from https://www.safaribooksonline.com/library/view/python-in-a/9781491913833/ch04.html
import unittest

class ClassProperties(unittest.TestCase):
    def test_class_attributes(self):
        '''
        Access class attributes.
        :return:
        '''

        class C(object):
            # Class level attribute.
            class_attrib = 100

            def get_class_attrib_on_class():
                return C.class_attrib

            def get_class_attrib_on_instance(self):
                # This needs to be qualified with the class name.
                return C.class_attrib

        # Directly access the attribute on the class.
        self.assertEqual(100, C.class_attrib, 'Direct access')

        # Access via accessor at class level.
        self.assertEqual(100, C.get_class_attrib_on_class(), 'Class level accessor')

        # Access via an instance of the class.
        c = C()
        self.assertEqual(100, c.get_class_attrib_on_instance(), 'Method access')

        # Not a very OO concept that anyone can set an attribute on a class.
        C.external_class_attrib = 200
        self.assertEqual(200, C.external_class_attrib, 'External set and get')

    def test_instance_attributes(self):
        '''
        Access instance attributes.
        :return:
        '''

        class C(object):
            def __init__(self, value):
                self.x = value

            def get_value(self):
                return self.x

        c = C(100)
        self.assertEqual(100, c.x, 'Direct access')
        self.assertEqual(100, c.get_value(), 'getter access')

        # Non OO way of tweaking instances of objects
        c.y = 200
        self.assertEqual(200, c.y, 'broken encapsulation')

    def test_base_magic_variables(self):
        '''
        Test what magic variables are set by instantiating an object.
        :return:
        '''
        class C(object):
            def __init__(self, value):
                self.x = value

        c = C(100)
        self.assertEqual('C', c.__class__.__name__, 'Class name')
        self.assertEqual({'x':100}, c.__dict__, 'Attribute dictionary')

        # Set an attribute through the dictionary.
        c.__dict__['y'] = 200
        self.assertEqual(200, c.y, 'Externally set attribute')

    def test_constant_object(self):
        '''
        Examples of descriptors for controlling access to instance attributes.
        :return:
        '''

        class Constant(object):
            def __init__(self, value):
                self.value = value

            def __set__(self, *_):
                '''
                Take any number of arguments, ignore them and prevent the
                attribute from being set on the instance.
                :param _: positional arguments to be set.
                :return:
                '''
                pass

            def __get__(self, *_):
                '''
                Always return the constant value.
                :param _: The name of the parameter to return.  Always ignored.
                :return: The constant value for this instance.
                '''
                return self.value

        class Container(object):
            constant = Constant(100)

        container = Container()
        self.assertEqual(100, container.constant, 'Access the constant value.')

        # Try and set the value.
        container.constant = 200
        self.assertEqual(100, container.constant, 'Check to make sure the value was not change')

    def test_singleton(self):
        # Singleton base class.
        class Singleton(object):
            _singletons = {}
            def __new__(cls, *args, **kwargs):
                if cls not in cls._singletons:
                    cls._singletons[cls] = super(Singleton, cls).__new__(cls)
                return cls._singletons[cls]

        s1 = Singleton()
        s2 = Singleton()
        self.assertEqual(s1, s2, 'Base class singleton.')

        class ChildSingleton(Singleton):
            pass

        s1 = ChildSingleton()
        s2 = ChildSingleton()
        self.assertEqual(s1, s2, 'Child singleton')

    def test_singleton_with_args(self):
        # Singleton base class.
        class Singleton(object):
            _singletons = {}
            def __new__(cls, *args, **kwargs):
                if cls not in cls._singletons:
                    cls._singletons[cls] = super(Singleton, cls).__new__(cls)

                return cls._singletons[cls]

            def __init__(self, value):
                # Need to make this safe as it is called regardless of whether a new
                # instance is created or not.
                self.value = value


        s1 = Singleton(100)
        s2 = Singleton(200)
        # print(s1, s1.value)
        # print(s2, s2.value)

        self.assertEqual(s1, s2, 'Base class singleton.')

        # Note that this is not the desired behavior.  The singleton should remain
        # constant over time.  See note above on making __init__ safe for multiple
        # calls to the constructor.
        self.assertEqual(200, s1.value, 'Access attribute')

if __name__ == '__main__':
    unittest.main()
