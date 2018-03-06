pass_tests = False

class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'

        if pass_tests:
            print("1 == 1")
            assert 1 == 1
        else:
            print("hasattr")
            assert hasattr(x, 'count')