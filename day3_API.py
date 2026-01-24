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

def get_stock_price(ticker, use_real_api=False):
    """
    Получает цену акции по тикеру
    """
    
    # Словарь с тестовыми данными
    mock_prices = {
        "GAZP": 180.50, "SBER": 300.25, "TATN": 800.75,
        "ROSN": 600.30, "YNDX": 4000.00, "AAPL": 190.50,
        "GOOGL": 145.25, "TSLA": 250.75, "MSFT": 410.25,
        "BTC": 45000.00
    }
    
    ticker = ticker.upper()
    
    # Если запросили реальный API
    if use_real_api:
        try:
            print(f"⚠️ Режим реального API ещё не настроен")
            print(f"   Используем тестовые данные для {ticker}")
        except:
            print(f"❌ Ошибка при запросе реальных данных для {ticker}")
    
    # Возвращаем цену из тестовых данных
    if ticker in mock_prices:
        return mock_prices[ticker]
    else:
        print(f"⚠️ Тикер {ticker} не найден в тестовых данных")
        return None

def get_all_financial_data():
    """
    Собирает ВСЕ финансовые данные: валюты + акции
    """
    print("=== СБОР ФИНАНСОВЫХ ДАННЫХ ===")
    
    # 1. Получаем валюты
    print("\n1. Получаем курсы валют...")
    currencies = get_currency_rates()
    
    # 2. Получаем акции
    print("\n2. Получаем цены акций...")
    
    stock_tickers = ["SBER", "GAZP", "TATN", "AAPL", "MSFT", "BTC"]
    stocks = {}
    
    for ticker in stock_tickers:
        price = get_stock_price(ticker, use_real_api=False)
        if price:
            stocks[ticker] = price
            # Определяем валюту
            if ticker == "BTC":
                currency = " $"
            elif ticker in ["SBER", "GAZP", "TATN"]:
                currency = " руб."
            else:
                currency = " $"
            print(f"   {ticker}: {price:.2f}{currency}")
    
    return currencies, stocks

# Основная программа
if __name__ == "__main__":
    # Получаем все данные
    exchange_rates, stock_prices = get_all_financial_data()
    
    print("\n" + "="*50)
    print("ИТОГОВЫЕ ДАННЫХ:")
    print("="*50)
    
    # Выводим курсы валют
    print("\nКУРСЫ ВАЛЮТ:")
    for currency, rate in exchange_rates.items():
        print(f"{currency}: {rate:.2f} руб.")
    
    # Выводим цены акций
    print("\nЦЕНЫ АКЦИЙ И КРИПТОВАЛЮТ:")
    for ticker, price in stock_prices.items():
        currency = " руб." if ticker in ["SBER", "GAZP", "TATN"] else " $"
        print(f"{ticker}: {price:.2f}{currency}")
    
    # Сохраняем ВСЁ в один файл
    today = datetime.now().strftime("%d.%m.%Y")
    
    with open('financial_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        # Заголовок
        writer.writerow(["Дата", "Тип", "Инструмент", "Значение", "Валюта"])
        
        # Валюта
        for currency, rate in exchange_rates.items():
            writer.writerow([today, "Валюта", currency, f"{rate:.2f}", "RUB"])
        
        # Акции
        for ticker, price in stock_prices.items():
            currency_type = "RUB" if ticker in ["SBER", "GAZP", "TATN"] else "USD"
            writer.writerow([today, "Акция/Крипто", ticker, f"{price:.2f}", currency_type])
        
        # Средние значения
        if exchange_rates:
            avg_currency = sum(exchange_rates.values()) / len(exchange_rates)
            writer.writerow([today, "Среднее", "Валюты", f"{avg_currency:.2f}", "RUB"])
        
        if stock_prices:
            avg_stock = sum(stock_prices.values()) / len(stock_prices)
            writer.writerow([today, "Среднее", "Акции/Крипто", f"{avg_stock:.2f}", "USD"])
    
    print(f"\n✅ Все данные сохранены в 'financial_data.csv'")
    print(f"   Дата обновления: {today}")
    
    # Тестовый скрипт
    print("\n" + "="*50)
    print("ДОПОЛНИТЕЛЬНОЕ ТЕСТИРОВАНИЕ:")
    print("="*50)
    
    test_tickers = ["AAPL", "SBER", "GAZP", "BTC", "UNKNOWN"]
    
    for ticker in test_tickers:
        print(f"\n--- {ticker} ---")
        price = get_stock_price(ticker)
        if price:
            print(f"Цена: {price}")
        else:
            print(f"Тикер не найден")
