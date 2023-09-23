import getpass #this module is used to make the password invisible

print('Create a account now!')
username=input('Enter username: ')
password = getpass.getpass('Enter password: ')#over here getpass is the module and .getpass() is the function

print('Your account has been created successfully!')
print('Login')

username2=input('Enter username: ')
password2=getpass.getpass('Enter password: ')

if username == username2 and password == password2:
  print('You are logged in!')
else:
  print('Invalid username or password')