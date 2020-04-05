# Written: 05-Apr-2020
# https://edabit.com/challenge/gB7nt6WzZy8TymCah

class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		# Complete the code!
		self.fullname = self.firstname + " " + self.lastname
		self.email = "{}.{}@company.com".format(self.firstname.lower(), self.lastname.lower())
