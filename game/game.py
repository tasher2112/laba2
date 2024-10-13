import random
a = ["Камень", "Ножницы", "Бумага"]
def gameplay(user):
    comp = random.randint(1,3)
    print("Выбор игрока: ", a[user-1])
    print("Выбор компьютера: ", a[comp-1])
    if user == comp:
        print("___Ничья!___")
    elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
        print("___Вы выйграли!!!___")
    else:
        print("___Вы проиграли(((___")

def game():
    while True:
        try:
            choice = int(input("Выберите: \n 1.Камень \n 2.Ножницы\n 3.Бумага \n 4.Выход \n Ваш выбор: "))
            if choice == 4:
                print("Вы вышли из игры!")
                break
            if choice > 0 and choice < 4:
                gameplay(choice)
            else:
                print("Повторите ввод!!!")
        except ValueError:
            print("Повторите ввод!")
    
game()