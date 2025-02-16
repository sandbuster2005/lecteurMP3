#made by sand
from libs.youtube_search import YoutubeSearch
from .utils import *
def init_download(self):
    pass
def yt_search(self):
    """
    cette fonction permert de faire une recherche sur youtube et de télécharger l'audio d'une video,
    elle propose les 10 premiers resultat
    
    limite:
    la fonction demande 2 valeur a l'utilisateur: une recherche ,une valeur numérique entre 0 et 9
    ou aucune valeur et affiche les 10 resultat obtenu de youtube
    certain charactère du titre seront supprimé pour le bon fonctionnement du programme
    """
    self.search=True
    word=input("votre recherche : ")
    results=YoutubeSearch(word, max_results=10).to_dict()#10 premier resultat de la recherche youtube
    for x in range(len(results)):
        print(x,results[x].get("title"))
        
    word=input("your selection : ")
    if all_numbers(word,10,1):
        title=replace(results[int(word)].get("title"),["(","'",'"',")"," ",":","|","&"])#formatage pour eviter les crash
        link="https://www.youtube.com"+results[int(word)].get("url_suffix")
        print(link) 
        self.external_call(["ls"],shell=True)
        self.external_call([f"./yt-dlp -x --audio-format mp3 -o {self.path_to_file}download/{title} {link} "], shell=True)# telechargement en externe en .mp3


def dl_yt_playlist(self):
    """
    cette fonction permet d'enregistre une chanson/ playlist de chanson  a partir de son url
    """
    playlist=input("playlist/song url:")
    lenght=input("lenght of playlist:")#wip
    if all_numbers(lenght):#wip
        lenght=int(lenght)#wip
        for f in listdir("{self.path_to_file}/download"):#wip
            lenght+=1#wip
            
        self.external_call([f"./yt-dlp -x --audio-format mp3 -P /{self.path_to_file}download/ {playlist} "], shell=True) # telechargement chanson / playlist en .mp3
