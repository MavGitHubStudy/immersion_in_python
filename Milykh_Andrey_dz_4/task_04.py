"""
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции - функции. Дополнительно сохраняйте
все операции поступления и снятия в список.

Напишите программу банкомат.
- Начальная сумма равна нулю.
- Допустимые действия: пополнить, снять, выйти.
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие - 1.5 от суммы снятия,
  но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия
  начисляются проценты - 3%.
- Нельзя снять больше, чем на счёте.
- При превышении суммы в 5 млн вычитать налог на
  богатство 10% перед каждой операцией, даже ошибочной.
- Любое действие выводит сумму денег.
"""
import decimal

DIVISOR = 50
MIN_MONEY = 30
MAX_MONEY = 600
LUXURY_MONEY = 5_000_000
#  percents
ACCRUAL_OPERATIONS = 3
ACCRUAL_PERCENT = 3
DEDUCTION_PERCENT = decimal.Decimal(3/2)
LUXURE_PERCENT = 10


userinfo = {
    "number_operations": 0,
    "money": decimal.Decimal(0),
}


def show_balanc():
    print(f"Баланс: {userinfo['money']} у.е.")


def interest_accrual():
    userinfo['money'] = userinfo['money'] + userinfo['money'] / 100 * \
                        ACCRUAL_PERCENT

    userinfo['number_operations'] = 0


def add_money(deposit_amount: decimal.Decimal):
    userinfo['money'] += deposit_amount
    userinfo['number_operations'] += 1
    print(userinfo['number_operations'])
    if userinfo['number_operations'] == ACCRUAL_OPERATIONS:
        interest_accrual()
    show_balanc()


def subtract_money(deposit_deduction: decimal.Decimal):
    userinfo['money'] -= deposit_deduction
    userinfo['number_operations'] += 1
    print(userinfo['number_operations'])
    if userinfo['number_operations'] == ACCRUAL_OPERATIONS:
        interest_accrual()
    show_balanc()


def luxury_tax():
    if userinfo['money'] > LUXURY_MONEY:
        userinfo['money'] -= userinfo['money'] / 100 * LUXURE_PERCENT


while True:
    choice = input("""Меню:
        [ 1 ] пополнить 
        [ 2 ] снять
        [ 3 ] выйти
        Пожалуйста, введите ваш выбор: """)

    if choice == '1':
        luxury_tax()
        while True:
            money_in = decimal.Decimal(input("Введите сумму, кратную 50 у.е, "
                                             "которую вы хотите внести: "))
            if money_in % DIVISOR == 0:
                add_money(money_in)
                break
    elif choice == '2':
        luxury_tax()
        while True:
            money_out = decimal.Decimal(input("Введите сумму, кратную 50 у.е, "
                                              "которую вы хотите снять: "))
            if money_out % DIVISOR == 0:
                percent = money_out / 100 * DEDUCTION_PERCENT
                if percent < MIN_MONEY:
                    percent = MIN_MONEY
                if percent > MAX_MONEY:
                    percent = MAX_MONEY
                money_out = money_out + percent
                if money_out > userinfo['money']:
                    print("Операция не выполнена. Недостаточно средств на "
                          "счёте!")
                    show_balanc()
                    break
                else:
                    subtract_money(money_out)
                    break
    elif choice == '3':
        print("Обслуживание завершено.")
        exit(0)
