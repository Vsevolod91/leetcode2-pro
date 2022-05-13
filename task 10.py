# Задача 10
# Найти количество цифр 5 в числе

number = int(input("Введите любое число: "))
count = 0

while number != 0:
    digit = number % 10
    if digit == 5:
        count += 1
    number = number // 10
print(count)

