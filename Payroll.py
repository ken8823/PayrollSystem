"""
Jacob Barger, Kenny Chen, Adam Thai, and Scott Graham
Software Engineering Fall 2016
Payroll System
<file name>
<file description>
"""

import sys

class User:
	"""
	User class description
	"""	
	def __init__(self, name):
		self.name = name
	
if __name__ == "__main__":
	user1 = User("Jimmy")
	print(user1.name)