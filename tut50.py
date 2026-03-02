import json
# file= open("tut50.json","r")
# x=file.read()
# fd=json.loads(x)
# for a in fd:
#  print(a['id'])
file= open("tut50.json","w")
x=file.write()
fd=json.dumps(x)
for a in fd:
 print(a)