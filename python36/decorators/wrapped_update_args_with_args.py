from functools import wraps


def my_arg_decorator(arg_value):
    def my_decorator(funct):
        @wraps(funct)
        def wrapped(*args, **kwargs):
            print(f"before decoration: args: {args}, kwargs: {kwargs}")

            kw_new = {
                "kw_arg2": {
                    "kw_arg2": arg_value
                }
            }

            kwargs.update(kw_new)

            result = funct(*args, **kwargs)
            print(f"after decoration: arg1: {args}, kwargs: {kwargs}")
            return result

        return wrapped

    return my_decorator


@my_arg_decorator("Passed Argument")
def myfunc(arg1, **kwargs):
    print(f"myfunc: arg1: {arg1}, kwargs: {kwargs}")
    return "return value"


r = myfunc("v1", kw_arg1={"kw_arg1.1": "kw_value1.1"})
print(r)
