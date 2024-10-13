def my_generate(start, stop):
    n = 0
    number = start
    while number <= stop:
        if number % 2 != 0:
            yield number
            n += 1
        number += 1
ranger = my_generate(0,30)
last = 0
print("Исходный массив: ")
for i in ranger:
    print(i, end=" ")
ranger = my_generate(0,30)
print("\nПервое, третье и пятое значения: ")
for index, value in enumerate(ranger):
    if index == 0 or index == 4:
        print(value)
    last = value
print(last)