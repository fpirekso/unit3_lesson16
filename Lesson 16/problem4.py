password = input('What is the password? ')

while password not in ['Open Sesame']:
	password = input('Passwod is invalid, try again. ')

print('Password is valid, welcome!')