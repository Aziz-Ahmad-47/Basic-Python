import pickle
file = open("tut46.txt","rb")
l=pickle.load(file)
print(l)