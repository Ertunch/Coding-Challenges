#Solution 1
a = [3,2,1]
outcome = []
for i in range(len(a)):
    b=a.copy()
    result = 1
    del b[i]
    for j in b:
        result = result * j
    outcome.append(result)
    
    
    
#Solution 2
a = [3, 2, 1]
e =0
b = []
r=1
while e < len(a):
    for i,j in enumerate(a):
        if i != e:
            r*=a[i]
    b.append(r)
    r = 1
    e+=1

print(b)
