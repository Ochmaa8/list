def main():
    print("Выберите задание:")
    print("1 - Перевернуть массив")
    print("2 - Специальное преобразование массива")
    print("3 - Рыбаки и лодки")
    
    choice = int(input("Введите номер задания: "))
    
    if choice == 1:
        from task1 import task1
        task1()
    elif choice == 2:
        from task2 import task2
        task2()
    elif choice == 3:
        from task3 import task3
        task3()
    else:
        print("Ошибка: выберите 1, 2 или 3")

if __name__ == "__main__":
    main()
