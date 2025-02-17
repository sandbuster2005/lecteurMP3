#made by sand
from time import sleep,monotonic
from libs.progress.bar import Bar
from math import floor,ceil
from .utils import *
import threading
import platform
import subprocess
from .ffiles import *

def init_main( self ):
    self.sys_os = platform.system().lower()
    self.sys_architecture = platform.machine()
    self.repeat = 0 #1 pour repeter en boucle la chanson
    self.stay = True  # False pour quiter le lecteur
    self.pause = 0  # pour mettre en pause le lecteur+la barre
    self.bar = None   # la barre de progression du temps de la chanson 
    self.search = False   # True pour cacher l'affichage
    self.param = "appdata/param.txt"#fichier de sauvegarde des paramétre
    self.MainThread = threading.currentThread()


def external_call( self, arg, shell = False ):
    """
    cette fonction permet d'executer des commandes dans le cmd avec ou sans
    shell
    """
    if shell == False :
        subprocess.Popen( arg ).wait()
        
    elif shell == True:
        subprocess.Popen( arg, shell = True ).wait()
  

def help_menu( self ):
        """
        cette fonction se sert du dico qui contient les info pour renvoier une
        liste de toute les info
        """
        return [ "entrer un nombre pour lancer la chanson correspondante", "ne rien rentrer pour mettre pause/actualiser" ]+[f"{ self.holders[ x ] } : { self.tooltips[ self.commands[ x ] ] }" for x in range( len( self.commands ) ) ]


def main( self ):
    """
    cette fonction est la fonction d'initialisation du programme et de fonctionnement 
    """
    self.get_param()#get param from file if it exist else create it
    progress = threading.Thread( target = self.update )#create update thread
    progress.start()
    self.Image.get_img( self.Image.path_to_img,start = 1 )#scan all image in repertory
    self.check_adress()#see if current file adress exist
    self.Core.load_songs()#try to load the song
    
    while len( self.Core.files ) == 0:# if folder is empty
        self.Display.out( "no song in folder" )
        self.change_main_path()
        self.Core.load_songs()
        
    if self.Batterie.battery_exist:#your not dumb are you ?
        self.get_battery_life()#init

    if self.Core.sound_manager != "base":#base sound manager need a media playing to get voulme
        self.display()
    
    while self.stay != False:
        self.get_input()#interface
        
        if not progress.is_alive():#if update thread crashed quit main thread
           self.stay = False
            
    self.Core.player.stop()#end
    self.write_param()#sauvegarde es parametre
    
    
def update( self ):
    """
    cette fonction afiche la bar de progression et la mettre a jour ainsi que
    passer a la chason suivant a la fin de l'actuel 
    """
    time0 = self.Core.player.get_time()#temps initial
    
    while self.stay:
        if not self.MainThread.is_alive():
            self.stay = False
            self.Core.player.stop()#end
            self.write_param()#sauvegarde es parametre
            
        time0 = self.Core.player.get_time()# temps actuel
        sleep( 0.5 )
        time = self.Core.player.get_time()#temps actuel
        
        if self.bar == None and self.Core.song != None:#chanson demarré 
            Max = self.Core.player.get_length()
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
                        self.Core.choose_song()
                    self.Core.play()
                    
        if time == time0 and self.Core.song != None and not self.search and not self.pause:
            if not self.repeat:
                self.choose_song()
            self.play()
            self.suspend( "display" )# affiche
            
            
def get_input( self ):
    """
    cette fonction est le menu principal qui permet a l'utilisateur d'interagir avec le programme
    """
    got = self.Display.ask( ":" ).lower()#ignorer les majuscules
    
    if all_numbers( got, len( self.Core.files ), 1 ):#chanson selectionné
            white()
            self.search = False
            self.Core.song = self.Core.files[ int(got) ]
            self.Core.play()
            
    if self.search:#recherche terminé
        self.search = False
        
    elif got == "" and self.song != None:#pause 
        self.wind( 6 )
        
    x = 0
    stop = False
    
    while x < len( self.Command.holders ) and not stop:#executer la premier commande contenu dans la chaine donné par l utilisateur
        if self.Command.holders[ self.Command.command[ x ] ] in got:#prenant en compte les modification de l'utilisateur 
            if self.Command.commands[ self.Command.command[ x ] ] == "+":
                command = "plus_f"
                
            elif self.Command.commands[ self.Command.command[ x ] ] == "-":
                command = "minus_f"
                
            else:
                command = self.Command.commands[ self.Command.command[ x ] ] + "_f"
                
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
    self.Image.get_img( self.Image.path_to_img, start = 1 )
    
    
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
        self.Core.player.set_time( self.Core.player.get_time() + 10000 )
    
    if mode == 2:
        self.Core.player.set_time( int( self.Core.player.get_time() - 10000 ) )
        self.bar.index = max( 0, self.bar.index - 10 )
    
    if mode == 3:
        self.Core.volume = min( 100, self.Core.volume + 5 )
        self.Core.set_volume()
        
    if mode == 4:
        self.Core.volume = max( 0, self.Core.volume - 5 )
        self.Core.set_volume()
        
    if mode == 5:
        self.Core.deafen()
    
    if mode == 6:
        self.pause = 1 - self.pause
        self.Core.player.pause()
    
    if mode == 7:
        self.Image.show = 1 - self.Image.show
    
    if mode == 8:
        self.repeat = 1 - self.repeat
    
    if mode == 9:
        self.Core.mode = 1 - self.Core.mode
    
    if mode > 0:
        self.suspend( "display" )


def get_param( self ):
    """
    cette fonction permet de lire le fichier ou sont stocké les parametre
    et de les charger ,et dans le cas ou le fichier n'existe pas le creer
    """
    data = get_data( self.param, [ "|" , "," , "#" ] )# pour extraire les donné
    if data == [] or len( data ) != 10:# si les donné sont corrompu ou n'existe pas
        self.write_param()
        self.help_menu()
        
    else:# attribution des parametre
        self.Core.path_to_file = data[ 0 ][ 0 ][ 0 ]
        self.Image.path_to_img = data[ 1 ][ 0 ][ 0 ]
        self.Core.sound_manager = data[ 3 ][ 0 ][ 0 ]
        self.Image.img = data[4][0][0]
        self.repeat = int(data[5][0][0])
        self.Core.dirs = data[6]
        self.Command.holders  = [ data[ 7 ][ x ][ 0 ] for x in range( len( data[ 7 ] ) ) ]
        self.Display.graphic_manager = data[ 8 ][ 0 ][ 0 ]
        self.Display.confirmation = data[ 9 ][ 0 ][ 0 ]
        self.Command.sort_command()
    
    
def write_param( self ):
    """
    cette fonction permet d'ecrire les parametre actuel en memoire
    dans le fichier param
    """
    data = [ str( self.Core.path_to_file ), str( self.Image.path_to_img ), str( self.Core.mode ), self.Core.sound_manager, str( self.Image.img ), str( self.repeat ), self.Core.dirs, self.Command.holders, self.Display.graphic_manager, self.Display.confirmation ]# tout les parametre a stocker
    data = join_list( data,[ "|", ",", "#" ] )# formatage pour l'ecriture
    write_file( self.param, data )
    self.Command.sort_command()
    
    
def reset( self ):
    """
    cette fonction permet de remmetre a 0 les parrametre actuel et
    se enregistrer dans le fichier param
    """
    self.__init__()#remise a 0
    self.write_param()
