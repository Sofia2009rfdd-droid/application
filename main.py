# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
index = ''
p = ''
OGRNIP = ''
INN = ''
Payment_account = ''
Bank_name = ''
BIK = ''
Correspondent_account = ''


def general_info_user(
    n_parameter,
    a_parameter,
    ph_parameter,
    e_parameter,
    index_parameter,
    p_parameter,
    i_parameter
):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', index_parameter)
    print('Почтовый адрес: ', p_parameter)
    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                n = input('Введите имя: ')
                while 1:
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                e = input('Введите адрес электронной почты: ')
                index = input('Введите индекс: ')
                p = input('Введите почтовый адрес: ')
                i = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                while 1:
                    OGRNIP = input('Введите ОГРНИП: ')
                    if len(OGRNIP) == 15 and OGRNIP.isdigit():
                        break
                    print('ОГРНИП должен состоять из 15-и цифр.')
                INN = input('Введите ИНН: ')

                while 1:
                    Payment_account = input('Введите расчётный счёт: ')
                    if len(Payment_account) == 20 and
                    Payment_account.isdigit():
                        break
                    print('Расчётный счёт должен состоять из 20-и цифр.')
                Bank_name = input('Введите название банка: ')
                BIK = input('Введите БИК: ')
                Correspondent_account = input('Введите '
                                              'корреспондентский счёт: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, index, p, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, index, p, i)
                print('ОГРНИП: ', OGRNIP)
                print('ИНН: ', INN)
                print('Расчётный счёт: ', Payment_account)
                print('Название банка: ', Bank_name)
                print('БИК: ', BIK)
                print('Корреспондентский счёт: ', Correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
