money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долго
months = 0
current_spend = spend  # траты в текущем месяце (первый месяц без повышения)

while money_capital + salary >= current_spend:
    # Тратим из подушки разницу между расходами и зарплатой
    money_capital -= (current_spend - salary)
    months += 1
    # Увеличиваем расходы на следующий месяц
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months )
