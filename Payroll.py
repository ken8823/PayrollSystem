"""
Jacob Barger, Kenny Chen, Adam Thai, and Scott Graham
Software Engineering Fall 2016
Payroll System
<file name>
<file description>
"""

import sys

def authentication(email, password, file):
	"""
	class description
	"""	
	
	datafile = open(file, "r+")
		
	for line in datafile:
			temp = line.split('|', 2)
			if temp[0] == email:
				if temp[1] == password:
					return
			
	datafile.close()
	
	sys.exit('Invalid Email or Password')

def register(file):
	"""
	class description
	"""
	
	datafile = open(file, "a")

	print('Thank you for choosing to register! We just need to ask you a few questions.')
	
	email = input('What is your email address? ')
	password = input('What would you like your password to be? ')
	firstname = input('What is your first name? ')
	lastname = input('What is your last name? ')
	birthday = input('What is your birthday? DD/MM/YYYY ')
	bankaccount = input('What is the bank account number you would like to use for transactions? ')

	userentry = email + '|' + password + '|' + firstname + '|' + lastname + '|' + birthday + '|' + bankaccount
	
	datafile.write(userentry);

	datafile.close()
		
	print('Successfully registered! Feel free to login now.')
	
	return
	
def startProgram(file, userfile, user):
	"""
	class description
	"""	
	company = None
	
	company = Company('Goofy Dogs Inc.', file)
	
	username = ''
	
	for line in userfile:
			temp = line.split('|', 5)
			if temp[0] == user:
				username = temp[2] + ' ' + temp[3]
				break
	
	print('\nWelcome ', username, ' to the Payroll system!' )
	print('\nHere are some useful commands: \ncreatecompany [name]\ninviteemployee [email address]\nviewemployees\nexit\n' )
	
	while True:
		userinput = input('\nPlease enter a command: ')
		
		userinput = userinput.split(' ', 1)
		
		if userinput[0].lower() == 'createcompany':
			company = Company(userinput[1], file)
			print('Company ', company.getName(), ' has been created')
		elif userinput[0].lower() == 'inviteemployee':
			company.addEmployee(userinput[1])
			print(userinput[1], ' was invited to the company!')
		elif userinput[0].lower() == 'viewemployees':
			print('\nHere are all the employees:')
			for i in company.viewEmployees():
				print(i)
		elif userinput[0].lower() == 'editemployee':
			print()
		elif userinput[0].lower() == 'exit':
			print('\nGoodbye!')
			#sys.exit()
			return
		else:
			print('ERROR: Command does not exist')
		
class Company:
	"""
	class description
	"""	
	
	def __init__(self, name, file):
		self.name = name
		self.userList = UserList()
		self.file = file
	
	def getName(self):
		return self.name
		
	def addEmployee(self, email):
		newUser = User(email)
		self.userList.addUser(newUser)
		self.file.write(newUser.dataString());
	
	def viewEmployees(self):
		self.file.seek(0)
		array = []
		for line in self.file:
			array.append(line)
		return array
		

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
		
	def dataString(self):
		description = self.name + '|' + self.email + '|' + self.position + '|' + self.salary + '\n'
		return description
	
if __name__ == "__main__":
	userinput = input('Login or Register? ')
	
	if userinput.lower() == 'register':
		register('userdata.txt')
		sys.exit()
	elif userinput.lower() == 'login':
		email = input('Enter Email: ') #temp email is admin
		password = input('Enter Password: ') #temp password is password
		
		authentication(email, password, 'userdata.txt')
		
		datafile = open('data.txt', "r+")
		datafile2 = open('userdata.txt', "r+")

		startProgram(datafile, datafile2, email)
	
		datafile.close()
		datafile2.close()
	else:
		sys.exit('Invalid Command')
			
	