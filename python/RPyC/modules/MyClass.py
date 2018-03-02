import threading

class MyClass():
    def method1(self):
        print('MyClass.method1(): ',threading.current_thread())
        return('MyClass.method1() Invoked')

