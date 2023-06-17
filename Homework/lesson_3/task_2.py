'''Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

'''

phone_number = input('Please input your phone number (10 digits)\n')

if phone_number.isdigit() is True:
    if len(phone_number) == 10:
        print('Phone number format is correct!')
    else:
        print("The number you've enreded is not correct. There should be exactly 10 digits!")
else:
    print("The number you've enreded is not correct. Please use digits only")          