#made by sand
from .ffiles import *
from .utils import *

def init_playlist(self):
    self.playlist=None# playlist selectionné , None = toute les chansons
    
def create_playlist(self):
    """
    cette fonction permet a l'utilisateur de creer une nouvelle playlist vide
    
    limite:
    cette fonction demande un nom a l'utilisateur
    une playlist déja existante sera écrasé
    """
    file=input("playlist name :")
    if file!="":
        write_file("appdata/playlist/"+str(file))


def load_playlist(self,playlist=""):
    """
    cette fonction permet de charger les chanson d'une playlist au choix ou de decharger une playlist
    elle affiche la liste des playlist créé
    
    limite:
    cette fonction demande une valeur a l'utilisateur pour selectionner/deselectioner une playlist
    """
    if playlist=="":# pas de playlist selectionné -> ecran de selection 
        playlist=self.select_playlist()
        
    if playlist==None: # playlist par defaut(toute les chanson) charger tout les repertoire
        self.playlist=None
        files=self.get_file(self.path_to_file,[])
        
    else:#playlist selectionné
        song=self.get_psongs(playlist)#recuperer les chason du fichier
        self.playlist=playlist
        if song!="":
            song=song.split("|||")
            files=[song[x] for x in range(len(song)-1)]
            
    return files
        
        
def select_playlist(self):
    """
    cette fonction affiche les playliste existante et renvoie la playlist choisis par l'utilisateur 
    
    limite:
    il doit exister au moins une playlist
    la fonction demande une valeur numérique a l'utilisateur pour selectionner une playlist
    """
    playlist=None
    if listdir(".appdata/playlist/")!=[]:#une playlist existe
        i=0
        for x in listdir("appdata/playlist/"):
            print(i,x);i+=1
            
        word=input("select playlist :")
        if all_numbers(word,len(listdir("appdata/playlist/")),1):
            playlist=listdir("appdata/playlist/")[int(word)]
            
    else:#sinon crrer une playlist
        create_playlist(self)
        playlist=listdir("appdata/playlist/")[0]
        
    return playlist


def get_psongs(self,playlist):
    """
    cette fonction renvoie les chanson deja presente dans une playlist
    
    limite:
    la playlist doit se trouver dans le dossier playlist 
    """
    with open("appdata/playlist/"+str(playlist),"r") as f:
        return f.read()
    
    
def edit_psong(self,playlist,dirs=None,song=None):
    """
    cette fonction permet de rajouter de chanson a une playlist déja existante
    
    limite:
    soit donner une valeur dirs SOIT une valeur song
    playlist doit se trouver dans le dossier playlist
    """
    songs=self.get_psongs(playlist)
    if dirs!=None:# par chason individuelle
        files=self.get_file(self.dirs[int(dirs)][0])
        
    if song!=None:# par repertoire
        files=[self.files[int(song)]]
        
    song+="".join([x+"|||" for x in files if x not in songs])# ne pas mettre 2 fois le meme 
    with open("appdata/playlist/"+str(playlist),"w") as f:
        f.write(songs)


def show_psong(self):
    """
    cette fonction affiche la liste de chanson d'une playlist
    
    limite:
    cette fonction demande a l utilisateur de rentrer
    aucune valeur pour retourner au menu et
    une valeur numérique pour selectionner la playlist 
    """
    songs=self.load_playlist()
    for x in range(len(songs)):
        print(x,songs[x].rsplit("/",1)[-1])
        
    input("press enter to continue")