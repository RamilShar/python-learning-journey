# -*- coding: utf-8 -*-
"""
ПЕРСОНАЛЬНЫЙ СБОРЩИК ДАННЫХ
Автоматизация сбора: валюта, акции, погода
"""

# 1. СПИСОК валют - это просто перечень значений
currencies = ["USD", "EUR", "KZT", "CNY"]

# 2. СЛОВАРЬ курсов - это "ключ: значение"
exchange_rates = {
    "USD": 76.5,
    "EUR": 98.2, 
    "KZT": 0.18,
    "CNY": 12.4,
    "GBP": 100.5
}

# 3. СПИСОК акций (то, что вы хотели)
stocks = ["Татнефть", "Сбербанк", "Газпром", "Яндекс", "Роснефть"]

stock_prices = {
    "Татнефть": 800,
    "Сбербанк": 300,
    "Газпром": 180,
    "Яндекс": 4000,
    "Роснефть": 100
}

# СПОСОБ 1: Вручную (долго и неудобно)
print("Курсы валют:")
print(f"{currencies[0]}: {exchange_rates['USD']}")
print(f"{currencies[1]}: {exchange_rates['EUR']}")
# ... и так для каждой валюты

# СПОСОБ 2: Автоматически циклом for (быстро!)
print("\n=== АВТОМАТИЧЕСКИЙ ВЫВОД ===")
for currency in currencies:
    rate = exchange_rates[currency]
    print(f"{currency}: {rate} руб.")


# Без цикла (сложно):
# total = exchange_rates["USD"] + exchange_rates["EUR"] + ...

# С циклом (просто):
total = 0
count = 0

print("\n=== ПОДСЧЁТ СРЕДНЕГО КУРСА ===")
for currency_name, currency_rate in exchange_rates.items():
    total += currency_rate  # Добавляем курс к сумме
    count += 1              # Считаем количество
    print(f"Добавили {currency_name}: {currency_rate}")

average = total / count
print(f"\nСредний курс: {average:.2f} руб.")

#для акций

print("\n=== АВТОМАТИЧЕСКИЙ ВЫВОД ===")
for stock in stocks:
    price = stock_prices[stock]
    print(f"{stock}: {price} руб.")

# С циклом (просто):
total = 0
count = 0

print("\n=== ПОДСЧЁТ СРЕДНЕЙ ЦЕНЫ ===")
for stock_name, stock_price in stock_prices.items():
    total += stock_price  # Добавляем акции к сумме
    count += 1              # Считаем количество
    print(f"Добавили {stock_name}: {stock_price}")

average = total / count
print(f"\nСредняя цена: {average:.2f} руб.")


import csv
from datetime import datetime

# Получаем сегодняшнюю дату
today = datetime.now().strftime("%d.%m.%Y")

# Создаём файл с результатами
with open('financial_report.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Заголовки
    writer.writerow(["Дата", "Валюта", "Курс", "Средний курс"])
    
    # Записываем данные по валютам
    for currency in currencies:
        rate = exchange_rates[currency]
        writer.writerow([today, currency, rate, average])
    
    # Записываем акции
    writer.writerow([])  # Пустая строка
    writer.writerow(["Акции для отслеживания:"])
    for stock in stocks:
        writer.writerow(["", stock, "—", "—"])

print("\n✅ Отчёт сохранён в 'financial_report.csv'")
print("   Можете открыть его в Excel!")
