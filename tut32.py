l=[]
while True:
 c=int(input('''enter the value 
      1 for push
      2 for pop
      3 for peek
      4 for display stack 
      5 for exit
       '''))
 if c==1:
    n = input("enter value for list ")
    l.append(n)
    print(l)
 elif c==2:
    if len(l)==0:
      print("stake is empty ")
    else:
      p=l.pop()
      print(p)
      print(l)
 elif c==3:
    if len(l)==0:
      print("stake is empty ")
    else:
      print("peek value is ",l[-1])
 elif c==4:
    print("display stake ",l)
 elif c==5:
   break;
     
