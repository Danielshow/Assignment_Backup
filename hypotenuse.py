import math

def hypotenuse(a, b):
    return (a, b)

### This stage makes sure the function is running properly and that it takes in two parameters
print(hypotenuse(2, 4))
## output: 2,4

def hypotenuse(a, b):
    asquared = a * a
    bsquared = b * b
    return (asquared, bsquared)

#### This stage squared the parameter and make sure they return the correct square
print(hypotenuse(2, 4))
# ### Output: 4, 16

def hypotenuse(a, b):
    asquared = a * a
    bsquared = b * b
    a_bsquared = asquared + bsquared
    return a_bsquared

#### This stage add the square of the parameter a and b
print(hypotenuse(5, 3))
# output: 34

def hypotenuse(a, b):
    asquared = a * a
    bsquared = b * b
    a_bsquared = asquared + bsquared
    result = math.sqrt(a_bsquared);
    print(result)
    return result

#### THis step complets the process by adding sqrt but print out the result to ensure there is no bug
hypotenuse(3,9)
#output: 9.486832980505138

hypotenuse(3, 4)
#outputL 5.0

hypotenuse(5, 12)
#output 13


###### Part two
### (-b±√(b²-4ac))/(2a)

def quadratic_formular(a, b, c):
    return (a, b, c)

## The first stage, I made sure my function is returning what I passed into it
print(quadratic_formular(1,3,4))
#output: 1,3,4

def quadratic_formular(a, b, c):
  ins = b * b - 4 * a * c
  return ins

### The second stage I did was to solve the formular in the square root so as not to encounter any error
print(quadratic_formular(1,3,4))
##output:  -7

def quadratic_formular(a, b, c):
  ins = (b * b) - (4 * a * c)
  ins_squared = math.sqrt(ins)
  return ins_squared

### The third step was to square the formular so all the remaining calculations will be easy
print(quadratic_formular(1,-4, -8))
### output: 6.928203230275509

def quadratic_formular(a, b, c):
  ins = (b * b) - (4 * a * c)
  ins_squared = math.sqrt(ins)
  x1 = (-b + ins_squared) / (2 * a)
  x2 = (-b - ins_squared) / (2 * a)
  return ('x1 = ', x1, 'x2 =', x2)

### The final step I used was to use the remaining formular and divide it by 2a

print(quadratic_formular(1, -4, -8))
#output ('x1 = ', 5.464101615137754, 'x2 =', -1.4641016151377544)

print(quadratic_formular(1, -3, -2))
###output: ('x1 = ', 3.5615528128088303, 'x2 =', -0.5615528128088303)

print(quadratic_formular(2, -5, -3))
#### output: ('x1 = ', 3.0, 'x2 =', -0.5)



##### PART 3
## I feel great about the feedback I have recieved so far. It is been eye opening and I have learnt a lot from the feedback. I also thing my peers will be happy with the feeddback I gave because I always read to understand their work before grading them
