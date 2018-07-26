from tasks.tasks import add

result = add.delay(3, 4)
print(result.get(timeout=1))
