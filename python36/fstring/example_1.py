"""
Simple examples related to fstring.

fstring was implemented in Python 3.6
"""
import time


def simple() -> None:
    """
    Simple text insertion into output string.
    :return: None
    """
    print(f"\n{__file__}:simple")

    text = "The lazy dog took a nap."
    print(f"\tString: {text}")


def number() -> None:
    """
    Number formating.

    :return: None
    """
    print(f"\n{__file__}:number")

    num = 1000 / 3
    print(f"\tNumber: {num}")


def number_format() -> None:
    """
    Number formating.

    :return: None
    """
    print(f"\n{__file__}:number_format")

    num = 1000 / 3
    print(f"\tNumber: {num:{10}.{4}}")


def performance() -> None:
    """
    Performance comparison between fstring and .format

    fstring generally tests to be 2-3 times faster than .format!

    :return: None
    """
    print(f"\n{__file__}:performance")

    n = 1000 / 3
    iters = 1000000

    t0_fmt = time.time()
    for _ in range(iters):
        s = "{:010.4f}".format(n)
    t1_fmt = time.time()
    print(f"\t.format: {t1_fmt-t0_fmt:{6}.{3}}")

    t0_fstr = time.time()
    for _ in range(iters):
        s = f"n:0{10}.{4}"
    t1_fstr = time.time()
    print(f"\tfstring: {t1_fstr-t0_fstr:{6}.{3}}")

    t_fmt = t1_fmt - t0_fmt
    t_fstr = t1_fstr - t0_fstr
    print(f"\tPerformance Improvement: {t_fmt/t_fstr:{6}.{2}}")


if __name__ == '__main__':
    simple()
    number()
    number_format()
    performance()
