package_error = []

try:
	from gsearchlib import Search
except ImportError:
	package_error.append('gsearchlib')

try:
	import time
except ImportError:
	package_error.append('time')

try:
	import os
except ImportError:
	package_error.append('os')

if len(package_error) > 0:
	print('Some libraries are not installed. Install them by running this command:\npip install ' + ' '.join(package_error))
	exit()


def absolute_paths():

	print("11 - Appdata path")
	print("22 - Local path")

	usr = int(input("Write what do you want to see: "))

	user = (11, 22)
	if usr == 11:
		print(os.getenv('APPDATA'))
		if usr == 22:
			print(os.getenv('LOCAL'))
	else:
		print("Wrong data")


print("1. Discord paths")


user_choice = input("What do you want to choose? ")

choice = ('1')
if user_choice in (choice):
	absolute_paths()
else:
	print("This choice doesnt exist, but you can find it in the internet. Tap something to continue")
	time.sleep(2)
	result = Search("How to do correct search? ")
	print(result)