#Happy coding!!!!!!!!

print('******************** Welcome to Calculator v1.1 ********************')
print('********************     coded by shadowak47    ********************\n\n')

cont = 'y'
while cont == 'y':
    selectOp =input('Select operation to perform(+,-,*,/):' )

    if selectOp == '+' or selectOp == '-' or selectOp == '*' or selectOp == '/':
        if selectOp == '+':
            firstNum = input('Please enter the first number: ')
            secNum = input('Please enter the second number: ')
            print('The answer is ')
            print(float(firstNum) + float(secNum))

            cont = input('Perform another calculation(y/n)?')

            if cont != 'y':
                break


        elif selectOp == '-':
            firstNum = input('Please enter the first number: ')
            secNum = input('Please enter the second number: ')
            print('The answer is ')
            print(float(firstNum) - float(secNum))

            cont = input('Perform another calculation(y/n)?')

            if cont != 'y':
                break

        elif selectOp == '*':
            firstNum = input('Please enter the first number: ')
            secNum = input('Please enter the second number: ')
            print('The answer is ')
            print(float(firstNum) * float(secNum))

            cont = input('Perform another calculation(y/n)?')

            if cont != 'y':
                break

        elif selectOp == '/':
            firstNum = input('Please enter the first number: ')
            secNum = input('Please enter the second number: ')
            print('The answer is ')
            print(float(firstNum) / float(secNum))

            cont = input('Perform another calculation(y/n)?')

            if cont != 'y':
                break

        else:
            print('Incorrect operation!')

    else:
        print('Invalid selection!!!')
        print('Only select from following options (+,-,*,/)')
        cont = input('Continue(y/n)?')

        if cont != 'y':
            break
