import math


def third_value(a):
    return a*a*a

The_third_power = third_value(5)
print(The_third_power)

def average_three(a,b,c):
    return (a + b + c)/3

average_of_3 = average_three(5, 6, 7)

print(average_of_3)
def write(n):
    for i in range(n):
        print(i)


write(10)

def greater_than_100(n):

    for i in range(n):

        print(100 + i)

greater_than_100(3)

def sequence_even(n):

    for i in range(1,n+1):
        print(2*i)

sequence_even(10)

def decreasing(n):

    for i in range(n):

        print(n - i)

        
decreasing(5)

def the_square(n):
    result = 0
    for i in range(1, n+1):

        result += i**2


    print(result)


        


the_square(5)

def ulohav4(n):
    for i in range(n, 0, -1):
        print(i)
        
ulohav4(5)


def set_of(n):
    series = 0
    for i in range(1, n+1):
        series = series + i**2
        print(series)
        
set_of(5)

def arit(a0, d, N):

    for i in range(N):

        b = a0 + i*d
        print(b)

arit(0, 3, 5)

def arit2(a0, d, N):
    b = a0
    for i in range(N):
        print(b)

        b = b + d

arit2(0, 3, 5)


def geo_seq(g0, r, N):

    for i in range(N):
        b = g0*r**i
        print(b)

geo_seq(4, 6, 20)

def geo_seq2(g0, r, N):

    b = g0
    for i in range(N):

        print(b)

        b = b*r

geo_seq2(4, 6, 20)


def grid(n):
    
    retazec =n*"+ - - - - "+"+"
    retazec2 =n*"|         "+"|"
    for j in range(n):
        print(retazec)
        for i in range(4):
            print(retazec2)
    print(retazec)
    
    
for i in range(4):
    print("+ - - - - ", end = '')
print("+")
    
grid(4)
 
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end= " ")
        
    for j in range(i+1):
        print("*", end = ' ')
        
    print()       
         
#Hill Pattern

n = 5
for i in range(n):
    
    for j in range(i, n):
        print(" ", end= " ")
        
    for j in range(i):
        print("*", end = " ")
        
    for j in range(i+1):
        print("*", end = " ")
        
    print()
    
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end= " ")
        
    for j in range(i, n-1):
        print("*", end= " ")  
        
    for j in range(i, n):
        print("*", end = " ")
        
        
    print()