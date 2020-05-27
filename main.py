

#Importing standard modules
from datetime import datetime
import sys
import art
import os
import time
import colorama
import getkey
appsopened=list()
storage = int(os.path.getsize('ballcollecter.py')) + int(os.path.getsize('calculator.py')) + int(os.path.getsize('commandterm.py')) + int(os.path.getsize('devtools.py')) + int(os.path.getsize('fightgame.py')) + int(os.path.getsize('gamehub.py')) + int(os.path.getsize('gmail.py')) + int(os.path.getsize('inspyre.py')) + int(os.path.getsize('timer.py')) + int(os.path.getsize('wordbomb.py')) + int(os.path.exists('main.py'))
#Booting varibles
def clear():
	os.system('clear')
clear()
logo = True
explorer = False
network = '810g4'
while True:
	if logo == True:
		print(art.text2art("PythonOS"))
	else:
		pass
	datnow = datetime.now()
	hour = int(datnow.strftime('%H'))-4
	time1 = datnow.strftime('%A, %B %d, %Y ')
	time2 = datnow.strftime(':%M:%S')
	if explorer == True:
		print(colorama.Fore.RED, '[!] You are in Explorer mode.')
		print(colorama.Style.RESET_ALL, ' ')
	else:
		pass
	print(f'{time1}{hour}{time2}                        Version: Alpha 1.1.3')
	print('----------------------------------------------------------------------------------')
	print('Apps: ')
	print('⏲️  [T] Timer App')
	print('🖥️  [D] Open Dev Tools')
	print('🎮  [G] Game Hub')
	print('💡  [!] See new update info')
	print('ℹ️  [?] Help\n')
	print('======Task Manager======')
	print('⬆️  [U] Update Console')
	print('📟  [/] Open Command Terminal')
	print('⚙️  [%] Settings')
	print('💻  [S] Shutdown\n')
	print('======Stats======')
	print(f'Storage: {storage}P')
	signal = os.cpu_count()
	if signal == 1:
		print(colorama.Fore.RED, f'PyGlobal signal strength: ' + 'o'*signal)
	elif signal == 2:
		print(colorama.Fore.YELLOW, f'PyGlobal signal strength: ' + 'o'*signal)
	elif signal == 3:
		print(colorama.Fore.LIGHTYELLOW_EX, f'PyGlobal signal strength: ' + 'o'*signal)
	elif signal == 4:
		print(colorama.Fore.GREEN, f'PyGlobal signal strength: ' + ')'*signal)
	print(colorama.Fore.RESET, 'Press CTRL-C to exit an app.\n')
	app = getkey.getkey().upper()
	os.system('clear')
	#Boot apps
	if app == 'T':
		clear()
		import timer
		storage += 0.02
		appsopened.append('Timer 0.02P')
		pass
	elif app == 'G':
		clear()
		import gamehub
	elif app == 'D':
		clear()
		import devtools
		pass
	elif app == '!':
		clear()
		try:
			updates = open('updateinfo.txt', 'r')
			print(updates.read())
			time.sleep(10)
			clear()
		except KeyboardInterrupt:
			clear()
			pass
	elif app == '/':
		import commandterm
	elif app == 'U':
		clear()
	elif app == '?':
		try:
			import time
			clear()
			print('PythonOS is a open-source project that I made.')
			print('To enter an app, type the letter you see next to the app.')
			print('For example, ')
			print('[T] Timer app')
			print('Type \'T\' to open the timer app.')
			print('Do CTRL-C to exit an app.')
			print('Follow me on Repl.it: @LoganSpong')
			time.sleep(10)
		except KeyboardInterrupt:
			clear()
			pass
	elif app == '%':
		try:
			clear()
			print(f'[L] Logo: {logo}')
			print(f'[W] PyGlobal Network: {network}')
			print(f'[E] Explorer Mode: {explorer}')
			setting = getkey.getkey().upper()
			if setting == 'L':
				if logo == False:
					logo = True
				else:
					logo = False
				clear()
			elif setting == 'E':
				if explorer == True:
					explorer = False
				else:
					import colorama
					print(colorama.Fore.RED, '[!] You are entering Explorer mode. Are you sure? ')
					print(colorama.Style.RESET_ALL, ' ')
					explorercheck = input(' ')
					if explorercheck == 'y':
						explorer = True
					else:
						explorer = False
				clear()
			elif setting == 'W':
				clear()
				wifi = input('Configure PyGlobal network: ')
				if wifi == '52E5F':
					network = '52E5F'
					print('Connecting to \"TP-LINK\"..')
					time.sleep(2)
					print('Configuring..')
					time.sleep(1)
					print('Done!')
					time.sleep(1)
					clear()
					pass
				elif wifi == '52E5F' and explorer == True:
					network = '52E5F_5G'
					print('Connecting to \"TP-LINK_5G\"..')
					time.sleep(2)
					print('Configuring..')
					time.sleep(1)
					print('Done!')
					print(colorama.Fore.RED, '[!] ' + colorama.Style, 'You are in Explorer mode. This network may be unstable.')
					time.sleep(1)
					clear()
					pass
			else:
				print('Invaild Setting.')
		except KeyboardInterrupt:
			clear()
			pass
	elif app == 'S':
		import os
		import time
		os.system('clear')
		print('PythonOS is shutting down..')
		time.sleep(3)
		import os
		os.system('clear')
		print('PythonOS is shut down. Press \'S\' again to revive it.')
		recov = getkey.getkey().upper()
		if recov == 'S':
			import os
			os.system('clear')
			pass
		else:
			print(colorama.Fore.RED, f'ConnectionError: PythonOS lost connection with PyGlobal network: {network} at time: {hour}{time2}')
			break
	else:
		try:
			import time
			clear()
			print('Unknown app.')
			time.sleep(3)
			clear()
		except KeyboardInterrupt:
			clear()
			pass
		