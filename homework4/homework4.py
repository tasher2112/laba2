from random import randint 
b = []
def multiple(num, func):
    while True:
        try:
            number = int(input("Введите цифру: "))
            if number >= 0 and number <=9:
                break
            else:
                print("Неверный ввод! Введите цифру от 0 до 9:")
        except ValueError:
            print("Неверный ввод! Введите цифру от 0 до 9!!!!")
    for i in num:
        if i % number == 0:
            func(i)

a = [randint(0,200) for i in range(randint(10, 20))]
print("Исходный массив: ", a)
multiple(a, lambda i: b.append(i))
if len(b)>0:
    print("Числа, кратные введённой цифре:", b)
else:
    print("Кратных чисел нет!")
