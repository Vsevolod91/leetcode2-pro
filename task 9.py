# Задача 9
# Найти максимальную цифру в числе

number = int(input("Введите любое число: "))
max_digit = 0

while number != 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print(max_digit)
