#made by sand
from random import randint

def init_song(self):
    #SONG variables
    self.song=None# son aactuelle
    self.mode=0# 0:aleatoire 1:dans'l'ordre
        
def choose_song(self):
    """
    cette fonction permet de:
    choisir une chanson aléatoire : mode 0
    choisit la chanson qui suit dans la liste : mode 1 
    """
    if self.mode==0:
        self.song=self.files[randint(0,len(self.files)-1)]#chanson aleatoire
        
    if self.mode==1:
        if self.song==None:
            self.song=self.files[0]# si pas de chanson joué avant prendre la premiére
            
        else:
            self.song=self.files[(self.files.index(self.song)+1)%len(self.files)]#chanson suivante : index+1


def add_song(self):
    """
    cette fonction permet de rajouter des chansons a une playlist
    une par une ou par dossiers si elle n en font pas deja parti
    
    limite:
    les chansons individuel doivent etre chargé en mémoire pour etre ajouté et ajouter par leur nombre actuel
    la fonction demande des valeurs numérique a l'utilisateur afin de selectionner des dossier/sous dossier/chanson
    """
    playlist=self.select_playlist()
    if playlist!=None:
        i=0
        for x in self.dirs:
            print(i,self.dirs[i][0]);i+=1
            
        print(i,"enter song by number")
        word="1"
        while all_numbers(word):
            word=input("select :")#choisir playlist 
            if allnumbers(word,len(self.dirs)):
                if int(word)==len(self.dirs):#ajouter par chason
                    while all_numbers(word):
                        word=input("enter song number:")
                        if all_numbers(word,len(self.files),1):
                            self.edit_psong(playlist,song=word)
                        
                else:
                    self.edit_psong(playlist,dirs=word)# ajouter par repertoire
           
              
def load_songs(self,playlist=""):
    """
    cette fonction permet de charge en memoire les chanson de la playlist selectionné/toute
    et de remmetre a 0 le lecteur
    """     
    self.files=self.load_playlist(playlist)
    self.song=None
    self.bar=None


def play_song(self):
    """
    cette fonction lance le choix de chanson et la joue
    """
    if len(self.files)!=0:
        self.choose_song()
        self.play()
        self.pause=0
