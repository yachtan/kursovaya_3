import json
from datetime import date

def load_operations(file_name):
    '''Загружает данные по операциям из файла'''
    with open(file_name, 'r', encoding='utf-8') as file:
        all_operations = json.load(file)
    return all_operations


def exec_operations(all_operations):
    '''Возвращает список словарей с выполненными и не пустыми операциями'''
    exec_operations = []
    for item in all_operations:
        if item != {}:
            if item["state"] == "EXECUTED":
                exec_operations.append(item)
    return exec_operations


def sorted_list(list_of_operations):
    '''возвращает отсортированный список последних
    операций по убыванию по дате'''
    return sorted(list_of_operations, key=lambda x: x["date"], reverse=True)


def conclusion(operation):
    '''возвращает информацию по операциям в виде:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>'''
    rev_date = date.fromisoformat(operation["date"][0:10]).strftime('%d.%m.%Y')

    if "Счет" in operation["to"]:
        rev_to = 'Счет **' + operation["to"][-4:]
    else:
        rev_to = operation["to"][0:-12] + ' ' + operation["to"][-12:-10] + '** **** ' + operation["to"][-4:]

    if "from" not in operation.keys():
        rev_from = '[]'
    else:
        if "Счет" in operation["from"]:
            rev_from = "Счет **" + operation["from"][-4:]
        else:
            rev_from = operation["from"][0:-12] + ' ' + operation["from"][-12:-10] +'** **** ' + operation["from"][-4:]

    return (f'{rev_date} {operation["description"]}\n'
            f'{rev_from} -> {rev_to}\n'
            f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}')
