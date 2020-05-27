

CalculatorAppOpened=True
while CalculatorAppOpened:
	try:
		print('Type add to do addition.')
		print('Type sub to do subtraction.')
		print('Type mul to do multipication.')
		print('Type div to do division.')
		print('Type mem plus to make the program remember a number.')
		print('Type mem rec to retrive the number you made the program remember.')
		print('Type special to ascess special operations.')
		print('Type stop to end the program.')
		operation=input('What operation would you like to do?')
		if operation=='add':
				a=input('First Number?')
				b=input('Second Number?')
				print('The answer is ')
				print(int(a)+int(b))
		elif operation=='sub':
				a=input('First Number?')
				b=input('Second Number?')
				print('The answer is ')
				print(int(a)-int(b))
		elif operation=='mul':
				a=input('First Number?')
				b=input('Second Number?')
				print('The answer is ')
				print(int(a)*int(b))
		elif operation=='div':
				a=input('First Number?')
				b=input('Second Number?')
				print('The answer is ')
				print(int(a)/int(b))
		elif operation=='mem plus':
				mem=input('What would you like to memorize?')
				memory=list()
				if mem =='First Number':
					memory.append(a)
				elif mem=='Second Number':
					memory.append(b)
		elif operation=='mem rec':
			memory_rem=memory[0]
			print(memory_rem)
			memory.remove(memory_rem)
		elif operation=='stop':
			break
		elif operation=='special':
			spec_oper=input('What operation would you like to do?')
			print('Type mod to do modulus.')
			print('Type hex to convert 2 numbers into hexadecimal form.')
			print('Type bin to convert 2 numbers into binary form.')
			if spec_oper=='mod':
					a=input('First Number?')
					b=input('Second Number?')
					print('The answer is ')
					print(int(a)%int(b))
			elif spec_oper=='hex':
					a=input('First Number?')
					b=input('Second Number?')
					print(hex(int(a)))
					print(hex(int(b)))
			elif spec_oper=='bin':
					a=input('First Number?')
					b=input('Second Number?')
					print(bin(int(a)))
					print(bin(int(b)))
	except KeyboardInterrupt:
		import os
		os.system('clear')
		CalculatorAppOpened=False
		pass								