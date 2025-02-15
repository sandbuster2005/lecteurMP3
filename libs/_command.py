#made by sand

from .utils import *

def init_command(self):
    # WIP
    self.holders=["h","q","r","k","e","f","g","i","j","o","n","+","-","p","m","d","s","a","c","b","y","l","t","u","v","w","x","dl","z","fv"]# commande defini par l'utilisateur
    self.command=[x for x in range(28)]# index des commande
    self.commands=["h","q","r","k","e","f","g","i","j","o","n","+","-","p","m","d","s","a","c","b","y","l","t","u","v","w","x","dl","z","fv"]# valeurs qui permet d appeler les fonction correspondante 
    #abcdefghijklmnopqrstuvwxyz+- :list des commande utilisé de base
    #dl,    
def sort_command(self):
    """
    cette fonction permet de trier les commandes modifié par l'utilisateur
    en fonction de leur taille et en gardant le h(help) en priorité
    """# WIP 
    command=self.holders[1:]
    command=sorted(command, key=lambda s: (-len(s)))
    x=0
    missing=""
    while x<len(command) and missing=="":
        if len(command[x])==1:
            missing=command[x]
            
        x+=1
        
    #print(missing)
    command=[command[x]*(1-((len(command[x-1])>1)==(len(command[x])==1)==(len(command[x+1])==1)==True))+"h"*((len(command[x-1])>1)==(len(command[x])==1)==(len(command[x+1])==1)==True) for x in range(len(command))]
    #print(command)
    if "h" in command:
        command=command[:command.index("h")+1]+[missing]+command[command.index("h")+1:]
        
    elif len(command[0])==1:
        command=["h"]+command
        
    elif len(command[0])>1:
        command+=["h"]
        
    #print(command)
    command=[self.holders.index(command[x]) for x in range(len(command))]
    self.command=command
    #print(self.command)


def edit_command(self):
    """
    cette fonction permet de de modifier les commande du programme a
    l'exception de h(help)
    """# WIP
    self.h_f()
    cmd=input("enter current command call :")
    if cmd=="h":
        print("help cannot be modified")
        return
    
    if cmd in self.holders:
        key=input("new command call :" )
        if not all_numbers(key):
             if key not in self.holders:
                 self.holders[self.holders.index(cmd)]=key
                 self.write_param()
                 self.sort_command()
             else:
                 print("key already exist")
