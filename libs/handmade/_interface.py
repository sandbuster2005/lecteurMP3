from time import sleep,strftime
from os.path import isdir
from libs.youtube_search import YoutubeSearch
from .utils import *

def select_img( self ):
    """
    cette fonction permet de choisir une image parmit la galerie ou de choisir aléatoire

    limite:
    cette fonction demande une valeur numérique de l utilisateur pour selectionner l'image
    et affiche le nom de toute les image de la liste

    """

    word = "0"
    while all_numbers( word , len( self.Image.imgs ) ):
        self.Image.imgs.append("random")
        word = self.Display.ask_list( self.Image.imgs, text = "select img:" )
    
        if all_numbers( word, len( self.Image.imgs ) ):
            if int( word ) == len( self.Image.imgs ):
                self.Image.img = ""# aleatoire
                word = ""
        
            else:
                self.external_call( [ f"{ self.Image.img_command }  { self.Image.imgs[ int( word ) ] }" ], True )
                confirm = self.Display.ask( "y/n ?" )
            
                if confirm.lower() == "y":
                    self.Image.img = self.Image.imgs[ int( word ) ] # selection
                    word = ""
        
        self.display()
        
        
def edit_command( self ):
    """
    cette fonction permet de de modifier les commande du programme a
    l'exception de h(help)
    """
    cmd = self.Display.ask_list( self.help_menu(), text = "enter current command call :", num = False )#show current command 
    if cmd=="h":
        self.Display.out( "help cannot be modified" )
        return

    if cmd in self.Command.holders:
        key = self.Display.ask( "new command call :" )
    
        if not all_numbers( key ):
             if key not in self.Command.holders:#if key don't already exist
                 self.Command.holders[ self.Command.holders.index( cmd ) ] = key
                 self.write_param()
                 self.Command.sort_command()
         
             else:
                 self.Display.out( "key already exist" )


def mani_file(self):
    """
    cette fonction permet de supprimer , deplacer(dans les dossiers connu)
    et renommer le fichier actuel
    """
    if self.Core.song != None:
        word = self.Display.ask_list( [ "delete ", "move", "rename"] )
        if all_numbers( word, 2 ):
            if int( word ) == 0:
                choice = self.Display.ask( "are you sure (y/n)" )
            
                if choice == "y":
                    rm_file( self.Core.song )
                
            if int( word ) == 1:
                choice = self.Display.ask_list( [ self.Core.dirs[ x ][ 0 ] for x in range( len( self.dirs ) ) ] )
            
                if all_numbers( choice, len( self.Core.dirs ), mode = 1 ):
                    mv_file( self.Core.song, self.Core.dirs[ int( choice ) ][ 0 ] + "/" + self.Core.song.rsplit( "/", 1 )[ 1 ] )
            
            if int( word ) == 2:
                choice = self.Display.ask( "new_name :" )
                mv_file( self.Core.song, self.Core.song.rsplit( "/",1 )[ 0 ] + choice + "." + self.Core.song.rsplit( ".",1 )[ 1 ])
            
            self.Core.files=self.Core.load_songs()
    

def check_adress( self ):
    """
    cette fonction permet de verifier si l'adresse existe et est un dossier
    """
    if not isdir( self.Core.path_to_file ):
        while not isdir( self.Core.path_to_file ):
            self.Core.path_to_file = self.Display.ask( "enter valid file path: " )
        
    self.write_param()


def change_main_path( self ):
    """
    cette fonction permet de changer l'adresse des chansons
    """
    self.Core.path_to_file = ""
    self.check_adress()


def select_dir( self ):
    """
    cette fonction permet d'activer/desactiver des dossiers de la liste de dossier sous dossier
    pour oculter les chanson qu'il contient

    limite:
    demande une valeur numérique a l'utilisateur pour selectionner un dossier/sous dossiers
    """
    word = "0"
    while all_numbers( word ):
        white()
    
        for x in range( len( self.Core.dirs ) ):
            print( x, self.Core.dirs[ x ] )
        
        word = self.Display.ask_list( self.Core.dirs, text = "switch folder on/off:" )
    
        if all_numbers( word, len( self.Core.dirs ), 1 ):
            self.Core.switch_dir( int( word ) )

