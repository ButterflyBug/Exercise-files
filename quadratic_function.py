import math


def check_int(givenStr):
    if givenStr[0] in ('-', '+'):
        return givenStr[1:].isdigit()
    return givenStr.isdigit()


def calculateDelta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

# print(check_int(str(-5)))
# print(calculateDelta(1, 5, 4))


coefficient_a = input("Insert a coefficient:")
print("Coefficient a is % s" % coefficient_a)

coefficient_b = input("Insert b coefficient:")
print("Coefficient b is % s" % coefficient_b)

coefficient_c = input("Insert c coefficient:")
print("Coefficient c is % s" % coefficient_c)

num_coefficient_a = int(coefficient_a)
num_coefficient_b = int(coefficient_b)
num_coefficient_c = int(coefficient_c)

delta = calculateDelta(num_coefficient_a,
                       num_coefficient_b,
                       num_coefficient_c)

if not (check_int(coefficient_a) and
        check_int(coefficient_b) and
        check_int(coefficient_c)):
    print("Coefficients do not fullfil an assumption")
else:
    if coefficient_a == 0:
        print("This is not a quadratic function.")
    else:
        if delta < 0:
            print("The function has no solutions.")
        elif delta == 0:
            x_0 = (-num_coefficient_b)/2*num_coefficient_a
            print("The function has one solution", x_0)
        else:
            x_1 = (-num_coefficient_b - math.sqrt(delta))/4*num_coefficient_a
            x_2 = (-num_coefficient_b + math.sqrt(delta))/4*num_coefficient_a
            print("The function has 2 solutions:", x_1, x_2)
