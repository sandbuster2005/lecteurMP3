#made by sand
from time import sleep,monotonic,strftime
from libs.progress.bar import Bar
from math import floor,ceil
import libs.vlc as vlc
import threading
from .utils import *
import alsaaudio
def init_main(self):
    self.master=alsaaudio.Mixer()
    self.repeat=0#1 pour repeter en boucle la chanson
    self.leave=True# False pour quiter le lecteur
    self.pause=0# pour mettre en pause le lecteur+la barre
    self.bar=None# la barre de progression du temps de la chanson 
    self.search=False# True pour cacher l'affichage
    self.player=vlc.MediaPlayer()# lecteur
    self.played=[]# historique
    self.sound=vol=int(self.master.getvolume()[0])
    self.tooltips={
            "h":"pour afficher le menu help",
            "q":"pour quitter le lecteur",
            "n":"pour aller a la chanson suivante",
            "r":"pour rechercher un son dans le catalogue",
            "l":"pour actualiser l'affichage",
            "s":"pour changer de mode aleatoire/dans l'ordre",
            "y":"pour changer le repertoire d'origine",
            "+":"pour avancer de 10 seconde",
            "-":"pour reculer de 10 seconde",
            "p":"pour monter le son de 10%",
            "m":"pour baisser le son de 10%",
            "a":"pour recharger le catalogue de chanson et d'image",
            "b":"pour charger la  chanson précédente",
            "i":"pour afficher l'historique",
            "c":"pour activer/desactiver des dossiers",
            "d":"pour mute/unmute le son",
            "o":"pour jouer en boucle",
            "k":"pour créer une playlist",
            "e":"pour ajouter des chansons a une playlist",
            "g":"pour afficher les chansons d'une playlist",
            "f":"pour charger une playlist",
            "fv":"pour rajouter/supprimer des favoris",#wip
            "j":"pour selectionner une image dans la galerie",
            "t":"pour afficher/cacher les images",
            "u":"pour sauvegarder les parametre actuel",
            "dl":"pour rechercher sur youtube",
            "x":"pour télécharger une playlist youtube",
            "v":" pour modifier une commande",
            "w":"pour remetre les paramètre a 0",
            "z":"pour supprimer/deplacer/renommer un fichier"
            }

        
def main(self):
    """
    cette fonction est la fonction d'initialisation du programme et de fonctionnement 
    """
    self.get_param()#init
    self.get_img(self.path_to_img,start=1)#init
    self.check_adress()
    self.files=self.load_playlist(self.playlist)#init
    if len(self.files)==0:
        print("no song in folder")
        print(self.tooltips["y"])
    if self.battery_exist:
        self.get_battery_life()#init
        
    progress = threading.Thread(target=self.update)#init
    progress.start()#init
    while self.leave!=False:
        self.get_input()#interface
        
    self.player.stop()#end
    self.write_param()#sauvegarde es parametre
    
    
def update(self):
    """
    cette fonction afiche la bar de progression et la mettre a jour ainsi que
    passer a la chason suivant a la fin de l'actuel 
    """
    time0=self.player.get_time()/1000#temps initial 
    while self.leave:
        time0=self.player.get_time()/1000# temps actuel
        sleep(0.5)
        if self.bar==None and self.song!=None:#chanson demarré 
            Max=self.player.get_length()
            self.bar=Bar("time(s)",max=floor(Max/1000),fill="■")
            
        if self.bar!=None and not self.search and not self.pause:#chason en cours et pas de pause/suspension     
            time=self.player.get_time()/1000#temps actuel
            if time>self.bar.max:#idk really
                continue
            
            if self.bar.index<0:##en cas de reculer en desosus du debut
                self.bar.index=0
                
            if time<0:#en cas de reculer en desosus du debut
                time=0
                
            if time>self.bar.index:#la chanson a avancer
                self.bar.index=floor(time)
                self.bar.update()

            if ceil(time)>=self.bar.max or time==time0:#la chanson est fini
                if self.bar.index>1:# la chason est bien fini et ne vien pas de commencer
                    if not self.repeat:self.choose_song()
                    self.play()


def get_input(self):
    """
    cette fonction est le menu principal qui permet a l'utilisateur d'interagir avec le programme
    """
    got=input(":").lower()#ignorer les majuscules
    if all_numbers(got,len(self.files),1):#chanson selectionné
            white()
            self.search=False
            self.song=self.files[int(got)]
            self.play()
            
    if self.search:#recherche terminé
        self.search=False
        
    elif got=="" and self.song!=None:#pause 
        self.wind(6)
        
    x=0
    stop=False
    while x<len(self.holders) and not stop:#executer la premier commande contenu dans la chai,e donné par l utilisateur
        if self.holders[self.command[x]] in got:#prenant en compte les modification de l'utilisateur 
            if self.commands[self.command[x]]=="+":command="plus_f"#wip
            elif self.commands[self.command[x]]=="-":command="minus_f"#wip
            else:command=self.commands[self.command[x]]+"_f"#wip
            getattr(self,command)()#lacer la function souhaité
            stop=True
        x+=1
     
     
