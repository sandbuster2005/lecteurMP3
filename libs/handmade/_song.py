#made by sand
from random import randint
from .utils import *


def init_song( self ):
    #SONG variables
    self.song = None# son aactuelle
    self.mode = 0# 0:aleatoire 1:dans'l'ordre
        
        
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
    self.suspend( "display" )# affiche
    
    
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
    for x in range( len( self.played ) ):
        print( str( self.played[ x ] ) + " : ", self.files[ self.played [x ] ].rsplit( "/",1 )[ -1 ] )# index : nom
        

def select( self ):
    """
    cette fonction permet de chercher une chanson dans la liste chargé de chanson et l'affiche
    
    limite:
    cette fonction demande une chaine de charactére a rechercher dans les données de l'utilisateur
    """
    self.search = True
    white( 1 )
    INPUT = input( "rechercher dans la liste de chanson :" )
    result = self.find_file( str( INPUT ) )#recherche dans les fichiers
    
    for x in range( len( result ) ):
        print(f"{ result[ x ][ 1 ] } :{ result[ x ][ 0 ] }")
        
    self.get_input()
