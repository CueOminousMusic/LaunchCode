def get_initials(fullname):
	""" Given a person's name, return the person's initials (uppercase) """

	initials = fullname[0]
	index = 1
	for char in fullname:
		if char == " ":
			initials = initials + fullname[index]
		index += 1
	initials = initials.upper()
	return initials

def main ():
	name = input("What's your name?")
	print(get_initials(name))
