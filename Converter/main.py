from online import get_currencies


available_currencies = get_currencies() # выгрузка словаря с доступными валютами


# Конвертер валют
def convert(amount, first_ticker, second_ticker, currencies):
    first_currency = currencies['data'].get(first_ticker) # исходная валюта
    second_currency = currencies['data'].get(second_ticker) # желаемая валюта

    coefficent = second_currency / first_currency # вычисление коэфициента конвертации
    return round(amount * coefficent, 2)



# Определение валюты
def input_currency(input_message, currencies):
    
    ticker = input(f'{input_message}: ').strip() # запрос валюты

    currency =  currencies['data'].get(ticker, None)
    while currency is None: # проверка существования валюты
        ticker = input(f'Ошибка при поиске валюты: {ticker}. Пожалуйста,\nпроверьте правильность написания валюты или выберите другую: ').strip() 
        currency =  currencies['data'].get(ticker, None)
    return ticker



# приветствие:
print('Здравствуйте! Это программа для конвертации валют!')

print("""
для работы с программой требуется:
- выбрать исходную валюту
- выбрать в какую валюту конвертируем
- ввести количество исходной валюты
      
Доступные валюты:
""")

# вывод списка доступных валют:
for currency in available_currencies['data']:
    print(f'- {currency}') 

# ввод исходной валюты:
first_ticker = input_currency('Введите исходную валюту', available_currencies)

# ввод желаемой валюты:
second_ticker = input_currency('Введите желаемую валюту', available_currencies)

# ввод конвертируемой суммы:
currency_amount_input = input('Введите сумму конвертации: ')
amount = None

# определения введенного типа данных:
while amount is None:
    try:
        amount = int(currency_amount_input.strip())
    except ValueError:
        try:
            amount = float(currency_amount_input.strip())
        except ValueError:
            currency_amount_input = input('Это не число. Пожалуйста, введите число: ')


# вычисление суммы конвертации:
result = convert(amount, first_ticker, second_ticker, available_currencies)

# вывод результата вычислений:
print(f'Результат: {amount} {first_ticker} = {result} {second_ticker}')