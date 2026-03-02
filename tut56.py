# class A:
#     def name(self,name=""):
#         print("my name is aziz ahmad khasman "+name)

# obj = A()
# obj.name(" aziz")
# -----------------------------
# class A:
#     def aziz_info(self):
#         print("name : aziz")
# class B(A):
#     def aziz_info(self):
#      super().aziz_info()
#      print("Rollno : 47")

# obj=B()
# obj.aziz_info()
# ------------------
class A:
    def sum(self):
        print(2+3)
class B(A):
    def sum(self):
        super().sum()
        print(3+3)

obj = B()
obj.sum()