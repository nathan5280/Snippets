from models.rpn import RPN


def add(x: int, y: int) -> int:
    calculator = RPN()
    calculator.clear()
    calculator.push(x)
    calculator.push(y)
    r = calculator.add()
    return r


def sub(x: int, y: int) -> int:
    calculator = RPN()
    calculator.clear()
    calculator.push(x)
    calculator.push(y)
    r = calculator.sub()
    return r


if __name__ == '__main__':
    r = add(1, 2)
    assert 3 == r

    r = sub(3, 2)
    assert 1 == r
