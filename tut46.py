import pickle
l=[20,30,50,60,70]

file = open("tut46.txt","wb")
pickle.dump(l,file)
file.close()