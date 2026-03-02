course={
  'php':{'duration': '2month','fee':2500,'session':'2021-25'},
  'python':{'duration': '2month','fee':1500,'session':'2021-25'},
  'javascript':{'duration': '2month','fee':1000,'session':'2021-25'},
}
print('''
    1 for print All
    2 for print php
    3 for print python
    4 for print javascript
    5 for exit
''')
a=int(input('enter value for porgram'))
if a == 1:
  print(course)
elif a==2:
  print(''' 
         press 1 for all
         press 2 for single thing ''')
  a = int(input(' enter value for this '))
  if a==1:
   print(' php ',course['php'])
  elif a==2:
    a = int(input(' enter requirement (1 duration ,2 fee ,3 session) '))
    if a== 1:
      print(' the dration of php is ',course['php']['duration'])
    if a== 2:
      print(' the fee of php is ',course['php']['fee'])
    if a== 3:
      print(' the session of php is ',course['php']['session'])
elif a==3:
  print(''' 
         press 1 for all
         press 2 for single thing ''')
  a = int(input(' enter value for this '))
  if a==1:
   print(' python ',course['python'])
  elif a==2:
    a = int(input(' enter requirement (1 duration ,2 fee ,3 session) '))
    if a== 1:
      print(' the dration of python is ',course['python']['duration'])
    if a== 2:
      print(' the fee of python is ',course['python']['fee'])
    if a== 3:
      print(' the session of python is ',course['python']['session'])
elif a==4:
  print(''' 
         press 1 for all
         press 2 for single thing ''')
  a = int(input(' enter value for this '))
  if a==1:
    print(' JS ',course['javascript'])
  elif a==2:
    a = int(input(' enter requirement (1 duration ,2 fee ,3 session) '))
    if a== 1:
      print(' the dration of JS is ',course['javascript']['duration'])
    if a== 2:
      print(' the fee of JS is ',course['javascript']['fee'])
    if a== 3:
      print(' the session of JS is ',course['javascript']['session'])
elif a==5:
   print(exit)
else:
   print('invalid number')