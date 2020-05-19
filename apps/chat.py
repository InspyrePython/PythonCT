
ChatAppOpened=True
while ChatAppOpened:
	try:
		
		import time
		import json
		import random
		from colorama import Fore
		import os

		from datetime import datetime
		serverIDfile=open('serverID.txt','w+')
		serverIDfile='serverID.txt'
		with open(serverIDfile,'w')as f:
			serverID=random.randint(1, 128222)
			json.dump(chr(serverID), f)
		server=True
		#Setup
		#Emoji Data:
		avatar=chr(128113)
		joinava=chr(128075)
		groupchat=chr(128490)
		waiting=chr(9202)
		stop=chr(128721)
		loading=chr(9881)*3
		yay=chr(127881)
		serverlock=chr(128274)
		serverunlock=chr(128275)
		mainemojis=[128113, 128075, 128490, 9202, 128721, 9881, 127881]
					#happy, sad, angry, thumbs-up, thumbs-down, highfive, laughing
		emoji=[128512, 128546, 128544, 128077, 128078, 9995, 129315]
		users=list()
		reports=0
		while server==True:
			print(f'{loading} Establishing connection...')
			time.sleep(1)
			print(f'{loading} Loading...')
			time.sleep(1)
			print(f'{yay} Connected!')
			print('Type \"/join\" to introduce yourself!')
			print('Type \"/help\" to see a list of commands.')
			print('Using version \'Alpha 1.5\' of Python Console Chat.')
			group=input('What is the group name?\n')
			chatrunning=True
			print(f"{groupchat}  Group name: {group}\n")
			for i in range(100):
				user=input('What is your name?\n')
				if user != 'start': #Chat start screen
					users.append(user)
					print(f"{joinava}   {user} joined the chat!")
					print(f"{waiting}   Waiting for users..")
					print('Type \"start\" to start the chat.\n')
				elif user=='start':
					time.sleep(3)
					print(f"{loading}  Starting chat..")
					print('Enjoy!')
					print('\n\n\n\n\n\n\n\nw\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
					print('Chat: \n')
					server=False
					class commands:
						def clear():
							print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
					class time:
						def weekday():
							now=datetime.datetime.now()
							print(now.strftime("%A"))
						def day():
							now=datetime.datetime.now()
							print(now.strftime("%d"))
						def time():
							now=datetime.datetime.now()
							print(now.strftime("%I:%M:%S%p"))
					while chatrunning: #(void) loop ({})
						chat=input('\b')
						name=input('Name:')
						if name in users:
							print(f"{avatar}  {name}: {chat}\n") 
							vailduser=True
						elif chat=='/join':
							vailduser=True
						else:
							print(f'{stop}  User not found.')
							print('Type \"/join\" to introduce yourself!')
						if chat=='/clear':
							commands.clear()
						elif chat=='/emoji man':
							avatar=chr(128113)
							print('Changed the avatar to a man.')
						elif chat=='/emoji woman':
							avatar=chr(128105)
							print('Changed the avatar to a woman.')
						elif chat=='/help':
							print(Fore.GREEN, 'PCC Server 1: ')
							print('Type \"/clear\" to clear the chat.')
							print('Type \"/emoji man\" to change the emoji to a man.')
							print('Type \"/emoji woman\" to change the emoji to a woman.')
							print('Type \"/ban\" to stop the chat.')
							print('Type \"/color\" to color your chat.')
							print('Type \"/report\" to report an issue to me.')
							print('Type \"/reportuser\" to report a user. Warning! This will stop the chat after 2 or more reports.')
							print('Type \"/serverlock\" to lock the server.')
							print('Type \"/serverunlock\" to unlock the server.')
							print('Type \"/info\" to get info about this project.')
							print('Type \"/serverID\" to get the serverID.\n\n\n\n')
						elif chat=='/stop':
							chatrunning=False
						elif chat=='/join':
							name=name.title()
							if name in users:
								print('You have already joined!')
							else:
								print(f"{avatar} {name} joined the chat!")
								users.append(name)
						elif chat=='/ban':
							chatrunning=False
							os.remove("serverID.txt")
						elif chat=='/report':
							issue=input('What is the issue?')
							import json
							with open('issuses.txt','w')as f:
								json.dump(issue, f)
						elif chat=='/reportuser':
							reports+=1
							print(Fore.RED, f'PCC Server 1: Someone has been reported! If that person is you, stop!')
							if reports==2 or reports>2:
								chatrunning=False
						elif chat=='/color':
							from colorama import Fore
							color=input('What color would you like it to be?')
							if color=='red':
								chat=input('\n')
								name=input('Name: ')
								print(Fore.RED, f"{avatar}  {name}: {chat}")
							elif color=='yellow':
								chat=input('\n')
								name=input('Name: ')
								print(Fore.YELLOW, f"{avatar}  {name}: {chat}")
							elif color=='green':
								chat=input('\n')
								name=input('Name: ')
								print(Fore.GREEN, f"{avatar}  {name}: {chat}")
							elif color=='blue':
								chat=input('\n')
								name=input('Name: ')
								print(Fore.BLUE, f"{avatar}  {name}: {chat}")
						elif chat=='/info':
							print('Emojis from: https://emojipedia.org/')
							print('Built by: Logan Spong.')
							print('Repl.it: @LoganSpong')
						elif chat=='/serverlock':
							if server==False:
								print(Fore.GREEN, 'PCC Server 1:  Server already locked!')
							else:
								print(Fore.GREEN, f'PCC Server 1: {serverlock}   Locking Server... Hold on..')
								server=False
						elif chat=='/serverunlock':
							if server==True:
								print(Fore.GREEN,'PCC Server 1: ' ' Server already unlocked!')
							else:
								print(Fore.GREEN,f'PCC Server 1: {serverunlock} Unlocking Server... Hold on..')
								server=True
						elif chat=='/serverID':
							f = open(serverIDfile, 'r')
							print('PCC Server 1: ' + str(f.read()))
						elif chat=='/users':
							print(users)
						elif chat=='/groupname':
							print(group)
						elif chat=='/changegroupname':
							group=input('New group name: ')

	except KeyboardInterrupt:
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		ChatAppOpened=False
