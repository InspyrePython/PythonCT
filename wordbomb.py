
def game():
	menu=list()
	lives=3
	points=0
	print('Type something and DONT TYPE IT AGAIN!')
	while True:
		word=input('')
		print('Do not type ' + word + ' again.')
		menu.append(word)
		if word in menu:
			a=menu.count(word)
			if a==2:
				print('OH NO!')
				lives-=1
				print('Lives ' + str(lives))
			elif a==3:
				print('OH NO!')
				lives-=1
				print('Lives ' + str(lives))
			elif a==4:
				print('OH NO!')
				lives-=1
				print('Lives ' + str(lives))
			if lives == 0 or lives < 0:
				print('You lose!')
				print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ')
				x=input('x')
				if x=='y':
					game()
					break	
			points+=1
			point='               Points '
			print(point + (str(points)))
game()
