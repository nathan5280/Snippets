g_var = 1
print("init: ", g_var, id(g_var))


def set_g_var(v):
    global g_var

    g_var = v
    print("set: ", id(g_var))


def get_g_var():
    print("get: ", id(g_var))
    return g_var
