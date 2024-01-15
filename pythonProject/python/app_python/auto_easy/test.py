import os
import shutil

path = input("ENTER PATH: ")
os.path.normpath(path)
i=1
LIST_FORDEL = {}
for d in os.listdir(path): 
    link = os.path.join(path, d)
    if os.path.isdir(link):
        LIST_FORDEL[str(i)]=link
        print(str(i) + ": " + d)
        i+=1
print(LIST_FORDEL.get("1"))
print(os.path.split(LIST_FORDEL.get("1"))[1])

dic = {"1": 1, "2": 2}
print(dic)