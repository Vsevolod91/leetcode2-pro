# Задача 6
# Найти сумму цифр числа.

number = int(input("Введите любое целое число: "))
sum = 0
while number != 0:
    sum += number % 10
    number = number // 10
print("Сумма цифр числа равна: ", sum)
