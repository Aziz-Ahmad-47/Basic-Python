# total number of bike
# avalaible bike 
# rent of bike
class bike:
  def __init__(self,stock):
     self.stock= stock

  def rents(self,rent):
    if rent<=0: 
      print("enter the positive value grater then zero ")
    elif rent>self.stock:
      print("there is only ",self.stock," bike is avaliable")
    else:
      print("the total rent of bike is ",self.rent*self.stock)

  def bike(self):
    print("the total number of bike is ",self.stock-self.rent)

while True:
  obj=bike(100)
  a=int(input('''
  1 for total find rent
  2 for avaliable bike 
  3 for exit
  '''))
  if a==1:
    n=int(input("enter the quantity of bike --"))
    obj.rents(n)
  elif a==2:
    obj.bike()
  else:
    break;



  
