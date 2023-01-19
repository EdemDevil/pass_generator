#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Объявляем пустой список
list = []
#Перебираем список в диапозоне введенного числа
for letter in range(0, nr_letters):
    #Делаем случайную выборку из списка букв
    a = r.choice(letters)
    #Добавляем этот элемент в пустой список
    list.append(a)
for symbol in range(0, nr_symbols):
    a = r.choice(symbols)
    list.append(a)
for number in range(0, nr_numbers):
    a = r.randint(0, number)
    list.append(str(a))
#Перемешиваем элементы в списке и выводим его
a = r.shuffle(list)
print("".join(list))
