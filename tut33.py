l=[]
while True:
 c=int(input('''enter the value 
      1 for push
      2 for pop
      3 for fornt
      4 for last
      5 for display stack 
      6 for exit
       '''))
 if c==1:
    n = input("enter value for list ")
    l.append(n)
    print(l)
 elif c==2:
    if len(l)==0:
      print("queue is empty ")
    else:
      del l[0]
      print(l)
 elif c==3:
    if len(l)==0:
      print("queue is empty ")
    else:
      print("fornth value is ",l[0])
 elif c==4:
    if len(l)==0:
      print("queue is empty ")
    else:
      print("last value is ",l[-1])
 elif c==5:
    print("display stake ",l)
 elif c==6:
   break;
     