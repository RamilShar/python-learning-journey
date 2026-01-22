def calculate_bmi(weight, height):
    """
    Рассчитывает ИМТ по формуле: вес / (рост в метрах)^2
    Возвращает ИМТ и категорию
    """
    
    bmi = weight / (height * height) 
    if bmi < 18.5:
        print(bmi, "Недостаточный вес")
    elif 18.5 <= bmi < 25:
        print(bmi, "Нормальный вес")
    else:
        print(bmi, "Ожирение")
 
    pass

result = calculate_bmi(70, 1.75)
print(result)  # Должно показать: (22.86, "Нормальный вес")

def convert_temperature(value, from_scale, to_scale):
    """
    Конвертирует температуру между Цельсием (C) и Фаренгейтом (F)
    
    Формулы:
    C -> F: (value * 9/5) + 32
    F -> C: (value - 32) * 5/9
    """

    if from_scale == 'C' and to_scale == 'F':
        return (value * 9/5) + 32
    elif from_scale == 'F' and to_scale == 'C':
        return (value - 32) * 5/9
    else:
        return value
    pass

print(convert_temperature(0, 'C', 'F'))   # 32.0
print(convert_temperature(100, 'C', 'F')) # 212.0
print(convert_temperature(32, 'F', 'C'))  # 0.0


def check_password_strength(password):
    """
    Проверяет пароль по критериям:
    1. Длина не менее 8 символов
    2. Есть хотя бы одна цифра
    3. Есть хотя бы одна заглавная буква
    4. Есть хотя бы один спецсимвол (!@#$%^&*)
    
    Возвращает:
    - True и "Сильный пароль", если все критерии выполнены
    - False и сообщение об ошибке, если критерии не выполнены
    """

    if len(password) < 8:
        return False, "Пароль должен быть не менее 8 символов"
    if not any(char.isdigit() for char in password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    if not any(char.isupper() for char in password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    special_chars = "!@#$%^&*"
    if not any(char in special_chars for char in password):
        return False, "Пароль должен содержать хотя бы один спецсимвол (!@#$%^&*)"
    return True, "Сильный пароль"

    pass

# Тесты:
print(check_password_strength("Qwerty1!"))   # (True, "Сильный пароль")
print(check_password_strength("qwerty"))     # (False, "Пароль должен быть не менее 8 символов")
print(check_password_strength("qwerty123"))  # (False, "Пароль должен содержать хотя бы одну заглавную букву")


# Тестирование
if __name__ == "__main__":
    print("Тест 1 - ИМТ:", calculate_bmi(70, 1.75))
    print("Тест 2 - Температура:", convert_temperature(0, 'C', 'F'))
    print("Тест 3 - Пароль:", check_password_strength("Qwerty1!"))
