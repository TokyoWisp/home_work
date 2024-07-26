#1
a: int = 2
b: float = 3.25
c: str = 'null'
d: list = [2, 14]
e: bool = (3 < 5)

def task_1(a, b, c, d, e) -> str:
    return (a, b, c, d, e)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(task_1(3, 4.1, 'zero', [3,6], (8<3)))


#2
def task_2(a = [1, 2, 3, 5, 8, 13, 21]) -> int: #последовательность Фибоначчи
    return (a[0:3])

print(task_2())


#3
def task_3(a: int) -> int:
    return (a ** 2)

print(task_3(6))
