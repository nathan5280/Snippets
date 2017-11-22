class TestException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrappedException(Exception):
    def __init__(self, msg, org_exception):
        super().__init__('{} inner exception: {}'.format(msg, org_exception))
        self._org_exception = org_exception

    @property
    def org_exception(self):
        return self._org_exception

def method():
    try:
        print('raising test exception')
        raise TestException('Test Exception 1')

    except TestException:
        raise

    except Exception as e:
        print('raising wrapped exception')
        raise WrappedException('Wrapped exception', e)


try:
    method()
except Exception as e:
    print(e.__str__())