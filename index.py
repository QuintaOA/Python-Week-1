# Basic Calculator Program

first_number = int(input("Add the first number here:  "))
second_number = int(input("Add the first number here: "))

operator = input("Specify the math operation here (+,-,*,/) ")

if(operator == '+'):
    print(first_number + second_number)
elif(operator == '-'):
    print(first_number - second_number)
elif (operator == '*'):
    print(first_number * second_number)
elif (operator == '/'):
    print(first_number / second_number)
else:
    print('Sorry, your operation is not in the provided list')



