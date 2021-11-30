print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:


def function1(a):
    s1 = []
    for y in a:
        if y <= 5:
            s1.append(y)
            y = y+1

    print(s1)


function1(x)

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:


def function2(a):
    s2 = []
    for y in a:
        if y % 2 == 0:
            s2.append(y)
    print(s2)


function2(x)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:


def function3(a):
    z = 0
    s3 = []
    while z < 5:
        for y in a:
            if y % 2 == 0:
                s3.append(y)
                z = z+1
            else:
                z = z+1
        break
    print(s3)


function3(x)
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:


def function4(a):
    s4 = []
    for y in a:
        s4.append(y[0])
    print(s4)


function4(names)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:


def function5(a):
    s5 = []
    for x in a:
        s5.append(x.index(" "))
    print(s5)


function5(names)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:


def function6(a):
    s6 = []
    for x in a:
        s6.append(x[0] + x[(x.index(" ") + 1)])
    print(s6)


function6(names)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
# A3a:


def function7(a):
    for x in a:
        if len(x) == len(set(x)):
            print(x)


function7(list_of_lists)
# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:


def function8():
    print('Enter a number bigger than 100')
    x = int(input())
    if x < 100:
        print('Enter a number bigger than 100')
        x = int(input())
    else:
        print(x)


# function8()
print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:


def function9():
    while True:
        try:
            x = int(input('Enter a prime number '))
            break
        except:
            print('Invalid input')
    for y in range(2, int(x/2)):
        if x % y == 0:
            print('not prime')
            break
    else:
        print('prime')
        x = int(input())


function9()


def function10(x: int) -> int:
    for y in range(2, int(x/2)):
        if x % y == 0:
            print('not prime')
            break
    else:
        print('prime')












