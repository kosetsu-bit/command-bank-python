#банк нахуй

#баланс банка
balance = 0.0
#баланс вклада
deposit_balance = 0.0

#ввод фио и т.д
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
print("Здравствуйте, " + first_name.capitalize() + " " + last_name.capitalize() + "!")

#пополнение счета
answer = input("Вы хотите положить деньги на счет? (да/нет): ").strip().lower()

if answer == "да":
    amount = float(input("Введите сумму для пополнения: ").replace(",", "."))
    balance += amount
    if balance.is_integer():
        display_balance = int(balance)
    else:
        display_balance = balance
    print("Ваш баланс успешно пополнен. Текущий баланс: " + str(display_balance))
elif answer == "нет":
    print("Хорошо, ваш баланс остается без изменений. Текущий баланс: " + str(balance))

#выбор действия
running = True
while running:
    answer = input('''Выберите действие (только цифра):
1. Снять деньги со счета.
2. Перевести деньги.
3. Внести деньги в вклад.
4. Просмотреть баланс вклада.
5. Снять деньги с вклада.
0. Выход из программы.
''').strip()

    if answer == "1":
        amount = float(input("Введите сумму которую хотите снять: ").replace(",", "."))
        balance -= amount
        if balance.is_integer():
            display_balance = int(balance)
        else:
            display_balance = balance
        print("Деньги успешно сняты! Остаток баланса: " + str(display_balance))

    elif answer == "2":
        number = input("Введите номер телефона человека, которому хотите перевести деньги: ").strip()
        choice = input("Проверьте, верно ли введен номер телефона (" + number + ")? (да/нет): ").strip().lower()

        if choice == "да":
            amount = float(input("Введите сумму денег, которую хотите перевести: ").replace(",", "."))
            balance -= amount
            if balance.is_integer():
                display_balance = int(balance)
            else:
                display_balance = balance
            print("Перевод денег на сумму " + str(amount) + " успешно выполнен! Остаток счета: " + str(display_balance))
        elif choice == "нет":
            print("Проверьте номер телефона и попробуйте снова.")

    elif answer == "3":
        amount = float(input("Введите сумму для вклада: ").replace(",", "."))
        deposit_balance += amount
        if deposit_balance.is_integer():
            display_deposit = int(deposit_balance)
        else:
            display_deposit = deposit_balance
        print("Деньги успешно внесены в вклад! Баланс вклада: " + str(display_deposit))

    elif answer == "4":
        if deposit_balance.is_integer():
            display_deposit = int(deposit_balance)
        else:
            display_deposit = deposit_balance
        print("Баланс вашего вклада: " + str(display_deposit))

    elif answer == "5":
        amount = float(input("Введите сумму для снятия с вклада: ").replace(",", "."))
        deposit_balance -= amount
        if deposit_balance.is_integer():
            display_deposit = int(deposit_balance)
        else:
            display_deposit = deposit_balance
        print("Деньги успешно сняты с вклада! Баланс вклада: " + str(display_deposit))

    elif answer == "0":
        print("Спасибо за использование нашего банка! До свидания!")
        running = False

    else:
        print("Неизвестная команда. Введите цифру из меню.")
