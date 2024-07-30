#1 
def max_num(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1

print(max_num(3, 26))


#2
def num(num1, num2):
    if num1 - num2 == 135 or num2 - num1 == 135:
        print('Yes')
    else:
        print('No')

num(15, 10)


#3
def season(month: int):
    if 3 <= month <= 5:
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif 9 <= month <= 11:
        print('Осень')
    else:
        print('Зима')

season(12)


#4
def numbers(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('Yes')
    else:
        print('No')

numbers(11, 14, 19)


#5
