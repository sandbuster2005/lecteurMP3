#made by sand
from os import listdir
from os.path import isdir,isfile
from random import randint
from .utils import *

    
def init_image( self ):
    
    if "64" in self.sys_architecture:
        self.img_command = "./libs/x86/jp2a_x86 --fill --color-depth=8"
        
    elif "arm" in self.sys_architecture:
        self.img_command = "./libs/arm/jp2a_arm --fill --color-depth=8"
        
    self.path_to_img = "appdata/image/"# chemin du dosier image
    self.imgs = []# liste des images contenu dans le chemin indiqué ,vide = random
    self.img = ""# image actuel
    self.show = True# affiche ou non l'image selectionné
    
    
def get_img( self, path, files = [], start = 0 ):
    """
    cette fonction permet de lister tout les png et jpg contenu dans le dossier image du programme 
    
    limite:
    cette fonction d'accéde pas au sous dossier
    """
    if start:
        self.imgs = []
        
    for f in listdir( path ):
        if isdir( path + f ):# un sous dossier existe
            self.get_img( path + f + "/" , [] )
            
        elif f[ -4: ] == ".png"  or f[ -4: ] == ".jpg":# c'est une image supporté par la librairie
            self.imgs.append( path + f )
    
    
def display_img( self ):
    """
    cette fonction affiche dans le terminal ;
    l'image choisis : image précisé
    une image aléatoire de la liste imgs :image non précisé
    
    limite:
    les images doit étre dans le dossiers image du programme
    """
    if self.img != "":# une image est selectionné
        self.external_call( [ f"{ self.img_command } { self.img }" ], True )# image selectionné
        
    if self.img == "" and self.imgs != []:# il y a au moins une image et aucune selcetionné
        self.external_call( [ f"{ self.img_command } { self.imgs[ randint( 0, len( self.imgs ) - 1) ] }" ], True )# image aléatoire
   
   
def select_img( self ):
    """
    cette fonction permet de choisir une image parmit la galerie ou de choisir aléatoire
    
    limite:
    cette fonction demande une valeur numérique de l utilisateur pour selectionner l'image
    et affiche le nom de toute les image de la liste
    
    """
    
    word = "0"
    while all_numbers( word , len( self.imgs ) ):
        for x in range( len( self.imgs ) ):
            print( x, self.imgs[ x ] )
            
        print( len( self.imgs ), "random" )# index max +1
        word = input( "select img:" )
        
        if all_numbers( word, len( self.imgs ) ):
            if int( word ) == len( self.imgs ):
                self.img = ""# aleatoire
                word = ""
            
            else:
                self.external_call( [ f"{ self.img_command }  { self.imgs[ int( word ) ] }" ], True )
                confirm = input( "y/n ?" )
                
                if confirm.lower() == "y":
                    self.img = self.imgs[ int( word ) ] # selection
                    word = ""
            
        self.display()
           