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
    "age": 30,                              # Integer
    "height": 5.9,                          # Float
    "is_active": True,                      # Boolean
    "scores": [85, 90, 95],                 # List
    "metadata": {"id": 101, "role": "admin"}, # Dictionary
    "coordinates": (12.9716, 77.5946)       # Tuple
}
print(({1:2,3:4}),)
def invert_dict(d):
    i_d=dict()
    val=[]
    s=()
    for i in d:
        cur_val=d[i]
        if not isinstance(cur_val,(dict,list)) and cur_val not in val:
            i_d[cur_val]=i 
            val.append(cur_val)
        elif cur_val in val:
            s+=(i,)+(i_d[cur_val],)
            i_d[cur_val]=s   
        else:
            if isinstance(cur_val,(list)):
                cur_val=tuple(cur_val)
                i_d[cur_val]=i
                val.append(cur_val)
            elif isinstance(cur_val,(dict)):
                cur_val=tuple(sorted(cur_val.items()))
                i_d[cur_val]=i
                val.append(cur_val)

                
    return i_d

print(cost1,invert_dict(mixed_data))

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
            i_d[safe_key] = []
            
        i_d[safe_key].append(key)
        
    return i_d

print(invert_dict_safe(mixed_data))