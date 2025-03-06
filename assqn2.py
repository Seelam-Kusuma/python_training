D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
union={**D1,**D2}
print(union)


D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
d_intersection={}
for key1,val1 in D1.items():
    for key2,val2 in D2.items():
        if key1 in key2:
            d_intersection[key1]=val1
print(d_intersection)








minus={}
for key1,val1 in D1.items():
    for key2,val2 in D2.items():
        if key1 == key2:
            del D1[key1]
            
print(D1)




    


for i,j in D1.items():
    if i not in D2:
        D2[i]=j
print(D2)




