from functools import wraps


def mydecorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        print("Before decorated function")
        result = f(*args, **kwargs)
        print("After decorated function")
        return result

    return wrapped


@mydecorator
def myfunc(myarg):
    print("my function", myarg)
    return "return value"


r = myfunc('asdf')
print(r)
