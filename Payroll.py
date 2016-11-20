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
	company = None
	
	#Creates a Company and a few users to make things easier for testing. Will be deleted.
	company = Company('Goofy Dogs Inc.')
	company.addEmployee('germanshep@dogmail.com')
	company.addEmployee('corgi@dogmail.com')
	#Creates a Company and a few users to make things easier for testing. Will be deleted.
	
	print('\nWelcome to the Payroll sytem!' )
	print('\nHere are some useful commands: \ncreatecompany [name]\ninviteemployee [email address]\nviewemployees\nexit\n' )
	
	while True:
		userinput = input('\nPlease enter a command:')
		
		userinput = userinput.split(' ', 1)
		
		if userinput[0].lower() == 'createcompany':
			company = Company(userinput[1])
			print('Company ', company.getName(), ' has been created')
		elif userinput[0].lower() == 'inviteemployee':
			company.addEmployee(userinput[1])
			print(userinput[1], ' was invited to the company!')
		elif userinput[0].lower() == 'viewemployees':
			print(company.viewEmployees())
		elif userinput[0].lower() == 'editemployee':
			print()
		elif userinput[0].lower() == 'exit':
			print('\nGoodbye!')
			sys.exit()
		else:
			print('ERROR: Command does not exist')
		
class Company:
	"""
	class description
	"""	
	
	def __init__(self, name):
		self.name = name
		self.userList = UserList()
	
	def getName(self):
		return self.name
		
	def addEmployee(self, email):
		newUser = User(email)
		self.userList.addUser(newUser)
	
	def viewEmployees(self):
		return self.userList.stringArray()
		

class UserList:
	"""
	class description
	"""
	
	def __init__(self):
		self.userList = []
		
	def addUser(self, user):
		self.userList.append(user)
		
	def getUsers(self):
		return self.userList
	
	def stringArray(self):
		userListString = ''
		
		for user in self.userList:
			userListString += ('\n' + user.string())
			
		return userListString
	
class User:
	"""
	User class description
	"""	
	def __init__(self, email, name="Unknown", position = "N/A", salary="0"):
		self.email = email
		self.name = name
		self.position = position
		self.salary = salary
	
	def string(self):
		description = self.name + ' | ' + self.email + ' | Position: ' + self.position + ' | Salary: $' + self.salary
		return description
	
if __name__ == "__main__":
	username = input('Enter Username: ') #temp username is admin
	password = input('Enter Password: ') #temp password is password
	authentication(username, password)
	
	startProgram()