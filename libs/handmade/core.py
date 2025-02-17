#made by sand
from os import listdir
from os.path import isdir,isfile
from .ffiles import*
from .utils import *
from random import randint
import libs.vlc as vlc

class Core:
    
    
    def __init__( self ):
        self.path_to_file = r"/home/sand/Musique/musique/"# chemin du dossier musique
        self.dirs = []# liste des dossier dans le chemin indiqué
        self.files = []# chanson chargé
        self.favorite = ""
        self.song = None# son aactuelle
        self.mode = 0# 0:aleatoire 1:dans'l'ordre
        self.player = vlc.MediaPlayer()  # lecteur
        self.played = []  # historique    
        self.init_sound()
    
    from libs.handmade._sound import init_sound,start_sound,get_volume,set_volume,deafen 
        
    def get_file( self, path, files = [] ):
        """
        cette fonction permet de récuperer tout les fichier waw,mp3 et m4a dans un dossier et sous dossiers,
        elle remet aussi a 0 l'historique ,stop toute chanson en cours de lecture et ajoute a la liste des dossiers
        le dossiers et les sous dossiers si il n'y sont pas
    
        limite:
        path est un chemin d'accés auquel l'utilisateur peut accéder
        files est une liste qui peut contenir des chemin d'accés auquel l'utilisateur peut accéder au préalable
        renvoie les ficher déja inclus et ceux du dossier scanné
        """
        self.song = None
        self.played = []
        self.player.stop()
        for f in listdir( path ):
            if isdir( path + f ):
            
                if [ path + f , '1' ] in self.dirs:# le dossier est activé
                    files += self.get_file( path + f + "/", [] )
            
                elif [ path + f, '0' ] in self.dirs:# le dossier est desactivé 
                    continue
            
                else:# le dossier n'est pas repertorié
                    files += self.get_file( path + f + "/", [] )
                    self.dirs.append( [ path + f, '1' ] )
                
            if f[ -4: ] == ".mp3"  or f[ -4: ] == ".m4a" or f[ -4: ] == ".wav":#le fichier est un audio
                files.append( path + "/" + f )
            
        return files


    def switch_dir( self, word ):
        """
        cette fonction permet d'activer ou desactiver un dossier de la liste
        """
        self.dirs[ word ][ 1 ] = str( 1 - int( self.dirs[ word ][ 1 ] ) )
  
  
    def find_file( self, word ):
        """
        cette fonction renvoie une liste contentant toute les chaine de charactères de la liste de chanson chargés
        contenant une chaine de charactère word
    
        limite:
        toute les charactère sont considérée comme minuscule
        """
        return [ [ self.files[ x ].rsplit( "/" )[ -1 ], x ] for x in range(len(self.files)) if word.lower() in self.files[ x ].lower().rsplit( "/", 1 )[ -1 ] ]#cherche dans la liste de son en ignorant les majuscules    


    def select( self ):
        """
        cette fonction permet de chercher une chanson dans la liste chargé de chanson et l'affiche
    
        limite:
        cette fonction demande une chaine de charactére a rechercher dans les données de l'utilisateur
        """
        self.search = True
        white( 1 )
        INPUT = self.Display.ask( "rechercher dans la liste de chanson :" )
        result = self.find_file( str( INPUT ) )#recherche dans les fichiers
    
        for x in range( len( result ) ):
            self.Display.show_list( [ f"{ result[ x ][ 1 ] } :{ result[ x ][ 0 ] }" for x in range( len( result ) ) ] )
        
        self.get_input()
     
             
    def choose_song( self ):
        """
        cette fonction permet de:
        choisir une chanson aléatoire : mode 0
        choisit la chanson qui suit dans la liste : mode 1 
        """
        if self.mode == 0:
            self.song = self.files[ randint( 0, len( self.files ) - 1 ) ]#chanson aleatoire
        
        if self.mode == 1:
            if self.song == None:
                self.song = self.files[ 0 ]# si pas de chanson joué avant prendre la premiére
                
            else:
                self.song = self.files[ ( self.files.index( self.song ) + 1 ) % len( self.files ) ]#chanson suivante : index+1


    def load_songs( self ):
        """
        cette fonction permet de charge en memoire les chanson de la playlist selectionné/toute
        et de remmetre a 0 le lecteur
        """     
        self.files = self.get_file( self.path_to_file, [] )
        self.song = None
        self.bar = None


    def play_song( self ):
        """
        cette fonction lance le choix de chanson et la joue
        """
        if len( self.files ) != 0:
            self.choose_song()
            self.play()
            self.pause = 0
    
    
    def play( self ):
        """
        cette fonction lance la musique actuel ,l'ajoute a l'historique et affiche l intérface
    
        limite:
        une musique doit étre selectionné au préalable 
        """
        self.bar = None
    
        if self.played == []:
            self.played.append( self.files.index( self.song ) )# ajoute a l'historique
        
        elif self.played[ -1 ] != self.files.index( self.song ):# ajoute a l'historique si la chanson a changé
            self.played.append( self.files.index( self.song ) )
        
        self.player.set_mrl( self.song )# charge la chanson
        self.player.play()
        
    
    
    def play_last( self ):
        """
        cette fonction permet de jouer la chanson precedante a condition qu'il y en est une
        """
        if len(self.played) > 1:
            self.played.pop()
            self.song = self.files[ self.played[ -1 ] ]
            self.bar = None
            self.play()
        
        
    def historic( self ):
        """
        cette fonction affiche l'historique d'écoute de la session 
        """
        self.Display.show_list( [ f"{ self.played[ x ] }: { self.files[ self.played [ x ] ].rsplit( "/",1 )[ -1 ] }" for x in range( len( self.played ) ) ], num = False )# index : nom
        


