def printer():
	print("\n    1   2   3")
	for i in range(3):
		print(' ', '-' * 13)
		print(f"{i + 1} ", end='')
		for j in range(3):
			print(f"| {signs[i][j]} ", end="")
		print("| ")
	print(' ', '-' * 13, '\n')

print('\n\nПриветсвую Вас в игре "Крестики-нолики"!')
print('Первыми ходят "Крестики"!')

flag = 1
signs = [['-' for i in range(3)] for j in range(3)]
printer()
while flag != 10:
	if flag % 2 == 1:
		print('Напишите через ПРОБЕЛ координаты (горизонталь, '
			'затем вертикаль),\nкуда хотите поставить "Крестик": ')
	else:
		print('Напишите через ПРОБЕЛ координаты (горизонталь, '
			'затем вертикаль),\nкуда хотите поставить "Нолик": ')
	coordinates = input().replace(" ", "")
	scnd, frst = int(coordinates[0]) - 1, int(coordinates[1]) - 1
	if len(coordinates) != 2 or frst < 0 or \
		frst > 2 or scnd < 0 or scnd > 2:
		print('\nСТОП! Вы ввели координаты неправильно!')
		print('Попробуйте еще раз...\n')
		printer()
		continue
	if signs[frst][scnd] != '-':
		print(f'\nСТОП! На этом месте уже стоит "{signs[frst][scnd]}"')
		print("Попробуйте еще раз... \n")
		printer()
		continue
	if flag % 2 == 1:
		signs[frst][scnd] = 'x'
	else:
		signs[frst][scnd] = 'o'
	printer()
	if (signs[0][0] == signs[1][0] == signs[2][0] == "x" or \
		signs[0][1] == signs[1][1] == signs[2][1] == "x" or \
		signs[0][2] == signs[1][2] == signs[2][2] == "x" or \
		signs[0][0] == signs[0][1] == signs[0][2] == "x" or \
		signs[1][0] == signs[1][1] == signs[1][2] == "x" or \
		signs[2][0] == signs[2][1] == signs[2][2] == "x" or \
		signs[0][0] == signs[1][1] == signs[2][2] == "x" or \
		signs[2][0] == signs[1][1] == signs[0][2] == "x"):
		print('Поздравляю! \nПобеду одержали "Крестики"!')
		break
	elif (signs[0][0] == signs[1][0] == signs[2][0] == "o" or \
		signs[0][1] == signs[1][1] == signs[2][1] == "o" or \
		signs[0][2] == signs[1][2] == signs[2][2] == "o" or \
		signs[0][0] == signs[0][1] == signs[0][2] == "o" or \
		signs[1][0] == signs[1][1] == signs[1][2] == "o" or \
		signs[2][0] == signs[2][1] == signs[2][2] == "o" or \
		signs[0][0] == signs[1][1] == signs[2][2] == "o" or \
		signs[2][0] == signs[1][1] == signs[0][2] == "o"):
		print('Поздравляю! \nПобеду одержали "Нолики"!')
		break
	# Я не понимаю, как сделать победу более красивым способом.
	# Буду очень рад, если Вы поможете мне с этим!
	flag += 1
	if flag == 10:
		print("Эх... Ничья!")
		print("Победила дружба :)")
		break