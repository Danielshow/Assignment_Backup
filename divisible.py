def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(x, y):
    if (y == 1 or x == y):
        # if y is equal to x or second argument is equal to 1 return true # base case
        return True
    elif(y > x):
        # returns false if y is greater than x to prevent maximum recursion
        return False
    else:
        x = x / y
        if (is_divisible(x, y)):
           return is_power(x, y)
        else:
            return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
