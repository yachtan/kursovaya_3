import pytest
from utils.func import exec_operations
from utils.func import sorted_list
from utils.func import conclusion


def test_exec_operations():
    assert exec_operations([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED"},
                            {"id": 3, "state": "CANCEL"}, {}]) == [{"id": 1, "state": "EXECUTED"},
                                                                   {"id": 2, "state": "EXECUTED"}]

def test_sorted_list():
    assert sorted_list([{"id": 1, "date": "2019-08-26T10:50:58.294041"},
                        {"id": 2, "date": "2019-09-27T10:50:58.293031"},
                        {"id": 3, "date": "2017-08-01T10:50:58.000041"}]) == \
           [{"id": 2, "date": "2019-09-27T10:50:58.293031"},
            {"id": 1, "date": "2019-08-26T10:50:58.294041"},
            {"id": 3, "date": "2017-08-01T10:50:58.000041"}]


def test_conclusion():
    assert conclusion({"date": "2019-08-26T10:50:58.294041", "description": "Перевод организации",
                        "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589",
                        "operationAmount": {"amount": "31", "currency": {"name": "руб.", "code": "RU"}}}) == \
    '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31 руб.'
    assert conclusion({"date": "2019-07-21T10:50:58.294041", "description": "Открытие вклада",
                         "to": "Счет 64586473678894759588",
                         "operationAmount": {"amount": "50", "currency": {"name": "USD", "code": "USD"}}}) == \
    '21.07.2019 Открытие вклада\n[] -> Счет **9588\n50 USD'
    assert conclusion({"date": "2019-08-26T10:50:58.294041", "description": "Перевод с карты на карту",
                       "from": "Maestro 1596837868705199", "to": "Visa Platinum 8990922113665229",
                       "operationAmount": {"amount": "9", "currency": {"name": "руб.", "code": "RU"}}}) == \
           '26.08.2019 Перевод с карты на карту\nMaestro 1596 83** **** 5199 -> Visa Platinum 8990 92** **** 5229\n' \
           '9 руб.'
    assert conclusion({"date": "2019-08-26T10:50:58.294041", "description": "Перевод организации",
                       "from": "Счет 64686400678094779584", "to": "Счет 64686473678894779589",
                       "operationAmount": {"amount": "35", "currency": {"name": "руб.", "code": "RU"}}}) == \
           '26.08.2019 Перевод организации\nСчет **9584 -> Счет **9589\n35 руб.'
