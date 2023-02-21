NUM_EMPLOYEER = 6

def main():

    hours = [0] * NUM_EMPLOYEER
    # Получить часы, отработанные сотрудником
    for index in range(NUM_EMPLOYEER):
        hours[index] = float(input(f'Введите количество часов отработанных сотрудником {index + 1}: '))

    # Получить почасовую ставку оплаты.
    pay_rate = float(input('Введите почасовую ставку опаты: '))

    # Показать заработную плату квждого сотрудника.
    for index in range(NUM_EMPLOYEER):
        gross_pay = hours[index] * pay_rate
        print(f'Зарплата сотрудника: {index + 1}: ${gross_pay:,.2f}')


if __name__ == '__main__':
    main()