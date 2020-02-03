def countdown(n):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

# I did not think much about the choice because any function I use will only print Blastoff! for input 0. I proceeded to perform a check using greater than and equal to
def awesome_program():
    n = int(input('Enter an input: '))
    if n >= 0:
        countdown(n)
    else:
        countup(n)

def any_program(n):
    print(num + n)

# Python understands we want to do addition but encountered an error when trying to implement our code because num is not defined
# To dix the error, I  must add create a variable number and set it to a number

countdown(2)
countup(-5)
awesome_program()
any_program(3)
