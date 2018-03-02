# https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html
import rpyc


class SubObject():
    def __init__(self):
        print('Constructing Sub Object')

    def exposed_method1(self):
        print('method1 called')
        return 'method1'


class MyService(rpyc.Service):
    def on_connect(self):
        self._subobject = SubObject()
        print(type(self._subobject))
        print(self._subobject.exposed_method1())

    def on_disconnect(self):
        pass

    def exposed_get_sub_object(self):
        return self._subobject

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer

    print(rpyc.__version__)

    server = ThreadedServer(MyService, port=18861)
    server.start()
