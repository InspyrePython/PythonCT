
#Importing standard modules
from datetime import datetime
import sys

#Booting varibles
while True:
	datnow = datetime.now()
	hour = int(datnow.strftime('%I'))-4
	time1 = datnow.strftime('%A, %B %d, %Y ')
	time2 = datnow.strftime(':%M:%S %p')
	def clear():
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	clear()
	print('Welcome to PythonOS. This is an open-source project made by Tobin MicroSystems.')
	print(f'{time1}{hour}{time2}                        Version: InDev 1.12')
	print('----------------------------------------------------------------------------------')
	print('Apps: ')
	print('[T] Timer App')
	print('[P] Python Console Chat')
	print('[D] Open Dev Tools\n')
	print('======Task Manager======')
	print('[U] Update Console (No waitime!)')
	print('[/] Open Command Terminal\n')
	sys.stdout.flush()
	app = input('')
	#Boot apps
	if app == 'T':
		clear()
		import apps.timer
	elif app == 'P':
		clear()
		import apps.chat
	elif app == 'C':
		clear()
		import apps.calculator
	elif app == 'D':
		clear()
		import apps.devtools.devtools
	elif app == '/':
		clear()
		print('================PyOS Command Terminal=================')
		command = input('--PyOS user ')
		if command == 'install python3 inspyre':
			import sys
			print('Installing Inspyre..')
			for i in range(1, 11):
				import time
				j=9-i
				time.sleep(1)
				sys.stdout.write('[' + '#'*i + ' '*j + ']')
				sys.stdout.write('\u001b[1000D')
				sys.stdout.flush()
		elif command == 'open taskmanager':
			print('Work in progress. Command will come in Alpha 1.2')
		else:
			print('Unknown Command.')
	sys.stdout.flush()
