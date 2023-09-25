# 1
name, status = input(), input()
print('Как Вас зовут?', f'Здравствуйте, {name}!', 'Как дела?', sep='\n')
if status == 'хорошо':
    print('Я за вас рада!')
else:
    print('Всё наладится!')

# 2
petya_speed, vasya_speed = int(input()), int(input())
if petya_speed > vasya_speed:
    print('Петя')
else:
    print('Вася')

# 3
petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())
winner_speed = max(petya_speed, vasya_speed, tolya_speed)
if winner_speed == petya_speed:
    print('Петя')
elif winner_speed == tolya_speed:
    print('Толя')
else:
    print('Вася')

# 4
speed_p, speed_v, speed_t = int(input()), int(input()), int(input())

winner_speed = max(speed_p, speed_v, speed_t)
loser_speed = min(speed_p, speed_v, speed_t)
if winner_speed == speed_p:
    winner = 'Петя'
    if loser_speed == speed_t:
        loser, second = 'Толя', 'Вася'
    else:
        loser, second = 'Вася', 'Толя'
elif winner_speed == speed_t:
    winner = 'Толя'
    if loser_speed == speed_p:
        loser, second = 'Петя', 'Вася'
    else:
        loser, second = 'Вася', 'Петя'
else:
    winner = 'Вася'
    if loser_speed == speed_t:
        loser, second = 'Толя', 'Петя'
    else:
        loser, second = 'Петя', 'Толя'
for place in range(1, 4):
    print(f'{place}. {(winner, second, loser)[place - 1]}')

# 5
petya_apples, vasya_apples = int(input()), int(input())
if vasya_apples + 3 > petya_apples:
    print('Вася')
else:
    print('Петя')

# 6
year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print("YES")
    else:
        if year % 400 == 0:
            print("YES")
        else:
            print("NO")
else:
    print("NO")

# 7
number = input()
print("YES") if number[::-1] == number else print("NO")

# 8
land = input()
print('YES') if 'зайка' in land else print('NO')

# 9
names = input(), input(), input()
print(min(names))

#10
num = input()

sum_min = int(num[1]) + int(num[2])
sum_max = int(num[0]) + int(num[1])
result = ''

if sum_min < sum_max:
    result = result + str(sum_max) + str(sum_min)
else:
    result = result + str(sum_min) + str(sum_max)

print(int(result))

# 11
number = list(map(int, input()))
first = max(number) + min(number)
print('YES') if first == 2 * (sum(number) - first) else print('NO')

# 12
stick_1, stick_2, stick_3 = int(input()), int(input()), int(input())
if stick_1 < (stick_2 + stick_3) and stick_2 < (stick_1 + stick_3) and stick_3 < (stick_1 + stick_2):
    print('YES')
else:
    print('NO')

# 13
elf, dwarf, human = input(), input(), input()
if elf[0] == dwarf[0] == human[0]:
    print(elf[0])
elif elf[1] == dwarf[1] == human[1]:
    print(elf[1])

# 14
number = list(map(int, input()))
second = str(max(number)) + str(max(sorted(number)[:-1]))
if number.count(0) == 1:
    first = str(min(sorted(number)[1:])) + str(min(number))
elif number.count(0) == 2:
    first = second
else:
    first = str(min(number)) + str(min(sorted(number)[1:]))
second = str(max(number)) + str(max(sorted(number)[:-1]))
print(first, second)

# 15
number = list(map(int, (input() + input())))
print(str(max(number)) + str((sum(number) - max(number) - min(number)) % 10) + str(min(number)))

# 16
petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())
winner_speed = max(petya_speed, vasya_speed, tolya_speed)
loser_speed = min(petya_speed, vasya_speed, tolya_speed)
if winner_speed == petya_speed:
    winner = 'Петя'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Вася'
    else:
        loser, second = 'Вася', 'Толя'
elif winner_speed == tolya_speed:
    winner = 'Толя'
    if loser_speed == petya_speed:
        loser, second = 'Петя', 'Вася'
    else:
        loser, second = 'Вася', 'Петя'
else:
    winner = 'Вася'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Петя'
    else:
        loser, second = 'Петя', 'Толя'
print(f'{"": ^8}{winner: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{loser: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

# 17
a, b, c = float(input()), float(input()), float(input())
if not a and not b and not c:
    print('Infinite solutions')
elif not a and not b and c or b ** 2 < 4 * a * c:
    print('No solution')
elif b ** 2 == 4 * a * c:
    print(f'{-b / (2 * a):.2f}')
elif not a:
    print(f'{-c / b:.2f}')
else:
    roots = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
    roots.sort()
    print(f'{roots[0]:.2f} {roots[1]:.2f}')

# 18
sides = [int(input()), int(input()), int(input())]
sides.sort()
if sides[2]**2 == sides[0]**2 + sides[1]**2:
    print("100%")
elif sides[2]**2 > sides[0]**2 + sides[1]**2:
    print("велика")
else:
    print("крайне мала")

# 19
x, y = float(input()), float(input())
if (x**2 + y**2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 5 >= y >= 0:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 5 >= y >= 0 and 5 * x - 3 * y > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif 0.25 * x ** 2 + 0.5 * x - 8.75 <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')

# 20
text = [input(), input(), input()]
text.sort()

for item in text:
    if 'зайка' in item:
        print(item, len(item))
        break