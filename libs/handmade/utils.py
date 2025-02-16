#made by sand
def white(x:int=40):
    for z in range(x):print("")

def replace(word:str,chrs:list):
    return "".join([word[x]*(1-(word[x] in chrs)) for x in range(len(word))])

def all_numbers(word,lim=0,mode=0):
    return all(test in "0123456789" for test in word)==(word!="")==True==(int("".join([str(max(0,int(ord(word[x])-48))) for x in range(len(word))]))*lim<lim*lim-mode+1)

def str_lowerup(word:str,chrs:list,mode=0):
    return "".join([word[x]*(1-(word[x].lower() in chrs))+(word[x].lower())*(word[x].lower() in chrs )*(1-mode)+(word[x].upper())*(word[x] in chrs )*(mode) for x in range(len(word))])
