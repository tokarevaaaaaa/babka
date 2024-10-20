money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mounth = 0

while (money_capital > 0):
    spend_tmp = spend - 5000
    money_capital -= spend_tmp
    spend = spend + spend * increase
    mounth += 1

if (money_capital < 0):
    mounth -= 1

print("Количество месяцев, которое можно протянуть без долгов:", mounth)
