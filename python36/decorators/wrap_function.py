def raw_funct(arg1, **kwargs):
    print(f"\tfunction: args={arg1}, kwargs={kwargs}")


def add_kwarg_wrapper(funct, *args, **kwargs):
    existing_dict_kwarg = kwargs.get("kw_dict_arg", {})

    update_dict = {
        "kwarg1": "new_kw_value1",
        "kwarg2": "new_kw_value2"
    }

    existing_dict_kwarg.update(update_dict)

    funct(*args, **kwargs)


if __name__ == '__main__':
    print("Bare Function: ")
    raw_funct("arg1", kwarg1="kw_value1")

    print()
    print("Wrapped Function: ")
    add_kwarg_wrapper(raw_funct, "arg1", kw_dict_arg={"kwarg1": "old_kw_value1"})
