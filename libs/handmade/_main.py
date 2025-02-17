#made by sand
from time import sleep,monotonic
from libs.progress.bar import Bar
from math import floor,ceil
from .utils import *
import libs.vlc as vlc
import threading
import platform


def init_main( self ):
    self.sys_os = platform.system().lower()
    self.sys_architecture = platform.machine()
    self.repeat = 0 #1 pour repeter en boucle la chanson
    self.stay = True  # False pour quiter le lecteur
    self.pause = 0  # pour mettre en pause le lecteur+la barre
    self.bar = None   # la barre de progression du temps de la chanson 
    self.search = False   # True pour cacher l'affichage
    self.player = vlc.MediaPlayer()  # lecteur
    self.played = []  # historique
    self.MainThread = threading.currentThread()
    self.tooltips = {
            "h": "pour afficher le menu help",
            "q": "pour quitter le lecteur",
            "n": "pour aller a la chanson suivante",
            "r": "pour rechercher un son dans le catalogue",
            "l": "pour actualiser l'affichage",
            "s": "pour changer de mode aleatoire/dans l'ordre",
            "y": "pour changer le repertoire d'origine",
            "+": "pour avancer de 10 seconde",
            "-": "pour reculer de 10 seconde",
            "p": "pour monter le son de 10%",
            "m": "pour baisser le son de 10%",
            "a": "pour recharger le catalogue de chanson et d'image",
            "b": "pour charger la  chanson précédente",
            "i": "pour afficher l'historique",
            "c": "pour activer/desactiver des dossiers",
            "d": "pour mute/unmute le son",
            "o": "pour jouer en boucle",
            "e": "pour changer le message de choix",
            "g": "changer de gestionnaire de volume",
            "j": "pour selectionner une image dans la galerie",
            "t": "pour afficher/cacher les images",
            "u": "pour sauvegarder les parametre actuel",
            "dl" :"pour rechercher sur youtube",
            "x": "pour télécharger une playlist youtube",
            "v": " pour modifier une commande",
            "w": "pour remetre les paramètre a 0",
            "z": "pour supprimer/deplacer/renommer un fichier"
            }

        
def main( self ):
    """
    cette fonction est la fonction d'initialisation du programme et de fonctionnement 
    """
    self.get_param()#init
    self.start_sound()
    progress = threading.Thread( target = self.update )#init
    progress.start()#init
    self.get_img( self.path_to_img,start = 1 )#init
    self.check_adress()
    self.load_songs()#init
    
    while len( self.files ) == 0:
        self.out( "no song in folder" )
        self.change_main_path()
        self.load_songs()
        
    if self.battery_exist:
        self.get_battery_life()#init

    if self.sound_manager != "base":
        self.display()
    
    while self.stay != False:
        self.get_input()#interface
        
        if not progress.is_alive():
           self.stay = False
            
    self.player.stop()#end
    self.write_param()#sauvegarde es parametre
    
    
def update( self ):
    """
    cette fonction afiche la bar de progression et la mettre a jour ainsi que
    passer a la chason suivant a la fin de l'actuel 
    """
    time0 = self.player.get_time()#temps initial
    
    while self.stay:
        if not self.MainThread.is_alive():
            self.stay = False
            self.player.stop()#end
            self.write_param()#sauvegarde es parametre
            
        time0 = self.player.get_time()# temps actuel
        sleep( 0.5 )
        time = self.player.get_time()#temps actuel
        
        if self.bar == None and self.song != None:#chanson demarré 
            Max = self.player.get_length()
            self.bar = Bar( "time(s)", max=floor( Max/1000 ), fill="■" )
            
        #print(self.bar,self.search)   
        if self.bar != None and not self.search and not self.pause:#chason en cours et pas de pause/suspension     
            if time/1000 > self.bar.max:#idk really
                continue
            
            if self.bar.index < 0:##en cas de reculer en desosus du debut
                self.bar.index = 0
                
            if time < 0:#en cas de reculer en desosus du debut
                time = 0
                
            if time/1000 > self.bar.index:#la chanson a avancer
                self.bar.index = floor( time/1000 )
                self.bar.update()
            
            if ceil( time/1000 ) >= self.bar.max : #la chanson est fini
                if self.bar.index > 1:# la chason est bien fini et ne vien pas de commencer
                    if not self.repeat:
                        self.choose_song()
                    self.play()
                    
        if time == time0 and self.song != None and not self.search and not self.pause:
            if not self.repeat:
                self.choose_song()
            self.play()
            
def get_input( self ):
    """
    cette fonction est le menu principal qui permet a l'utilisateur d'interagir avec le programme
    """
    got = self.ask( ":" ).lower()#ignorer les majuscules
    
    if all_numbers( got, len( self.files ), 1 ):#chanson selectionné
            white()
            self.search = False
            self.song = self.files[ int(got) ]
            self.play()
            
    if self.search:#recherche terminé
        self.search = False
        
    elif got == "" and self.song != None:#pause 
        self.wind( 6 )
        
    x = 0
    stop = False
    
    while x < len( self.holders ) and not stop:#executer la premier commande contenu dans la chaine donné par l utilisateur
        if self.holders[ self.command[ x ] ] in got:#prenant en compte les modification de l'utilisateur 
            if self.commands[ self.command[ x ] ] == "+":
                command = "plus_f"
                
            elif self.commands[ self.command[ x ] ] == "-":
                command = "minus_f"
                
            else:
                command = self.commands[ self.command[ x ] ] + "_f"
                
            getattr( self,command )()#lancer la function souhaité
            stop = True
            
        x+=1
    
    
def load_all( self ):
    """
    cette fonction permet de recharger toute les images ainsi que toute les chanson et
    remmetre a 0 le lecteur en passant
    """
    self.player.stop()
    self.load_songs()
    self.get_img( self.path_to_img, start = 1 )
    
    
def wind( self , mode ):
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
    if mode == 1:
        self.player.set_time( self.player.get_time() + 10000 )
    
    if mode == 2:
        self.player.set_time( int( self.player.get_time() - 10000 ) )
        self.bar.index = max( 0, self.bar.index - 10 )
    
    if mode == 3:
        self.volume = min( 100, self.volume + 5 )
        self.set_volume()
        
    if mode == 4:
        self.volume = max( 0, self.volume - 5 )
        self.set_volume()
        
    if mode == 5:
        self.deafen()
    
    if mode == 6:
        self.pause = 1 - self.pause
        self.player.pause()
    
    if mode == 7:
        self.show = 1 - self.show
    
    if mode == 8:
        self.repeat = 1 - self.repeat
    
    if mode == 9:
        self.mode = 1 - self.mode
    
    if mode > 0:
        self.suspend( "display" )
