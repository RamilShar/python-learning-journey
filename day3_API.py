import requests
import csv
from datetime import datetime

def get_currency_rates():
    """
    Получает актуальные курсы валют с бесплатного API
    Возвращает словарь с курсами
    """
    try:
        # Делаем запрос к API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=50)
        data = response.json()
        
        # Извлекаем курсы
        rub_rate = data["rates"]["RUB"]
        eur_rate = rub_rate / data["rates"]["EUR"]
        kzt_rate = rub_rate / data["rates"]["KZT"] if "KZT" in data["rates"] else 0.18
        cny_rate = rub_rate / data["rates"]["CNY"] if "CNY" in data["rates"] else 12.4
        gbp_rate = rub_rate / data["rates"]["GBP"] if "GBP" in data["rates"] else 100.5
        jpy_rate = rub_rate / data["rates"]["JPY"] if "JPY" in data["rates"] else 0.01
        
        return {
            "USD": rub_rate,
            "EUR": eur_rate,
            "KZT": kzt_rate,
            "CNY": cny_rate,
            "GBP": gbp_rate,
            "JPY": jpy_rate
        }
        
    except Exception as e:
        print(f"⚠️ Не удалось получить актуальные курсы: {e}")
        print("Используем данные по умолчанию")
        return {
            "USD": 90.5,
            "EUR": 98.2,
            "KZT": 0.18,
            "CNY": 12.4,
            "GBP": 100.5,
            "JPY": 0.01
        }

# Основная программа
print("=== СБОР АКТУАЛЬНЫХ КУРСОВ ВАЛЮТ ===")
print("Подключаемся к серверу...")

# Получаем актуальные курсы
exchange_rates = get_currency_rates()

# Выводим результат
for currency, rate in exchange_rates.items():
    print(f"{currency}: {rate:.2f} руб.")

# После получения курсов выводим средний курс:
average_rate = sum(exchange_rates.values()) / len(exchange_rates)
print(f"\nСредний курс: {average_rate:.2f} руб.")

# Сохраняем в файл
today = datetime.now().strftime("%d.%m.%Y %H:%M") # 23.01.2024 21:30 здесь можно убрать время

with open('actual_rates.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Дата", "Валюта", "Курс к RUB"])
    writer.writerow([today, "СРЕДНИЙ", f"{average_rate:.2f}"]) #добавил средний курс
    
    for currency, rate in exchange_rates.items():
        writer.writerow([today, currency, f"{rate:.2f}"])

print(f"\n✅ Актуальные курсы сохранены в 'actual_rates.csv'")
print(f"   Обновлено: {today}")
