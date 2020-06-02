
import time
def clear():
	import os
	os.system('clear')
clear()
print('================PyOS Command Terminal=================')
commandstart = Fore.LIGHTYELLOW_EX, 'pyosct> ', Fore.GREEN, '$'
command = input(commandstart)
if command 