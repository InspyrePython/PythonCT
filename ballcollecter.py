
import random
balls=list()
ownedballs=list()
installs=['Not Installed', 'Not Installed']
f = open('games/balls.txt', 'r')
for i in range(28):
	balls.append(f.readline())
while True:
	move=input('Choose an action:\n[1] Look for a ball.\n[2] See your collection.\n[3] Suggest a ball.\n[4] Shop\n')
	if move=='1':
		randomball=random.choice(balls)
		print(f'\n\n\n\nYou got: {randomball}')
		print(f'Ball #: {balls.index(randomball)}/{len(balls)}\n\n')
		ownedballs.append(randomball)
	elif move=='2':
		coveredballs=list()
		print('\n\n\n\n\n\n')
		for i in range(len(ownedballs)):
			ball=ownedballs[i]
			if ownedballs.count(ball) > 2 or ownedballs.count(ball) == 2 and ball not in coveredballs:
				coveredballs.append(ownedballs[i])
				print(f'{ownedballs[i]} x {ownedballs.count(ball)}')
				continue
			elif ball in coveredballs:
				print('\t')
			else:
				print(ball)
	elif move=='3':
		g = open('games/suggestaball.txt', 'a')
		ballsuggest=input('Suggest a ball: \n')
		if ballsuggest!='None':
			g.write(ballsuggest + '\n')
			print('Now, to load the ball, type 3 again. Then, when your it the suggest a ball screen, type None.')
		else:
			print('Ball loaded to \"suggestaball.txt\".')
	elif move=='4':
		print('\n\n====Shop====')
		print('Packs: ')
		print('Medical Pack: ')
		print('Get balls like: \n')
		print('The Corona Ball')
		print('The Virus Ball')
		print('Installed\n\n')
		print('Superhero Pack: ')
		print('Get balls like: \n')
		print('The Superman Ball')
		print('The Joker Ball')
		print('Installed\n\n')
		print('The Coder Pack:\n')
		print('Get balls like: \n')
		print('The Java Ball')
		print('The Python Ball')
		print(f'{installs[0]}\n\n')
		print('The Repl.it Pack:\n')
		print('Get balls like: \n')
		print('The Tomato Pie Ball')
		print('The Squid Ball')
		print(f'{installs[1]}\n\n')
		print('If you get a code, enter it here, and you will get a pack.')
		install=input(' ')
		if install=='Repl.it Ball':
			print('You installed the \'Repl.it Pack\'.')
			balls.append('')