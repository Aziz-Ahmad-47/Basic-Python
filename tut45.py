# sessor -> rock =rock Win
# page -> rock== page Win
# rock -> page = page win
import random
l = ["Rock", "page", "scissor"]
while True:
   a=int(input('''
     Do You Want to Play game?
     1 Yes
     2 No|exit
'''))
   ucount =0
   ccount = 0
   if a==1:
       for a in range(1,6):
        player = int(input('''
        select one
          1 rock 
          2 page 
          3 scissor
        '''))
        if player==1:
          uc = "Rock" 
        elif player==2:
          uc = "page" 
        elif player==3:
          uc = "scissor" 
        Cc = random.choice(l)
        if uc==Cc:
         print('your choice',uc)
         print('computer choice',Cc)
         print("round draw") 
         ucount = ucount+1
         ccount = ccount+1
        elif (uc=="Rock" and Cc=="seasor") or ( uc =="page" and Cc=="Rock") or (uc=="seasor"and Cc=="page"):
         print('your choice',uc)
         print('computer choice',Cc)
         print("you win")
         ucount=ucount + 1
        else:
         print('your choice',uc)
         print('computer choice',Cc)
         print("computer win")
         ccount=ccount+1
        print("computer  :",ccount)   
        print(" your     :",ucount)
        if ccount==ucount:
          print("match draw")
        elif ccount>ucount:
          print("computer  win match with ",ccount-ucount)
        elif ccount<ucount:
          print("you win the match with ",ucount-ccount)
   elif a==2:
       break;