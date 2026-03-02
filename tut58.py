class A:
    def __init__(self,stoke):
        self.stoke=stoke
    def total_bike(self):
        print("The total bike in Stoke is ",self.stoke)

    def total_rent(self,q):
        if q<0:
          print(" The number should be positive  :")
        elif q>self.stoke:
          print(" The avalable stoke is ", self.stoke," plece inter less number")
        else:
          print("the total price is ",q*100)
          print("the number of bike is ",self.stoke)

while True:
    print('''
    1 for total bike 
    2 for toal rent 
    3 for exit
    ''')
