
from colorama import Fore, Style
import time
import sys
from random import randint, choice
def scrollTxt(text):
	for char in text:
		delay=10
		time.sleep(delay/100)
		sys.stdout.write(char)
		sys.stdout.flush()
scrollTxt('Dr.Mech: Are you ready? I don\'t think you are. The apocalypse is here.\n')
scrollTxt('You: Ok? Who are you?\n')
scrollTxt('Dr.Mech: I was the one who saved you from that zombie back there. Remember?\n')
scrollTxt('You: Nope. And, you didn\'t answer my question. Who are you?\n')
scrollTxt('Dr. Mech: A doctor. That\'s all.\n')
scrollTxt('You: You don\'t seem like a person you would just say: \"That\'s all\".\n')
scrollTxt('You: I mean, You said \"I saved you from those zombies.\"\n')
scrollTxt('You: Why do I even trust you?\n')
scrollTxt('Dr.Mech: I saved you. That\'s why you should trust me.\n')
scrollTxt('You: Which is the exact reason I don\'t trust you.\n')
scrollTxt('You: Why should I?\n')
scrollTxt('Dr.Mech: Be glad that you\'re ALIVE. Ok? Happy?\n')
scrollTxt('You: Fine. But, what is happening?\n')
scrollTxt('Dr.Mech: Zombie apocalypse.\n')
scrollTxt('You: You say that with such a chill voice. I mean, like, ZOMBIE apocalypse!\n')
scrollTxt('Dr.Mech: Watch out!\n')
reset=Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.LIGHTYELLOW_EX
normal = Fore.WHITE
attack = '[X]'
alert = '[!]'
armor = str()
health=100
weapons=['Fist']
damages=[20,25]
allweapons=['Fist', 'stone sword', 'Iron sword']
monsters=['zombie', 'Sewer rat']
newweapons=[' ','Stone Sword']
print('Fight!')
battlegoing=True
monsterhealth=75
areas=['The Field', 'The Trash Alley']
monster=monsters[0]
monsterstrength=10
area=0
while battlegoing:
	pickweapon=input(f'Pick a weapon: {weapons}\n')
	if pickweapon in weapons:
		damage=randint(1,damages[weapons.index(pickweapon)])
		print(yellow, '\n[!]' + normal,'You did' + green, str(damage) +  ' damage' +  normal, '!')
		monsterhealth-=damage
	elif pickweapon in allweapons and pickweapon!=weapons:
		print('You do not have that weapon yet.\n')
		continue
	else:
		print('That is not a weapon.\n')
		continue
	print(f'{monster.title()} health: {monsterhealth}')
	move=input('\x1B[3mContinue...\x1B[23m')
	damage=randint(1,monsterstrength)
	print('\n' + red, attack + normal, f'The {monster} did' + red, str(damage) + ' damage' +  normal, '!')
	health-=damage
	print(f'Health: {health}')
	if health<0:
		print('You died.')
		battlegoing=False
	elif monsterhealth<0:
		print('You Won!.')
		win=True
		area+=1
		print(f'New weapon: {newweapons[area]}')
		weapons.append(newweapons[area])
		print('Continue..')
		
		if area==12:
			print('You win the game!')
			print('I hope you enjoyed this game.')
			print('Check out my profile on Repl.it: @LoganSpong')
			print('Good-Bye!')
		while win:
			actions=['1) Forward to new area', '2) Look for items', '3) Look in your backpack','Q)Quit.']
			select=input(f'Select an action: {actions}')
			if select=='1':
				print(f'You walk to {areas[area]}')
				battlegoing=True
				monster=monsters[1]
				monsterhealth=100
				monsterstrength=20
				win=False
			elif select=='2':
				finds=['Apple +25 Health', 'nothing', 'Leather Armor +5 Armor', 'nothing']
				find=f'You found: {choice(finds)}'
				print(find)
				if find=='Apple +25 Health':
					health+=25
					win=False
					monster=monsters[1]
					monsterhealth=100
					monsterstrength=20
					battlegoing=True
				elif find=='Leather Armor +5 Armor':
					monsterstrength-=5
					win=False
					monster=monsters[1]
					monsterhealth=100
					monsterstrength=20
					battlegoing=True
				elif find=='Nothing':
					pass
					win=False
					monster=monsters[1]
					monsterhealth=100
					monsterstrength=20
					battlegoing=True
			elif select=='3':
				items=['Pizza +50 Health', 'Tethered Shirt +1 Armor', '3) Back']
				itemuse=input(f'Use an item: {items}')
				if itemuse=='Pizza':
					print('You gained +50 Health!')
					win=False
					monster=monsters[1]
					monsterhealth=100
					monsterstrength=20
					battlegoing=True
			elif select=='Q':
				print('Quitting resets all your progress. Are you sure? (y/n)')
				quit=input(' ')
				if quit=='y':
					break
				else:
					continue