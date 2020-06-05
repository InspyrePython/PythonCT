

from flask import Flask
import time
import os
from colorama import Fore
users = list()
exit = True
import os
a = 'hello'
folder = ' '
while exit:
	orange = '\u001b[33m'
	green = '\u001b[92m'
	reset = "\u001b[0m"
	commandstyle =  f'\u001b[33mpythonos \u001b[33m' + f'{green}$ {green}'
	command = input(commandstyle)
	print(f'{reset}')
	if 'setup -' in command:
		flagstr = command[command.index('-') + 1]
		flag = command.index('-') + 1
		if flagstr == 't':
			filename = command[flag + 1 : len(command)] + '.txt'
			f = open(filename, 'w+')
		if flagstr == 'v':
			app = Flask('app')
			@app.route('/')
			def appsym():
				return 'Virtual Environment <br> Press CTRL-C to exit a virtual environment.'
			app.run(host='0.0.0.0', port=8080)
			os.system('clear')
			command = input(f'${folder}')
	elif 'goto@ ' in command:
		flagstr = command[command.index('@') + 1: len(command)] + '.txt'.replace('\t', '\b ').strip()
		f = open(flagstr, 'a')
		write = input(f'$ {flagstr} WRITE')
		f.write(write)
		f.close()
	elif 'delete@ ' in command:
		flagstr = command[command.index('@') + 1 : len(command)] + '.txt'
		try:
			os.remove(flagstr)
		except FileNotFoundError:
			print(f'No file found named: {flagstr}.')
	elif 'read@ ' in command:
		flagstr = command[command.index('@') + 1 : len(command)] + '.txt'
		try:
			f = open(flagstr, 'r')
			print(f.read().strip())
		except FileNotFoundError:
			print(f'No file found named: {flagstr}.')
	elif 'venv -' in command:
		flagstr = command[command.index('-') + 1]
		flag = command.index('-') + 1
		if flagstr == 'e':
			try:
				f = open('appconfig.txt', 'r')
				g = open('appconfig.txt', 'a')
			except FileNotFoundError:
				h = open('appconfig.txt', 'a')
				f = open('appconfig.txt', 'r')
				g = open('appconfig.txt', 'a')
				continue
			try:
				edit = input('venv app EDIT ')
			except KeyboardInterrupt:
				break
			if edit == 'refresh':
				continue
			else:
				g.write(edit)
				app = Flask('app')
				@app.route('/')
				def appsym():
					return f.read()
				app.run(host='0.0.0.0', port=8080)
		elif flagstr == 'r':
			app.run(host='0.0.0.0', port=8080)
		elif flagstr == 'd':
			g = open('appconfig.txt', 'w')
			g.write('Virtual Environment <br> Press CTRL-C to exit a virtual environment.')
	elif command == 'exit':
		exit = False
	elif command == 'help':
		print(open('info.txt', 'r').read())
	elif command == '@cpu.self/count':
		print(os.cpu_count())
	elif command == '@pyglobal.self/shutdown':
		# Insert shutdown here
		pass
	elif command == '@bytepath.self/get':
		byte = True
		from random import randint
		while byte:
			try:
				print(bin(randint(-2**200, 2**200)))
			except KeyboardInterrupt:
				byte = False
				os.system('clear')

	elif command == '@pyglobal.self/strength':
		print(os.cpu_count())
	else:
		import time
		print(f'Unknown command: {command}')
		time.sleep(2)
		os.system('clear')
