# 1
print("Привет, Яндекс!")

# 2
username = input()

print("Как Вас зовут?")
print("Привет,", username)

# 3
string = input()
print((string + '\n') * 3)

# 4
money = int(input())
cost = 38 * 2.5
result = int(money - cost)

print(result)

# 5
cost, weight, total_money = int(input()), int(input()), int(input())
result = int(total_money - (cost * weight))
print(result)

# 6
name, cost, weight, total_money = input(), int(input()), int(input()), int(input())
result = int(total_money - (cost * weight))
print(f'Чек\n{name} - {weight}кг - {cost}руб/кг')
print(f'Итого: {cost * weight}руб')
print(f'Внесено: {total_money}руб\nСдача: {result}руб')

# 7
n = int(input())
for i in range(n):
   print("Купи слона!")

# 8
n = int(input())
phrase = input()

for i in range(n):
   print(f'Я больше никогда не буду писать "{phrase}"!')

# 9
minutes = int(input())
kids = int(input())

if minutes >= 1 and kids >= 1:
   print((kids * minutes) // 2)

# 10
name = input()
number = input()

print(f'Группа №{number[0]}.')
print(f'{number[2]}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number[1]}.')

# 11
number = str(int(input()))
reverse_number = number[1] + number[0] + number[3] + number[2]
print(int(reverse_number))

# 12
num1 = list(map(int, input().rjust(3, '0')))
num2 = list(map(int, input().rjust(3, '0')))
num_0 = str((num1[0] + num2[0]) % 10)
num_1 = str((num1[1] + num2[1]) % 10)
num_2 = str((num1[2] + num2[2]) % 10)
print((num_0 + num_1 + num_2).lstrip('0'))

# 13
kids = int(input())
candy = int(input())

print(candy // kids)
print(candy % kids)

# 14
red, green, blue = int(input()), int(input()), int(input())
print(red + blue + 1)

# 15
hours = int(input())
minutes = int(input())
duration = int(input())

# 16
new_minutes = str((minutes + duration) % 60)
new_hours = str((hours + (minutes + duration) // 60) % 24)
print(f'{new_hours.rjust(2, "0")}:{new_minutes.rjust(2, "0")}')

# 17
A, B, C = int(input()), int(input()), int(input())

s = abs(A - B)
time = s / C

print(f'{time:.2f}')

# 18
earn = int(input())
last = int(input(), 2)
print(earn + last)

# 19
cost = int(input(), 2)
bill = int(input())

print(bill - cost)

# 20
item, price, weight, money = input(), int(input()), int(input()), int(input())
headings = ['Товар:', 'Цена:', 'Итого:', 'Внесено:', 'Сдача:']
values = [item, f'{weight}кг * {price}руб/кг', f'{weight * price}руб', f'{money}руб', f'{money - weight * price}руб']
print('Чек'.center(35, '='))
for i in range(len(headings)):
    print(f"{headings[i] : <10}{values[i] : >25}")
print('=' * 35)

# 21
weight, price, price_1, price_2 = int(input()), int(input()), int(input()), int(input())
weight_1 = int((price - price_2) * weight / (price_1 - price_2))
weight_2 = weight - weight_1
print(weight_1, weight_2)
