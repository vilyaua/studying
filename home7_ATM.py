"""
ATM SERVICE
test task

Objective:
   Implement web-service for ATM using python3 and Flask web-framework.
The result of this task should be two files atm.py and test.py. First contains API implementation, second unittests for this API.

Description:
   User can check balance and withdraw cash using API. API provided by Flask-server via HTTP. Communication based on JSON format: user and server send JSONs to each other.

Requirements:
ATM for one user (no authorization required)
ATM has unlimited amount of cash.
Values of bills: 100$, 50$, 20$, 10$, 5$, 1$
Server keeps information about users balance in text file.
Implement API (application public interface) which consists of two methods:
GET balance
url: /atm/api/money
read information about balance from file
return JSON:
{
        “balance”: int
}
POST withdraw
url: /atm/api/money
calculate quantity of each bill (1, 2, 5, ...) depends on requested by user amount. If users balance less than requested amount return error: “You don’t have enaught money.” and HTTP status 403 Forbidden.
receive JSON:
{
        “amount”: int
    }
return JSON:
    {
        “cash”: {
    “100$”: int,      // if zero can be omitted
    “50$”: int,
    “20$”: int,
    “10$”: int,
    “5$”:int,
    “1$”:int
}
    }
if error return JSON:
    {
        “error”: “message”
}

Unittests:
Cover implemented methods by unittests. Place them into tests.py file.

Example:
> GET http://localhost:5000/atm/api/money
< 200 OK { “balance”: 500 }

> POST http://localhost:5000/atm/api/money
> { “amount”: “357” }
< 200 OK {
    “cash”: {
        “100$”: 3,
        “50$”: 1,
        “5$”: 1,
        “1$”: 2,
}
}

> GET http://localhost:5000/atm/api/money
< 200 OK { “balance”: 143 }

> POST http://localhost:5000/atm/api/money
> { “amount”: “200” }
< 403 Forbidden { “error”: “You don’t have enaught money.” }

Hints:
For development use JetBrains PyCharm IDE (Community edition is free!)
Install new frameworks and libraries using IDE: File/Preferences/ProjectInterpreter ...
Use an official Flask doc: http://flask.pocoo.org/
Place your API methods in different functions. Use ‘route’ decorators parameter ‘method’ to specify which request it handle POST or GET (read the docs for more info).
For easier testing divide your program into small separate methods which are responsible for undivided pieces of work.
To parse and serialize JSONs use standard pythons module “json”.

Good luck!

"""
import json
from flask import Flask, request

INIT = {'Vova': 865, 'Vasya': 2000, 'Sveta': 400, 'Petya': 2000}    # "базовые" балансы клиентов
FILE_NAME = "ATM.txt"                                               # текстовый файл с данными
VALUES = [100, 50, 20, 10, 5, 1]                                    # доступные номиналы в "банкомате"

app = Flask(__name__)

# функция возвращает последовательности "клиент: баланс" (dict)
def file_read():
    f = open(FILE_NAME, encoding="utf-8")       # открываем файл с данными для чтения
    lines = f.readlines()                       # считываем все строки в массив
    f.close()                                   # закрываем файл с данными
    rez = {}                                    # инициализируем словарь для дальнейшего заполнения
    for line in lines:                          # перебираем каждую строку из массива строк
        data = line.split(":")                  # разбиваем строку на пару элементов - до : и после
        rez[data[0]] = int(data[1][:-1])        # добавляем пару в словарь, избавляясь попутно от перевода строки
    return rez                                  # возвращаем словарь со всеми клиентами и их текущими балансами

# функция актуализирует файл с пользователями и их балансами, на вход принимается словарь с актуальными данными
def file_write(new_dict):
    f = open(FILE_NAME, mode="w", encoding="utf-8")     # открываем файл для перезаписи
    for key in new_dict:                                # перебираем кадлую пару словаря с актуальными данными
        f.write(key + ":" + str(new_dict[key]) + "\n")  # преобразовываем в текст и добавляем перевод строки
    f.close()                                           # закрываем файл с обновленными данными

# функция возвращает баланс заданного клиента (int), на вход принимаем имя клиента
def bal(client_name):
    data = file_read()                          # считываем данные всех клиентов и их балансов
    return data[client_name]                    # возвращаем целое число - баланс конкретного клиента

# возвращает JSON из номиналов и количества купюр, необходимых для выдачи требуемой суммы, либо ошибку
# на вход принимаем имя клиента, запрашиваемую сумму и доступные в "банкомате" номиналы
def cash(client_name, amount, values):
    data = file_read()                          # считываем данные всех клиентов и их балансов
    if client_name not in data:                 # проверяем, есть ли такой клиент
        return "No Such Client", 404                # если клиента нет, возвращаем 404 Page_Not_Found
    client_cash = data[client_name]             # запоминаем исходный баланс клиента
    if client_cash < amount:                    # проверяем, не превышает ли запрошенная сумма текущий баланс
        return "You don't have enough money", 403   # если денег недостаточно. возвращаем 403 Forbidden
    d = {}                                      # создаем пустой словарь
    amount_left = amount                        # остаток для выдачи (изначально он совпазает с запрошенной суммой
    for value in values:                        # перебираем все номиналы по порядку, определенному в константах
        key = str(value) + "$"                  # приводим ключ к заданному виду (номинал + символ $)
        value_num = int(amount_left / value)    # определяем количество купюр для выдачи остатка суммы
        if value_num != 0:                      # если номинал участвует в выдаче...
            d[key] = value_num                  # добавляем очередную пару в словарь
        amount_left -= value * value_num        # определяем остаток суммы, который еще нужно выдать
    data[client_name] = client_cash - amount    # изменяем остаток кликнта на выданную сумму
    file_write(data)                            # записываем новые значения пользователей и их балансов
    d_rez = {}
    d_rez["cash"] = d
    return json.dumps(d_rez)                    # конвертируем словарь в JSON и возвращаем

# обработчик POST-запроса
@app.route("/atm/api/money", methods=["GET"])
def balance():
    amount = bal("Vasya")                       # согласно ТЗ, проверяем баланс только одного Васи по GET
    d_rez = {}
    d_rez["balance"] = amount
    return json.dumps(d_rez)                    # возвращаем баланс согласно ТЗ

# обработчик POST-запроса
@app.route("/atm/api/money", methods=["POST"])
def withdraw():
    input_data = request.get_json()             # преобразовываем JSON в словарь
    client_name = input_data["client_name"]     # определяем имя клиента
    amount = input_data["amount"]               # определяем сумму, которую запрашивает клиент
    return cash(client_name, amount, VALUES)    # возвращаем результат функции Cash

#file_write(INIT)

if __name__ == "__main__":
    app.run()
