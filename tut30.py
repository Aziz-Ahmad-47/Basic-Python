l1=[20,30,40,50,60]
l2=[60,70,80,90,100,101]

for a,b in zip(l1,l2):
    print(a,b)

t=len(l1)
for a in range(t):
    print(l1[a],l2[a])