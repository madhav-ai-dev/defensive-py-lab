# Performing operations through bruit force then using dict functions

def merge_dicts(d1,d2):
    d3=dict()
    for i in d1:
        d3[i]=d1[i]
    for i in d2:
        d3[i]=d2[i]
    return d3

cost1={'pencil':5,'eraser':5,'pen':20}
cost2={'sharpener':30,'A4 sheet':1,'pen':10}
# cost2=[1,2,3] shows error 
print(merge_dicts(cost1,cost2))


def merge_dict_safe(d1,d2):
    clean_d1=d1 if isinstance(d1,dict) else{}
    clean_d2=d2 if isinstance(d2,dict) else{}
    return clean_d1 | clean_d2

print(merge_dict_safe(cost1,cost2))
cost2=[1,2,3] # defensive coding using isinstance makes sure no errors unlike previous method
print(merge_dict_safe(cost1,cost2))

mixed_data = {
    "name": "Alice",                        # String
    "age": 65,                              # Integer
    "height": 5.9,                          # Float
    "is_active": True,                      # Boolean
    "scores": [85, 90, 95],                 # List
    "metadata": {"id": 101, "role": "admin"}, # Dictionary
    "coordinates": (12.9716, 77.5946),      # Tuple
    "Weight": 65
}
print(({1:2,3:4}),)


def invert_dict_safe(d):
    if not isinstance(d, dict):
        return {}  # Defend against non-dict inputs entirely
        
    i_d = {}
    
    for key, value in d.items():
        # 1. Defensively convert unhashable types so they can safely become keys
        if isinstance(value, list):
            safe_key = tuple(value)
        elif isinstance(value, dict):
            safe_key = tuple(sorted(value.items()))
        elif isinstance(value, set):
            safe_key = tuple(sorted(value))  # Handling sets defensively too
        else:
            safe_key = value
            
        # 2. Safely handle duplicates by grouping into a list
        if safe_key not in i_d:
            i_d[safe_key] = [] # we convert each value to list data type so that we can append duplicates and the duplicates are not deleted
            
        i_d[safe_key].append(key)
        
        
    return i_d

print(invert_dict_safe(mixed_data))




def word_count(l):
    w_c=dict()
    w=[]
    for i in l:
        if isinstance(i,str):            
            if i in w:
                w_c[i]+=1
            else:
                w_c[i]=1
            w.append(i)
    return w_c

w = [42, 3.14, "apple", True, None, 42, "banana", 3.14, False, "apple", {"key": "value"}, 
     ['car','baleno'],('bike','Himalayan'),('car','G-Wagon'),[1, 2, 3], (4, 5), True, None]

print(word_count(w))

def group_by_key(k):
    if not isinstance(k,(list,tuple)):
        return {}
    d=dict()
    for i in k:
        if not isinstance(i,(tuple,list)):
            continue
        if isinstance(i[0],dict):
            key=tuple(sorted(i[0].items()))
        elif isinstance(i[0],list):
            key=tuple(i[0])
        elif isinstance(i[0],set):
            key=tuple(sorted(i[0]))
        else:
            key=i[0]
        if key not in d:
            d[key]=[]
        d[key].append(i[1:])
    return d

data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
print(group_by_key(data))
print(group_by_key(w)) # takes first value of list/tuple in the list/tuple as key and rest as value

test_data = [
    # Group 1: Integer key (1)
    (1, "apple"),
    (1, "apricot"),
    
    # Group 2: List key ([10, 20])
    ([10, 20], "carrot"),
    ([10, 20], "celery"),
    
    # Group 3: Set key ({30, 40}) - order in set doesn't matter since it gets sorted
    ({30, 40}, "date"),
    ({40, 30}, "dragonfruit"), # Will match the same set group
    
    # Group 4: Dict key ({"a": 1, "b": 2})
    ({"a": 1, "b": 2}, "egg"),
    ({"b": 2, "a": 1}, " eggplant"), # Will match because keys are sorted
    
    # Ignored elements (testing defensive branches)
    "I should be skipped",
    42,
    ([], "orphan list - missing inner structure or skipped if not length >= 1"),
]
print(group_by_key(test_data))
