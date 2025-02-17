#made by sand
from os import listdir
from os.path import isdir,isfile
from random import randint
from .utils import *
import platform
import subprocess

def external_call(arg, shell = False ):
    """
    cette fonction permet d'executer des commandes dans le cmd avec ou sans
    shell
    """
    if shell == False :
        subprocess.Popen( arg ).wait()
        
    elif shell == True:
        subprocess.Popen( arg, shell = True ).wait()
        
        
class Image:
    
    
    def __init__( self ):
        self.local_bin = True
        self.path_to_img = "appdata/image/"# chemin du dosier image
        self.imgs = []# liste des images contenu dans le chemin indiqué ,vide = random
        self.img = ""# image actuel
        self.show = True# affiche ou non l'image selectionné
    
        if self.local_bin == False:
            self.img_command = "jp2a --fill --color-depth=8"
        
        elif "64" in platform.machine():
            self.img_command = "./libs/x86/jp2a_x86 --fill --color-depth=8"
        
        elif "arm" in platform.machine():
            self.img_command = "./libs/arm/jp2a_arm --fill --color-depth=8"
        
        
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
    
    
    def display_img( self ,img="" ):
        """
        cette fonction affiche dans le terminal ;
        l'image choisis : image précisé
        une image aléatoire de la liste imgs :image non précisé
    
        limite:
        les images doit étre dans le dossiers image du programme
        """
        if self.show:
            if img!="":
                external_call( [ f"{ self.img_command } { img }" ], True )
            
            subprocess.Popen( [ "ls" ] )
            if self.img != "":# une image est selectionné
                external_call( [ f"{ self.img_command } { self.img }" ], True )# image selectionné
        
            if self.img == "" and self.imgs != []:# il y a au moins une image et aucune selcetionné
                external_call( [ f"{ self.img_command } { self.imgs[ randint( 0, len( self.imgs ) - 1) ] }" ], True )# image aléatoire
   
           