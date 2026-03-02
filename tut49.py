import json

d='{"name":"aziz","roll no":47,"session":"2021-25"}'

x = json.loads(d)
print(type(x))
print(x)

for a in x:
    print(a,x[a])