# ===========================
#   Sets
# =========================

#  Unordered and unique collection of data
cars={'BMW','Toyota','Hyundai','BMW','Honda'}
print(cars)

# fastest for membership testing. Always use sets for membership testing
a='BMW' in cars
print(a)
b='KIA' in cars
print(b)

# Set is O(1) complexity, list O(N)
# if you have membership testing in a list. If it is a single time do it as a list itself. else it is O(N)+O(1). (O(N) to convert list to set.)
#  But if it is multiple times in a loop converting to set is better. Set is O(1) complexity, list O(N) in membership

l=[1,34,34,'Sofa',12,1,2,'Chair']
c=12 in l
print(c)

l1=['Table',1,'Chair',27,12,168]
l1=set(l1)
for i in l1:
    if i in l:
        print(i,end=', ')


# ================
# Set Operations
# ================

s1=set('India')
s2=set('England')
print(s1,s2,sep='\n')
op1=s1-s2 # Unique letters in s1
op2=s1 | s2 # letters s1, s2 in both
op3=s1 & s2 # letter in both s1 and s2
op4=s1 ^ s2 # letters in s1 or s2 but not both
print(op1,op2,op3,op4,sep='\n')


# ==================
# Set Comprehension
# ==================
sc={s for s in s1 if s in 'AEIOUaeiou'}
print(sc)

# ==================
#   Dictionaries 
# ==================


cost={'pencil':5,'eraser':5,'pen':20}
print(cost)
cost['pen']=10
print(cost)
# if u try retrieving a value with wrong value like cost['ruler'] it gives key error
# It is a better practice to use .get() which returns None
# print(cost['ruler'])
print(cost.get('ruler'))
cost['sharpener']=15
print(cost)
del cost['pencil']
print(cost)

print(list(cost))
print(sorted(cost))

print(10 in cost)
print('pen' in cost)
print('A4 sheets' in cost)

a={x:x**2 for x in (2,4,9)}
print(a)

# Dont take key as a string it shows SyntaxError type it normally it convert to string automatically
b=dict(Cat='Animal',Neem='Plant',Bacteria='Micro Organism')
print(b)


# Dict has unique keys if there are duplicates the last time it is mentioned that value will be taken
cost1={'pencil':5,'eraser':5,'pen':20,'pen':10,'sharpener':15,'pencil':10,'pen':30}
print(cost1)


# looping teachniques

p=dict()
for i,v in enumerate(['Charmander','Charmeleon','Charizard']):
    p[i]=v
    print(i,v)
print(p)

# zip() to loop to or more sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# Reversed
for i in reversed(range(1, 10, 2)):
    print(i) 


# sorted for sorting low to high
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print('.')

# for lower complexity and unique values use set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
basket=set(basket)
for f in sorted(basket):
    print(f)

# Comparing sequences
print((1, 2, 3)              < (1, 2, 4),
[1, 2, 3]              < [1, 2, 4],
'ABC' < 'C' < 'Pascal' < 'Python',
(1, 2, 3, 4)           < (1, 2, 4),
(1, 2)                 < (1, 2, -1),
(1, 2, 3)             == (1.0, 2.0, 3.0),
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))