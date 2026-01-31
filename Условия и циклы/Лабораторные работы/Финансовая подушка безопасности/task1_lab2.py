money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months_survived = 0
total_money = money_capital + salary
actual_spend = spend

while money_capital + salary >= spend:
    total_money = money_capital + salary

    total_money -= spend

    money_capital = total_money

    months_survived += 1

    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_survived)