def change_sound_manager( self ):
    """
    cette fonction permet de changer le gestionnaire
    """
    choice = self.Display.ask_list( [ "base inclued in vlc", "alsaaudio , use global volume ONLY on linux" ] )
    
    if choice == "0":
        self.Core.sound_manager = "base"
    
    if choice == "1":
        if "linux" in self.sys_os:#si le systeme est compatible
            self.Core.sound_manager = "alsa"
            self.Core.start_sound()#start alsa session

def display( self ):
    """
    cette fonction affiche l'image ,recupére la durée de la chanson ainsi que le nom de la chanson en cours,
    le volume de la musique ainsi que creer la bar de progression si besoin
    
    limite:
    il est nécessaire qu'une chanson soit selectionné
    """
    if self.Core.song != None:
        a = "/"
        sleep( 0.10 )
        white()
        time=strftime( "%H %M" ).split( " " )# affiche l'heure au format standard
        self.Core.volume = self.Core.get_volume()
        self.Image.display_img()
        
        if self.Batterie.battery_exist:
            self.Batterie.get_battery_life()
            print( f"{ time[ 0 ] }:{ time[ 1 ] }  batterie : { self.Batterie.get_battery() } %  { self.Batterie.battery_life } h    volume: { self.Core.volume }% " )# heure,batterie,temps restant,volume
        
        else:
            print( f"{ time[ 0 ] }:{ time[ 1 ] }   volume: { self.Core.volume }% " )# heure,volume
        
        print( f"Song: { self.Core.files.index( self.Core.song ) }:{ self.Core.song.rsplit( a, 1 )[ 1 ] }" )# playlist,index,chanson

    else:
        if self.Core.sound_manager != "base":
            print( f"volume :{self.Core.volume}" )
    
    
def yt_search( self ):
    """
    cette fonction permert de faire une recherche sur youtube et de télécharger l'audio d'une video,
    elle propose les 10 premiers resultat
    
    limite:
    la fonction demande 2 valeur a l'utilisateur: une recherche ,une valeur numérique entre 0 et 9
    ou aucune valeur et affiche les 10 resultat obtenu de youtube
    certain charactère du titre seront supprimé pour le bon fonctionnement du programme
    """
    self.search = True
    word = self.Display.ask("votre recherche : ")
    results = YoutubeSearch( word, max_results = 10 ).to_dict()#10 premier resultat de la recherche youtube     
    word = self.Display.ask_list( [ results[ x ].get( "title" ) for x in range ( len( results ) ) ])
    
    if all_numbers( word, 10, 1 ):
        title = replace( results[ int( word ) ].get( "title" ), [ "(", "'", '"', ")", " ", ":", "|", "&"] )#formatage pour eviter les crash
        link = "https://www.youtube.com" + results[ int( word ) ].get( "url_suffix" )
        print( link ) 
        self.external_call( [ f"./yt-dlp -x --audio-format mp3 -o { self.path_to_file }download/{ title } { link } " ], shell = True )# telechargement en externe en .mp3


def dl_yt_playlist( self ):
    """
    cette fonction permet d'enregistre une chanson/ playlist de chanson  a partir de son url
    elle verifie aussi si toute les chanson on été télécharger sans probléme
    """
    playlist = self.Display.ask( "playlist/song url:" )
    lenght = self.Display.ask("lenght of playlist:")
    new_lenght=0
    if all_numbers( lenght ):
        lenght = int( lenght )
        for f in listdir( "{ self.path_to_file }/download" ):
            lenght += 1
            
        self.external_call( [ f"./yt-dlp -x --audio-format mp3 -P /{ self.path_to_file }download/ { playlist } " ], shell = True ) # telechargement chanson / playlist en .mp3
        
        for f in listdir( "{ self.path_to_file }/download" ):
            new_lenght += 1
        
        if new_lenght!=lenght:
            self.Display.out( f"{ lenght-new_lenght } songs don't seem to have been downloaded" )

