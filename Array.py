'''
# Armstrong Number
# concept--> three digit number with, sum of cube of its digit = number itself.

def armstrong_number():
    for _ in range(100, 1000):
        hundred = _//100
        mid = _ - (hundred*100)
        tens = mid//10
        ones = mid - (tens*10)
        result = hundred**3 + tens**3 + ones**3
        if _ == result:
            print(_)


armstrong_number()
'''
# accept a two digit number and display in reversed form

'''
def rev():
    my_number = int(input('Enter a number :'))
    d1 = my_number//10
    d2 = my_number % 10
    result = d2*10+d1

    if my_number < 10:
        return my_number
    else:
        print('Reversed digits are-->', result)


rev()
'''

# Factorial of number
'''

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)


my_number = int(input('Enter a number :'))
print('Factorial of a number is ', fact(my_number))
'''

# Fibonacci
'''

def Fibonacci():
    first = 0
    second = 1
    for _ in range(0, 11):
        res = first+second
        print(res)
        first = second
        second = res


Fibonacci()
'''
# prime number
'''

def prime():
    my_number = int(input('No of prime numbers:'))
    lst = []
    for _ in range(2, my_number):

        if _ == 2 or _ == 3 or _ == 5 or _ == 7:
            print(_)
        elif _ % 2 == 0 or _ % 3 == 0 or _ % 5 == 0 or _ % 7 == 0:
            lst.append(_)

        elif _ % 3 != 0 or _ % 5 != 0 or _ % 7 != 0:
            print(_)


prime()
'''
# gcd
'''

def GCD():
    n = int(input('Enter number 1: '))
    n1 = int(input('Enter number 2: '))
    if n < n1:
        gcd = n
    else:
        gcd = n1
    while n % gcd != 0 or n1 % gcd != 0:
        gcd = gcd-1
    if gcd == 1:
        print('No gcd found')
    else:
        print('GCD is ', gcd)


GCD()
'''
# lcm
'''

def LCM():
    n = int(input('Enter number 1: '))
    n1 = int(input('Enter number 2: '))
    if n > n1:
        lcm = n
    else:
        lcm = n1
    while lcm % n != 0 or lcm % n1 != 0:
        lcm = lcm+1
    print('LCM is', lcm)


LCM()
'''
# Length of string

'''
def length():
    str = input('Enter any string :')
    count = 0
    for _ in range(0, len(str)):
        if str[_] == 'a' or str[_] == 'e' or str[_] == 'i' or str[_] == 'o' or str[_] == 'u':
            count = count+1

    print('The number of vowels are', count)


length()
'''
# reverse a string

'''
def rev():
    str = input('Enter any string :')
    lst = []
    for _ in range(0, len(str)):
        lst.append(str[_])
    new = lst[::-1]
    print(*new)


rev()
'''
# palindrome
'''

def palindrome():
    str = input('Enter any string :')
    old = list(str)
    lst = []
    for _ in range(0, len(str)):
        lst.append(str[_])
    new = lst[::-1]
    if old == new:
        print('Yes this string is a palindrome')
    else:
        print('Not a palindrome')


palindrome()

'''
# decimal to binary


def binary(num):

    if num >= 1:
        binary(num//2)
        #print(num % 2)
        lst.append(num % 2)


'''
lst = []
num = int(input('enter a number: '))
binary(num)
print(lst)
global_counter = 0
local_count = 1

for _ in range(1, len(lst)):

    if lst[_-1] == 1 and lst[_] == 1:
        local_count = local_count+1
    elif global_counter <= local_count:
        global_counter = local_count
        local_count = 1


print(global_counter)
'''

# alternate solution

'''
print(len(max(bin(int(input().strip()))[2:].split('0'))))
'''
# Array in reverse without using any built in function
'''

def revarr():
    lst = []
    lst1 = []
    for _ in range(3):
        num = int(input('Enter number'))
        lst.append(num)
    print(lst)
    for _ in range(0, len(lst)):
        lst1.append(lst[(len(lst)-1)-_])
    print(lst1)


revarr()
'''
# l = [3,5,1,7,9,5,6,4,2]

# l2 = [ _*_ for _ in l]
# print(l2)

# l = ['raj', 'heyy', 'yo']
# l2 = [ len(_) for _ in l]
# print(l2)
# l = [[1,2,3], [4,5,6]]
# l2= [ i for _ in l for i in _]
# print(l2)

# n = int(input())
# d = { _ : _**2  for _ in range(1,n)}
# print(d)

# map

# d = [1,2,3,4,5]
# def s(n):
#   return n**2
# result = list(map(s,d))
# print(result)

# def add(num1,num2):
#   return num1 + num2

# d = [100,200,300]
# d1 = [10,20,30]
# result = list(map(add, d, d1))
# print(result)

# filter

# lets say we want to print out even numbers that
'''

def check(num):
    if num % 2 == 0:
        return num


d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(check, d))
print(result)
'''

# generator functions, example fibo
'''

def fibo():

    num1 = 0
    num2 = 1

    while (True):
        next_val = num1 + num2
        yield next_val
        num1, num2 = num2, next_val
        


result = fibo()

print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

'''
# iter
'''
l = [1, 2, 3, 4, 5, 6]
i = iter(l)

print(next(i))
'''

# sort 0s and 1s and 2s without any sorting algorithm
'''
a=[1,1,0,2,0,1]
print(a)



low = 0
mid = 0
high = len(a) -1

while mid <= high :
  if a[mid] == 0:
    a[low], a[mid] = a[mid], a[low]
    low = low +1
    mid = mid +1
  elif a[mid]  == 1:
    mid = mid + 1
  else:
    a[mid],a[high] = a[high],a[mid]
    high = high -1
print(a)    
'''
'''
#missing and repeat number
a = [1,5,2,4,5]
z = sorted(a)
lst =[]
print(z)
for _ in range(1,len(z)):
  if z[_-1] == z[_]:
    lst.append(z[_])
    if _ < len(z)-1:
      _ = _ +1
  elif z[_-1]+ 1 != z[_]:
    lst.append(z[_-1]+1)

print(*lst)
'''
# kadanes algo, largest subarray sum
'''
a = [-1,-4,2,3,6,7]
max_sum = 0
current_sum = 0
for _ in range(0,len(a)):
  current_sum = current_sum + a[_]
  if current_sum < 0:
    current_sum = 0

  elif current_sum > 0 and max_sum < current_sum:
    max_sum = max_sum + current_sum  

print(max_sum)
'''

# find max number in an array, without sorting
'''
n = [3,4,5,6,1,2,3,5,6,8,12,32,56,78,34,23,678,89]

maxi = 0

for _ in range(1, len(n)):
  if n[_-1] > n[_]:
    maxi = n[_-1]
    _ = _ + 1
  else :
    _ = _ + 1  
    

print(maxi)    
'''