def display(self):
    """
    cette fonction affiche l'image ,recupére la durée de la chanson ainsi que le nom de la chanson en cours,
    le volume de la musique ainsi que creer la bar de progression si besoin
    
    limite:
    il est nécessaire qu'une chanson soit selectionné
    """
    if self.song!=None:
        a="/"
        sleep(0.10)
        white()
        time=strftime("%H %M").split(" ")# affiche l'heure au format standard
        self.sound=vol=int(self.master.getvolume()[0])
        if self.show:
            self.display_img()
        if self.battery_exist:
            self.get_battery_life()
            print(f"{time[0]}:{time[1]}  batterie : {self.get_battery()} %  {self.battery_life} h    volume: {self.sound}% ")# heure,batterie,temps restant,volume
        else:
            print(f"{time[0]}:{time[1]}   volume: {self.sound}% ")# heure,volume
        print(f"Playlist: {self.playlist}   Song: {self.files.index(self.song)}:{self.song.rsplit(a,1)[1]}")# playlist,index,chanson
    
    
def help_menu(self):
    print("entrer un nombre pour lancer la chanson correspondante")
    print("ne rien rentrer pour mettre pause/actualiser")
    for x in range(len(self.commands)):
        print(f"{self.holders[x]} : {self.tooltips[self.commands[x]]}")
        
        
def play(self):
    """
    cette fonction lance la musique actuel ,l'ajoute a l'historique et affiche l intérface
    
    limite:
    une musique doit étre selectionné au préalable 
    """
    self.bar=None
    if self.played==[]:
        self.played.append(self.files.index(self.song))# ajoute a l'historique
        
    elif self.played[-1]!=self.files.index(self.song):# ajoute a l'historique si la chanson a changé
        self.played.append(self.files.index(self.song))
        
    self.player.set_mrl(self.song)# charge la chanson
    self.player.play()
    self.suspend("display")# affiche


def select(self):
    """
    cette fonction permet de chercher une chanson dans la liste chargé de chanson et l'affiche
    
    limite:
    cette fonction demande une chaine de charactére a rechercher dans les données de l'utilisateur
    """
    self.search=True
    white(1)
    INPUT=input(("rechercher dans la liste de chanson :"))
    result=self.find_file(str(INPUT))#recherche dans les fichiers
    for x in range(len(result)):
        print(f"{result[x][1]} :{result[x][0]}")
        
    self.get_input()
    
    
def load_all(self):
    """
    cette fonction permet de recharger toute les images ainsi que toute les chanson et
    remmetre a 0 le lecteur en passant
    """
    self.player.stop()
    self.load_songs(self.playlist)
    self.get_img(self.path_to_img,start=1)


def play_last(self):
    """
    cette fonction permet de jouer la chanson precedante a condition qu'il y en est une
    """
    if len(self.played)>1:
        self.played.pop()
        self.song=self.files[self.played[-1]]
        self.bar=None
        self.play()


def historic(self):
    """
    cette fonction affiche l'historique d'écoute de la session 
    """
    for x in range(len(self.played)):
        print(str(self.played[x])+" : ",self.files[self.played[x]].rsplit("/",1)[-1])# index : nom
    
    
def wind(self,mode):
    """
    cette fonction permet de:
    avancer de 10 seconde : mode 1
    reculer de 10 seconde : mode 2
    augmenter le volume de 10% : mode 3
    baisser le volume de 10% : mode 4
    couper/reactiver le son : mode 5
    mettre la musique en pause : mode 6
    afficher/cacher les image : mode 7
    jouer la chanson en boucle : mode 8
    de jouer en aleatoire/dans l'ordre : mode 9
    et actualise l'affichage a chaque fois
    
    limite:
    le volume du son est compris entre 0 et 100%
    """
    if mode==1:
        self.player.set_time(self.player.get_time()+10000)
    
    if mode==2:
        self.player.set_time(int(self.player.get_time()-10000));self.bar.index=max(0,self.bar.index-10)
    
    if mode==3:
        self.sound+=10
        self.sound=min(100,self.sound)
        self.sound=max(0,self.sound)
        self.master.setvolume(self.sound)
        
    if mode==4:
        self.sound-=10
        self.sound=min(100,self.sound)
        self.sound=max(0,self.sound)
        self.master.setvolume(self.sound)
        
    if mode==5:
        self.master.setvolume(0)
    
    if mode==6:
        self.pause=1-self.pause
        self.player.pause()
    
    if mode==7:
        self.show=1-self.show
    
    if mode==8:
        self.repeat=1-self.repeat
    
    if mode==9:
        self.mode=1-self.mode
    
    if mode>0:
        self.suspend("display")
