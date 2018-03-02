# https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html
import rpyc


class MyService(rpyc.Service):
    def on_connect(self):
        print(self._conn)
        pass

    def on_disconnect(self):
        print(self._conn)
        pass

    def exposed_get_answer(self):
        return 42

    exposed_the_real_answer_though = 43

    def get_question(self):
        return 'What is the airspeed velocity of an unladen swallow?'

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer
    print(rpyc.__version__)

    server = ThreadedServer(MyService, port=18861)
    server.start()