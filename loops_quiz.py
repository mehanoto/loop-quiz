# -*- coding: utf-8 -*-
"""Loops_quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1znlgPnT-Y9aqD16gjCr_OyTLh2Y5N-Dj

## Цикли. Упражнение/изпитване.

**Задача 1:** Допълнете кода, така че да изведе числата от 7 до -3.
"""

number = _
while number >= _:
	print(number, end=" ")
	number -= _

"""**Задача 2:** Функцията show_letters приема стринг като входен параметър, и трябва да принтира всички символи съставящи стринга, всеки на нов ред от първия към последния. Допълнете кода, така че да съответства на горното описание."""

def show_letters(word):
	for _ in _:
		print(_)

show_letters("Hello")
# Should print one line per letter

"""**Задача 3:** Допълнете функцията digits(n), която връща броя на цифрите в числото n. Примерно: 25 има 2 цифри, 144 има 3 цифри. Подсказка: можете да разберете броя на цифирите делейки на 10, докато резултатът стане по-малък от 0.


**Забележка** Функцията работи само с цели положителни числа.
"""

def digits(n):
	count = 0
	if n _ 10:
	  return 1
	while n >= _ :
		count += _
		n = _/_
	return count

print(digits(25.44))   # Трябва да принтира 2
print(digits(144))  # Трябва да принтира 3
print(digits(1000)) # Трябва да принтира 4
print(digits(9999)) # Трябва да принтира 4
print(digits(0))    # Трябва да принтира 1

"""**Задача 4:** Тази функция принтира квадрат от числа с размерност n x n. Числата във квадрата съответстват на номера на колоната, примерно всички числа във втора колона имат стойност 2, всики числа в първа колона имат стойност 1-ца и т.н.

Квадрат с размерност 3х3

1 2 3

1 2 3

1 2 3
"""

def print_square(n):
	for r in range(_, _):
		for c in range(_, _):
			print(_, end=" ")
		print()

print_square(3)

"""**Задача 5:** Функцията counter изброява последователно целите числа от началното към крайното. Когато началното(start) е по-малко или равно от крайното(stop), изписва "Counting up: start, start + 1, ..., stop. Примерно извикване към counter(1, 3), трябва да върне като резултат стринга "Counting up: 1, 2, 3". Обратно, ако числото start e по-голямо от stop, функцията трябва да върне стринг "Counting down: start, start-1, ..., stop". Примерно извикване към counter(3, 1), трябва да върне като резултат стринга "Counting down: 3, 2, 1".


"""

def counter(start, stop):
	x = start
	if _ > _:
		return_string = "Counting down: "
		while x __ stop:
			return_string += str(_)
			if x != stop: #след междинните числа трябва да добавим запетая
				return_string += "_"
			x _= _
	else:
		return_string = "Counting up: "
		while x __ stop:
			return_string += str(_)
			if x != stop:#след междинните числа трябва да добавим запетая
				return_string += "_"
			x _= _
	return return_string

print(counter(1, 10)) # Трябва да принтира "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Трябва да принтира "Counting down: 2,1"
print(counter(5, 5)) # Трябва да принтира "Counting up: 5"

"""**Задача 6:** Функцията loop е подобна на range(): Приема 3 параметъра: начална точка start, крайна точка stop, и стъпка step. Ако началната точка е по-голяма от крайната, задава отрицателна стъпка. Обратно, когато началната точка е по-малка от крайната, задава положителна стъпка. Също така ако стъпката е 0, автоматично я прави 1 или -1 в зависимост от ситуацията. Резултатът е стринг от числа разделени с интервали. Примерно, loop(11,2,3), трябва да върне "11 8 5", loop(1,5,0) трябва да върне "1 2 3 4". Също както при range, крайното число stop се пропуска. Допълнете функцията по-долу, така че да се държи според описанието.

**Забележка** Стандартната функция abs(n) връща абсолютната стойност на подадения параметър n. abs(5) -> 5, abs(-5) -> 5
"""

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = _
	if start > stop:
		step = abs(_) * -1
	else:
		step = abs(_)
	for count in range(start,stop,step):
		return_string += str(_) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24
print(loop(1,1,1)) # Should be empty

"""**Задача 7:** Фермер е произвел реколта от 20т. ябълки през 2001 година. Всяка следваща година реколкотата му се увеличава с 5 процента. Допълнете програмата по-долу, така че да принтрира през коя година реколкотата на фермера ще надвиши 130т. Ако сте работили правилно вашият скрипт трябва да отпечата "The year that the harvest exceeds 130 tones is: 2007"."""

harvest = _
year = 2001
while harvest _ _ :
  year += 1
  harvest = harvest * _
print("The year that the harvest exceeds 130 tones is: " + str(year))