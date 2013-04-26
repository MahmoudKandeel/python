#!/usr/bin/python2

import math

# Question 1: 1 else, unlimited elif

# Question 2
def bool_ret(p,q):
    return not(p or not q)

print "p = True, q = True : ", bool_ret(True,True)
print "p = True, q = False : ", bool_ret(True,False)
print "p = False, q = True : ", bool_ret(False,True)
print "p = False, q = False : ", bool_ret(False,False)

# Question 3
# ((n - n % 10) % 100) / 10
# (n // 10) % 10

# Question 4: 10

# Question 5:
def f(x):
    return -5*x**5+69*x**2-47

print "f(0) = ",f(0)
print "f(1) = ",f(1)
print "f(2) = ",f(2)
print "f(3) = ",f(3)


# Question 6:
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value*(1+rate_per_period)**periods
    return fv

print "future_value(500, .04, 10, 10)",future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

# Question 7:
def area(no_of_sides,length_of_each_side):
    return 1./4*no_of_sides*math.pow(length_of_each_side,2)/math.tan(math.pi/no_of_sides)

print "area(5,7) = ",area(5,7)
print "area(7,3) = ",area(7,3)

# Question 10: Incorrect Indentation

# Question 9:
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
