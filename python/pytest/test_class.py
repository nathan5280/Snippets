pass_tests = True

class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'

        if pass_tests:
            assert 1 == 1
        else:
            assert hasattr(x, 'check')