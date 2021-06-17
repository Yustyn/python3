"""1. Написати клас "Карточка на знижку" (DiscountCard), який містить наступну інформацію: 

Номер карточки 
Розмір знижки (знижка передбачається накопичуваною; на початковому етапі вона рівна 1%.
 За кожні 1000 грн. покупки, сума знижки збільшується на 1%.) 
Приховане допоміжне поле для збереження вартості накупленого товару 
Дата видачі карточки в форматі "12/02/1200") 
Забезпечити можливість: 
Купляти товар з використанням карточки на знижку; 
Виводити інформацію про поточну величину знижки; 
Виводити інформацію про те, на яку суму ще необхідно докупити товару, щоб величина знижки збільшилась. 
"""

from random import randint
from datetime import datetime as date


class Discont_Card:

    def __init__(self):
        self._id = randint(1000000000, 9999999999)
        self.__sum = 0
        self.discount = 0.01
        self._issueDate = date.today().strftime("%d/%m/%Y")

    def buy_something(self, price):
        self.__sum += price
        print(self.__sum - self.__sum * self.change_discount())

    def change_discount(self):
        self.discount = (self.__sum // 1000)/100
        return self.discount

    def print_discount(self):
        print(self.discount, '%')

    def to_increase(self):
        print(1000 - self.__sum % 1000)


dc = Discont_Card()

dc.buy_something(5100)

dc.print_discount()

dc.to_increase()
