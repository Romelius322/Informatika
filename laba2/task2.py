salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_deficit = 0
current_spend = spend

for month in range(1, months + 1):
    deficit = current_spend - salary
    if deficit > 0:
        total_deficit += deficit
    # Увеличиваю расходы на следующий месяц (после первого)
    current_spend *= (1 + increase)
money_capital = round(total_deficit)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",money_capital)
