"""
Некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них."""
a = int(input("Введите количество учеников в классе А: "))
b = int(input("Введите количество учеников в классе Б: "))
c = int(input("Введите количество учеников в классе В: "))

res = (a + b + c)/2
print(round(res))

