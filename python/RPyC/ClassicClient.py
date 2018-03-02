import rpyc

conn = rpyc.classic.connect('127.0.0.1')
module = conn.modules['modules.MyClass']
myclass = module.MyClass()
print(myclass.method1())