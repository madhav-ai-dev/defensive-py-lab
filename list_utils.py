s='Apple Sauce'
n=6
l1=[2,4,3,2,3,5,6,2]
l2=['Rat','rat',67,5,[2,4],(6,),5,[2,4],{'India':'+91'},'rat',(1,3),'Car',1]
l3=[[1,2,3],(4,5,6),[7,8,9]]


'''
# Deduplication(dedupe) is removing identical or redundant data
def dedupe_preserve_order(l):
    d=[l[i] for i in range(len(l)) if l[i] not in l[i+1:]]
    return d

print(dedupe_preserve_order(l1))
print(dedupe_preserve_order(l2))

# Breaking down list into groups of n
def chunk_list(l,n):
    c=[[l[i:i+n]] for i in range(len(l)) if i%n==0 ]
    return c

print(chunk_list(l1,5))
print(chunk_list(l2,4))


# for lists with only lists and tuples in it
def flatten_list_1(l):
    f=[num for i in l for num in i]
    return f

print(flatten_list_1(l3))

# for lists of all data types taking only values in lists and tuples
def flatten_list_2(l):
    f=[num  for i in l if type(i) is list or type(i) is tuple for num in i]
    return f

print(flatten_list_2(l2))

# for lists of all data types taking only values in lists and tuples
def flatten_list_2(l):
    f=[num  for i in l for num in (i if type(i) is list or type(i) is tuple else [i]) ]
    return f

print(flatten_list_2(l2))
'''

# ==================================================
# Warmup_func.py questions using list comprehension
# ==================================================

def count_integer_list(l):
    x=[0]
    count=[0]
    [count.append(x[-1]+1) for i in l if type(i) is int ]
    return count[-1]

def print_n_num(n):
    [print(i) for i in range(1,n+1)]



def count_vowels(s):
    n=[0]
    c=[0]
    [c.append(1+c[-1]) for i in s if i in 'AEIOUaeiou']
    return c[-1]


def factorial(n):
    f=[1]
    [f.append(f[-1]*i) for i in range(1,n+1)]
    return f[-1]


def find_max(l):
    max=[l[0]]
    [max.append(i) for i in l if i>max[-1]]
    return max[-1]

def remove_duplicates(l):
    l1=[l[0]]
    [l1.append(l[i]) for i in range(1,len(l)) if l[i] not in l1]
    return l1

def sum_list(l):
    s=[0]
    [s.append(s[-1]+i) for i in l]
    return s[-1]



print(f'Number of integers in {l2} is {count_integer_list(l2)}')

print(f'Printing {n} numbers')
print_n_num(n)

print('No of vowels=',count_vowels(s))

print(f'Factorial of {n} is {factorial(n)}')

print(f'Maximum no. in {l1} is {find_max(l1)} ')

print(l2,'After removing duplicates',remove_duplicates(l2),sep='\n')

print(f'Sum of numbers in list {l1}={sum_list(l1)}')

'''
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

'''
