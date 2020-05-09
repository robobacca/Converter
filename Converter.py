print('welcome to the numerical converter')
print('Please select a base (binary, octal, hexadecimal)\n', 'Do not that this system is case sensitive')
option1 = str(input('Choice of numerical base : '))
option2 = int(input('Type 1 to convert to base and 0 to convert from base : '))
number = str(input('Please enter your number'))

if option1 == 'binary' :
    if option2 == 0:
        output = int(number, 2)
        print('Output : ', output)
    elif option2 == 1:
        output = bin(int(number))
        print('Output : ', output)
    elif option2 > 1:
        print('Invalid input, please try again')
    elif option2 < 0:
        print('Invalid input, please try again')
elif option1 == 'octal':
    if option2 == 0:
        output = int(number, 8)
        print('Output : ', output)
    elif option2 == 1:
        output = oct(int(number))[2:]
        print('Output : ', output)
    elif option2 > 1:
        print('Invalid input, please try again')
    elif option2 < 0:
        print('Invalid input, please try again')
elif option1 == 'hexadecimal':
    if option2 == 0:
        output = int(number, 16)[2:]
        print('Output : ', output)
    elif option2 == 1:
        output = hex(int(number))
        print('Output : ', output)
    elif option2 > 1:
        print('Invalid input, please try again')
    elif option2 < 0:
        print('Invalid input, please try again')
else:
    print('Invalid input, please try again')
