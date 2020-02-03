import math

def my_sqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return(y)

print(my_sqrt(9))


def test_sqrt():
    a = 1
    while a <= 25:
        diff = math.sqrt(a) - my_sqrt(a)
        print("a = " + str(a) + " | my_sqrt(a) = " + str(my_sqrt(a)) + " | math.sqrt(a) = " + str(math.sqrt(a)) + " | diff = " + str(diff))
        a = a + 1

test_sqrt()
