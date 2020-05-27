
import smtplib, ssl
port = 465
smtp_server = "smtp.gmail.com"
sender_email = input('Type in your email: ')
password = input("Type your password and press enter: ")
receiver_email = input('Type the person\'s email you would like to send a message to: ')
message = input(f'Message to {receiver_email}: \n')
context = ssl.create_default_context()
try:
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message)
	print(f'Sent email to {receiver_email}.')
except smtplib.SMTPAuthenticationError:
	print('Login Failed.')