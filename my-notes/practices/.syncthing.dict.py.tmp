from random import randrange


def bet(dice, wager):
	"""下注
	:param: dice: 骰子点数
			wager: 用户的输入
	"""
	if dice == 7:
		# \n 是换行符号
		print(f'The dice is {dice};\nDRAW!\n')
		return 0
	elif dice < 7:
		if wager == 's':
			print(f'The dice is {dice};\nYou WIN!\n')
			return 1
		else:
			print(f'The dice is {dice};\nYou LOST!\n')
			return -1
	elif dice > 7:
		if wager == 's':
			print(f'The dice is {dice};\nYou LOST!\n')
			return -1
		else:
			print(f'The dice is {dice};\nYou WIN!\n')
			return 1

def main():
	# 可以用一个赋值符号分别为多个变量赋值.
	coin_user, coin_bot = 10, 10
	# 回合计数, 初始值为0
	rounds_of_game = 0

	while True:
		print(f'You: {coin_user}\t Bot: {coin_bot}')
		# 生成一个 2 到 12 的随机数.
		dice = randrange(2, 13)
		wager = input("What's your bet? ")

		if wager == 'q':
			break
		# 只有当用户输入的是 b 或者 s 的时候, 才"掷骰子".
		elif wager in 'bs':
			result = bet(dice, wager)
			coin_user += result
			coin_bot -= result
			rounds_of_game += 1
		if coin_user == 0:
			print("Woos, you've LOST ALL, and game over!")
			break
		elif coin_bot == 0:
			print("Woos, the robot's LOST ALL, and game over!")
			break
	print(f"You've played {rounds_of_game} rounds.\n")
	print(f"You have {coin_user} coins now.\nBye!")

if __name__ == '__main__':
	main()