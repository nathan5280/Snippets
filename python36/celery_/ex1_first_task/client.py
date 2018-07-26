import time

from tasks.tasks import add

if __name__ == '__main__':
    result = add.delay(3, 4)

    print(result.ready())

    time.sleep(1)

    print(result.ready())
    print(result.state, result.result)
