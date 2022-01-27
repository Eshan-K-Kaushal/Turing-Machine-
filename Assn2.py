import numpy as np
import itertools

state = 'A'

def ones(a):
    list1 = []
    while a:
        list1.append(1)
        a -= 1
    return list1

def addition(a, b):
    print('Addition Here:')
    tape = ['#', '#']
    tape.insert(1, ones(a))
    tape.insert(2, '+')
    tape.insert(3, ones(b))
    print('The tape after converting the inputs into ones - ')
    print(tape)
    print('----------------------------------------------------------------------------')
    # breaking down the lists of ones in the tape into individual ones
    tape_bd = list(itertools.chain(*tape))
    # replacing the first plus sign we see
    for i in range(len(tape_bd)):
        if tape_bd[i] == '+':
            tape_bd[i] = 1
    print('The state of the tape after replacing the "+" sign - ')
    print(tape_bd)
    print('-----------------------------------------------------------------------------')
    # to get to the end and then changing the state and then deleting the first 1 we see while going backwards
    for i in range(1, len(tape_bd)):
        if tape_bd[i] == '#':
            print('end reached')
            print('state change')
            state = 'B'
            for i in range(len(tape_bd)-1, -1, -1):
                if tape_bd[i] == 1:
                    tape_bd[i] = '_'
                    break
    print('After the changed head state and going in the reverse order and deleting the first 1 we encounter - ')
    print(tape_bd)
    print('------------------------------------------------------------------------------')
    # ust printing the total number of ones we have now in the tape after all the steps have been carried out
    sum1 = 0
    for i in range(len(tape_bd)):
        if tape_bd[i] == 1:
            sum1 += 1

    print("The result of addition is ", sum1)
    print('The current head state is ',state)
# end of addition function
# start of subtraction function
def subtraction(a,b):
    print('Subtraction here:')
    tape = ['#', '#']
    tape.insert(1, ones(a))
    tape.insert(2, 'M')
    tape.insert(3, ones(b))
    print('Tape after inputs have been converted to 1s and put into the tape:')
    print(tape)
    print('-----------------------------------------------------------------------------------')
    tape_bd = list(itertools.chain(*tape))
    print('Tape after the list of 1s has been broken down into individual 1s:')
    print(tape_bd)
    print('-----------------------------------------------------------------------------------')

    for i in range(a + 1, len(tape_bd)): # this iterates through the half of the list after the 'M' symbol
        if tape_bd[i] == 1: # this looks for any 1s left after the 'M symbol'. If there are 1s left then it will do the following for loops
            for i in range(a + 1, len(tape_bd)): # here we replace the 1s after 'M' by 'X'
                if tape_bd[i] == 1:
                    tape_bd[i] = 'X'
                    break
            for i in range((a + 1) - 1, -1, -1): # here we replace the 1s just before the 'M' symbol with 'X'
                if tape_bd[i] == 1:
                    tape_bd[i] = 'X'
                    break
    print('Tape after subtraciton has been carried out:')
    print(tape_bd)
    print('------------------------------------------------------------------------------------')
    sub1 = 0
    for i in range(len(tape_bd)):
        if tape_bd[i] == 1:
            sub1 += 1
    print('The result of the subtraction is 'sub1)
# end of subtraction function

'''
MAIN
'''
print('Hi! Welcome to a basic Turing Machine!')
choice = ''
ending = ''
i = 2
while 1:
    print('What do you wan to go for? 1) Addition (Type 1) 2) Subtraction (Type 2)')
    choice = int(input('Type your choice: '))
    if choice ==1:
        print('You have chosen addition!')
        a = int(input('Input the first number for addition '))
        b = int(input('Input the second number for addition '))
        addition(a,b)
        break
    elif choice == 2:
        print('You have chosen subtraction!')
        a = int(input('Input the first number for subtraction (The number you want to subtract from - the larger number that is) '))
        b = int(input('Input the second number for subtraction (The number you want to subtract from the larger number) '))
        if a>b:
            subtraction(a,b)
        else:
            print('Had to adjust the elements here since', a, '<', b)
            subtraction(b,a)
            break

