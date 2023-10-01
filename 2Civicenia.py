import math


def third_value(a):

    return a*a*a

cube_of = third_value(2)
print(cube_of)

cubes_of = third_value(3)
print(cubes_of)


def third_power(a):

    return a*a*a

power_of_five = third_power(5)

print(power_of_five)

def average_three(a, b, c):

    return (a+b+c)/3

average_of_three = average_three(1, 2, 3)

print(average_of_three)

average_th = average_three(1, 2, 4.5)

print(average_th)

averages = average_three(5, 6, 7)

print(averages)

def list_num(n):

    for i in range(n):
        print(i)

list_of_num = list_num(12)
print(list_of_num)


def listing(n):
    for i  in range(n):
        print(100 + i)


listing_of = listing(3)
print(listing_of)

def even_num(n):

    for i in range(n):
        print(2*(i+1))

even_numbers = even_num(5)
print(even_numbers)

def decreasing_order(n):

    for i in range(n):

        i = n-i
        print(i)

decreasing_sequence = decreasing_order(5)

print(decreasing_sequence)


def arthimetic_sequence(a, d, N):

    for i in range(1, N):

        print(a +(i-1)*d)



arthi = arthimetic_sequence(2, 3, 10)

print(arthi)

def geometric_sequence(a0, r, N):
    a=a0
    for i in range(N):
        a = a*r

        print(a)

geo = geometric_sequence(1, 2, 12)
print(geo)




    
    






