from models import Calculator


def main():
    a = 1
    b = 2

    r = Calculator.add(a=a, b=b)
    print(f"(a+b): a={a}, b={b}, result={r}")


if __name__ == '__main__':
    main()
