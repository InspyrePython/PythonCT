
InspyreAppOpened=True
while InspyreAppOpened:
	try:
		def add(num1, num2): #Addtion
			answer=num1 + num2
			return(answer)
		def sub(num1, num2): #Subtraction
			answer=num1 - num2
			return(answer)
		def mul(num1, num2): #Multiplication
			answer=num1 * num2
			return(answer)
		def div(num1, num2):
			answer=num1 / num2
			return(answer)
		def mod(num1, num2): #Modulus function
			answer=num1 % num2
			return(answer)
		def expon(num1, power): #Exponents
			answer=num1 ** power
			return(answer)
		def randombetween(range1, range2, exclude, modi): #Random number between range1 and range2
			from random import randint
			answer=randint(range1, range2)
			answer=answer-modi
			while answer==exclude:
				answer=randint(range1, range2)
				answer=answer-modi
			else:
				return(answer)
		def rand(): #Random decimal from 0.0 - 1.0
			from random import random
			answer=random()
			return(answer)
		def randhex(range1, range2, modi): #Random hexadecimal number
			from random import randint
			answer=hex(randint(range1, range2))
			answer=answer-modi
			return(answer)
		def randbin(range1, range2, modi): #Random Binary number
			from random import randint
			answer=(randint(range1, range2))
			answer=answer-modi
			return(bin(answer))
		def randoct(range1, range2, modi): #Random octal number
			from random import randint
			answer=oct(randint(range1, range2))
			answer=answer-modi
			return(answer)
		def randuni(range1, range2, modi, surrobool, asciibool): #Random Unicode Character
			try:
				from random import randint
				answer=randint(range1, range2)
				return(chr(answer))
				if surrobool==True:
					from random import randint
					answer=randint(range1, range2)
					return(chr(answer))
				else:
					answer=randint(33,127)
					answer=answer-modi
					return(answer)
			except UnicodeEncodeError:
				pass
		class logic:
			def LT(num1, num2):
				if num1<num2:
					return(True)
				elif num1==num2:
					return(True)
				else:
					return(False)
			def SLT(num1, num2): #Strictly Less than
				if num1<num2:
					return(True)
				elif num1==num2:
					return(False)
				else:
					return(False)
			def GT(num1, num2): #Greater than
				if num1>num2:
					return(True)
				elif num1==num2:
					return(True)
				else:
					return(False)
			def SGT(num1, num2): #Strictly Greater than
				if num1>num2:
					return(True)
				elif num1==num2:
					return(False)
				else:
					return(False)
			def EQ(num1, num2):
				if num1>num2:
					return(False)
				elif num1==num2:
					return(True)
				else:
					return(False)
			def AND(bit1, bit2):
				if bit1==True and bit2==True:
					return(True)
				else:
					return(False)
			def OR(bit1, bit2):
				if bit1==True or bit2==True:
					return(True)
				else:
					return(False)
			def NOT(bit):
				if bit==True:
					return(False)
				else:
					return(True)
			def NAND(bit1, bit2):
				if bit1==True and bit2==True:
					return(False)
				else:
					return(True)
			def NOR(bit1, bit2):
				if bit1==True or bit2==True:
					return(False)
				elif bit1==False and bit2==False:
					return(True)
			def XOR(bit1, bit2):
				if bit1==True or bit2==True:
					return(False)
				else:
					return(True)
		def count(string, lookfor):
			answer=string.count(lookfor)
			return(answer)
		def genletter():
			password=list()
			from random import randint
			password.append(chr(randint(33,127)))
			return(password)
		class console:
			try:
				def w(write):
					print(write)
				def wait(time):
					from time import sleep
					sleep(time)
				def line_break():
					print('\n')
				def tab():
					print('\t')
				def clear():
					print(flush=True)
				def aspos():
					print('\'')
				def double_aspos():
					print('\"')
				def revrs(write):
					print(write[::-1])	
				def unitrans(write):
					return(chr(write))
				def dedicate():
					print('To my amazing family, and mainly to my mom, Yvette, for being my inspration, light, and path for me to grow.')
				def ask(question,ifright,messageifwrong,messageifright):
					answer=input(question)
					if answer==ifright:
						return(messageifright)
					else:
						return(messageifwrong)
					def slowtype(text, speed):
						import random
						import sys
						import time
						for char in text:
							mydelay=random.randint(1,40)
							mydelay = mydelay/100
							sys.stdout.write(char)
							sys.stdout.flush()
							time.sleep(mydelay)
			except TabError:
				pass
			except IndentationError:
				pass
			except ModuleNotFoundError:
				pass
			try:
				class color:
					class Fore:
						def red(write):
							from colorama import Fore
							print(Fore.RED, write)
						def green(write):
							from colorama import Fore, Back, Style
							print(Fore.GREEN, write)
						def light_blue(write):
							from colorama import Fore, Back, Style
							print(Fore.LIGHTBLUE_EX, write)
						def blue(write):
							from colorama import Fore, Back, Style
							print(Fore.BLUE, write)
						def yellow(write):
							from colorama import Fore, Back, Style
							print(Fore.YELLOW, write)
						def magenta(write):
							from colorama import Fore, Back, Style
							print(Fore.MAGENTA, write)
						def cyan(write):
							from colorama import Fore, Back, Style
							print(Fore.CYAN, write)
						def light_green(write):
							from colorama import Fore, Back, Style
							print(Fore.LIGHTGREEN_EX, write)
						def light_red(write):
							from colorama import Fore, Back, Style
							print(Fore.LIGHTRED_EX, write)
					class Back:
						def red(write):
							from colorama import Fore, Back, Style
							print(Back.RED, write)
						def green(write):
							from colorama import Fore, Back, Style
							print(Back.GREEN, write)
						def light_blue(write):
							from colorama import Fore, Back, Style
							print(Back.LIGHTBLUE_EX, write)
						def blue(write):
							from colorama import Fore, Back, Style
							print(Back.BLUE, write)
						def yellow(write):
							from colorama import Fore, Back, Style
							print(Back.YELLOW, write)
						def magenta(write):
							from colorama import Fore, Back, Style
							print(Back.MAGENTA, write)
						def cyan(write):
							from colorama import Fore, Back, Style
							print(Back.CYAN, write)
						def light_green(write):
							from colorama import Fore, Back, Style
							print(Back.LIGHTGREEN_EX, write)
						def light_red(write):
							from colorama import Fore, Back, Style
							print(Back.LIGHTRED_EX, write)
					class Style:
						def dim(write):
							from colorama import Fore, Back, Style
							print(Back.LIGHTGREEN_EX, write)
						def bright(write):
							from colorama import Fore, Back, Style
							print(Back.LIGHTGREEN_EX, write)
			except IndentationError:
				pass
			except TabError:
				pass
		try:
			def cut(write,startcut, endcut):
				return(write[startcut, endcut])
			def concat(string1, string2):
				return(string1 + string2)
		except TabError:
			pass
		except IndentationError:
			pass
		try:
			class jsonpy:
				def load(filename):
					with open(filename) as f:
						import json
						answer=json.load(f)
						return(answer)
				def dump(filename, write):
					with open(filename, 'w') as f:
						import json
						json.dump(write, f)
		except FileNotFoundError:
			pass
		except TabError:
			pass
		except IndentationError:
			pass
		def upper(string):
			return(string.upper())
		def lower(string):
			return(string.lower())
		def title(string):
			return(string.title())
		def swapcase(string):
			return(string.swapcase())
		class time:
			def datetime():
				from datetime import datetime
				return(datetime.now())
		class stream:
			def __init__ (self, streamtitle, visible):
				self.title = streamtitle
				self.visible = visible
				self.contents = list()
				if visible == True:
					print(f'======={streamtitle}=======')
				else:
					return(None)
			def update(self, add, user='Anonymous'):
				import datetime
				self.contents.append(add)
				now = datetime.datetime.now()
				print(f'On {now}, {user} wrote: {add}')
			def removepost(self, thing):
				for thing in self.contents:
					self.contents.remove(thing)
			def getposts(self):
				return self.contents
		from colorama import Fore, Back, Style
		print(Style.RESET_ALL, ' ')
		code = input('Code Window: ')
		exec(compile(code, code, 'exec'))
	#Start of Error Catching System: AKA. EOS

	except TabError:
		pass
	except IndentationError:
		pass
	except UnicodeEncodeError:
		pass
	except FileNotFoundError:
		pass
	except ValueError:
		pass
	except IndexError:
		pass
	except TypeError:
		pass
	except TimeoutError:
		pass
	except ModuleNotFoundError:
		pass
	except ArithmeticError:
		pass
	except AttributeError:
		pass
	except SyntaxError:
		pass
	except ZeroDivisionError:
		pass
	except SystemError:
		pass
	except EOFError:
		pass
	except KeyboardInterrupt:
		InspyreAppOpened=False
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')