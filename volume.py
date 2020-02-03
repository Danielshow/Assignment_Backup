def print_volume(r):
  pi = 3.141592653589793
  return 4/3 * pi * r * r * r


def print_triangle_area(b, h):
  # area of a triangle
  return 0.5 * b * h

def multiply(x, y):
    return x * y;

print(multiply(5, "fffff"))

def removeNegativeNumber(a_list):
    for i in a_list:
        if i < 0:
            a_list.remove(i)
    return a_list

print(removeNegativeNumber([1, 3, 0, -9, 34, -1]))
