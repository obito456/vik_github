#1 odd or even.
a=int(input("enter="))
if a%2==0:
    print("e")
else:
    print("o")

#2 positive or negative.
a=float(input("enter="))
if a>0:
    print("p")
elif a==0:
    print("z")    
else:
    print("n")

#3 sum of two numbers.
a=float(input("enter="))
b=float(input("enter="))
c=a+b
print(c)

#4 prime or not.

def isprime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False  
    return True

number=int(input("enter="))

if isprime(number):
    print("p")
else:
    print("n")

#5 palindrome or not.
num=input("enter=")

if(num==num[::-1]):
    print("p")
else:
    print("n")

def pali(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

number = input("Enter=")

if pali(number):
    print("PALINDROME")
else:
    print("NOT")

#6  Armstrong or not.
def arm(num):
    stnum=str(num)
    lnum=len(stnum)
    arms=sum(int(num)**lnum for num in stnum)
    return arms==num 
number=int(input("enter="))

if arm(number):
    print("ARMSTRONG")
else:
    print("NOT")

#7 anagram or not
def anagram(s,t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()
    return sorted(s) == sorted(t)

a = input("Enter=")
b = input("Enter=")

if anagram(a,b):
    print( "ANAGRAM")
else:
    print( "NOT")

#8 min pr max
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
print(max(a, b))
print(min(a, b))

#9 factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter="))

if number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    result = factorial(number)
    print(result)

#10 fibonacci of a number.
def fibonacci(n):
    fibsequence = [0, 1]

    while len(fibsequence) < n:
        fibsequence.append(fibsequence[-1] + fibsequence[-2])

    return fibsequence[:n]

number = int(input("Enter="))

if number <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(number)
    print(result)

#11  GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter="))
num2 = int(input("Enter="))

result = gcd(num1, num2)
print(result)

#12 pattern
def myfunc(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

n = 5
myfunc(n)

#13 pattern



    


    
