from scratch.pkg.mod import show_g_var, get_g_var
from scratch import set_g_var

if __name__ == '__main__':
    show_g_var()
    set_g_var(2)
    show_g_var()
    print("main", get_g_var())