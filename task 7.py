# Задача 7
# Найти произведение цифр числа.

mult = 1
number = int(input("Введите любое целое число: "))

while number != 0:
    mult *= number % 10
    number = number // 10
print("Произведение цифр числа:", mult)