def replace(word:str,chrs:list):return "".join([word[x]*(1-(word[x] in chrs)) for x in range(len(word))])
from os import listdir
import os
path="/home/sand/Musique/download"
for f in listdir(path):
    extension="."+f.rsplit(".",1)[1]
    #print(extension)
    file=f.rsplit("[",1)[0]
    #print(file)
    file=replace(file,["(","'",'"',")"," ",":","|","&","[","]"])
    #print(path+"/"+file+extension)
    #print(path+"/"+f)
    #input()
    os.rename(path+"/"+f,path+"/"+file+extension)