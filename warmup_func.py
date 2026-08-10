s=input("Enter a string:")
l1=input("Enter a list of numbers separated by commas:").split(",")
l2=input("Enter a list of items seperated by commas:").split(',')
n=int(input("Enter a number:"))

def is_palindrome(s):
    return s[::-1]==s

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    c=0
    for i in s:
        if i in 'aeiou':
            c+=1
    return c

def fizzbuzz(n):
    for i in range(n+1):
        if i%15==0:
            print('FizzBuzz')
        elif i%5==0:
            print('Fizz')
        elif i%3==0:
            print('Buzz')
        print(i)
        i+=1

def is_even(n):
    return n%2==0

def factorial(n):
    fact=1
    i=1
    while i<=n and i>=0:
        fact*=i
        i+=1
        
    return fact

def celsius_to_fahrenheit(n):
    return n*1.8+32

def find_max(l1):
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    return max

def remove_duplicates(l2):
    unique=[]
    for i in l2:
        if i not in unique:
            unique.append(i)
    return unique

def sum_list(l1):
    total=0
    for i in l1:
        total+=int(i)
    return total

print('String is:',s)
if is_palindrome(s):
    print('String is a palindrome')
else:
    print('String is not a palindrome')

print('Reversed string:',reverse_string(s))
print('No of vowels=',count_vowels(s))

print('Number is',n)
print('Count of integer 1 to n')
fizzbuzz(n)

if is_even(n):
    print('Number is even')
else:
    print('Number is odd')

print("Factorial of n is:",factorial(n))

print('Celsius',n,'fahrenheit:',celsius_to_fahrenheit(n))

print(l1)
print('Largest value:',find_max(l1))
print('Sum of numbers',sum_list(l1))

print(l2)
print('After removing duplicates list is:',remove_duplicates(l2))
