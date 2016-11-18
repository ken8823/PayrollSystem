"""
Jacob Barger, Kenny Chen, Adam Thai, and Scott Graham
Software Engineering Fall 2016
Payroll System
<file name>
<file description>
"""

import sys

def authentication(username, password):
	"""
	class description
	"""	
	if username == 'admin':
		if password != 'password':
			sys.exit('Invalid Username or Password')
	else:
		sys.exit('Invalid Username or Password')

def startProgram():
	"""
	class description
	"""	
	print('\nWelcome to the Payroll sytem!' )
	print('\nHere are some useful commands: \ncreatecompany\ninviteuser\nexit\n' )

	while True:
		userinput = input('Please enter a command:')
		
		if userinput.lower() == 'createcompany':
			print('Company created')
		elif userinput.lower() == 'inviteuser':
			print('User Invited')
		elif userinput.lower() == 'exit':
			print('Goodbye!')
			sys.exit()
		else:
			print('ERROR: Command does not exist')
		
class Company:
	"""
	class description
	"""	
	
	def __init__(self, name):
		self.name = name

class UserList:
	"""
	class description
	"""
	
	#def addUser():
		
	#def getUsers():
		
class User:
	"""
	User class description
	"""	
	def __init__(self, name):
		self.name = name
		
	#def getUser(user):
		
	
if __name__ == "__main__":
	username = input('Enter Username: ') #temp username is admin
	password = input('Enter Password: ') #temp password is password
	authentication(username, password)
	
	startProgram()