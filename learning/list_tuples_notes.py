a=['AI','Engineering','Python','DSA','AI','Python','AI','DSA']

# =====================================================================
# LISTS - BUILT-IN FUNCTIONS
# =====================================================================

'''
print(a.count('AI'),a.count('Python'),a.count('DSA'),a.count('API'))
Syntax: list.count(value) if value not in list it gives 0 as output. No error'''

'''
print(a.index('AI'),a.index('Engineering'),a.index('n8n'))
Syntax: list.index(value) if value not in list it gives Value Error'''

'''
print(a)
a.reverse()
print(a)
Syntax: #list.reverse()'''

'''
a.append('Web Dev')
print(a)
Syntax: list.append(Value)'''

'''
a.append(3)
a.sort()
print(a)
Syntax: list.sort(Value) if you have different data types in list while sorting it gives TypeError'''

'''
a.pop()
s=a.pop()
print(a)
print(s)
Syntax: list.pop() Removes last element. Can also store value of last element in variable using this function'''

# =====================================================================
# USING LISTS AS STACKS
# =====================================================================
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

Stack: Last in First Out approach'''

# =====================================================================
# USING LISTS AS QUEUES
# =====================================================================    
'''
from collections import deque
queue=deque(a)
print(queue)
queue.append('Systems')
print(queue)
queue.append('Automation')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)

First in First out approach

Syntax: deque(list), list.popleft()
Lists can be used as queues using append and pop. 
However when we have to do first in first out method,
we use this deque as lists are slow in this process and require shift of all elements by one. '''

# =====================================================================
# LIST COMPREHENSION
# =====================================================================    

'''Printing squares of numbers 1 to n
n=10
squares=[x**2 for x in range(n)]
or
squares = list(map(lambda x: x**2, range(10)))
print(squares)
'''

l=[2,6,-5,3,14,-3]

'''Printing list with values doubled
l1=[x*2 for x in l]
print(l1)
'''

'''Printing positive values from list
l2=[x for x in l if x>=0]
print(l2)
'''

l3=[1.7,2,-3.5,6,-1.112,-5,1.6,30]

'''Applying function (round) using list comprehension
l4=[round(x) for x in l3]
print(l4)
'''

''' Calling method (title() for each element
l5=[x.title() for x in a]
print(l5)
'''

'''Creating list of tuples
l6=[(x,'Even') if x%2==0  else (x,'Odd') for x in range(5)]
print(l6)
 if and else come before for in list comprehension. 
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
