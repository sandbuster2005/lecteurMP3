#made by sand

from .utils import *


class Command:
    
    
    def __init__( self ):
        self.holders = [ "h", "q", "r", "g", "i", "j", "o", "n", "+", "-", "p", "m", "d", "s", "a", "c", "b", "y", "l", "t", "u", "v", "w", "x", "dl", "z", "e" ]# commande defini par l'utilisateur ( modifiable )
        self.commands = [ "h", "q", "r", "g", "i", "j", "o", "n", "+", "-", "p", "m", "d", "s", "a", "c", "b", "y", "l", "t", "u", "v", "w", "x", "dl", "z", "e" ]# valeurs qui permet d appeler les fonction correspondante ( PAS TOUCHER )
        #abcdeghijlmnopqrstuvwxyz+- :list des commande utilisé de base
        #dl
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
    
    def sort_command( self ):
        """
        cette fonction permet de trier les commandes modifié par l'utilisateur
        en fonction de leur taille puis alphabétiquement en gardant le h(help) en priorité dans l'alphabet
        """
        # all this THING sort commands by lenght then by alphabetical order and put the h on top of the alphabet
        command = self.holders[ 1: ]
        command = sorted( command, key = lambda s: ( -len( s ) ) )
        x = 0
        missing = ""
        while x < len( command ) and missing == "":
            if len( command[ x ] ) == 1:
                missing = command[ x ]
            
            x += 1
        
        command=[ command[ x ] * ( 1 - ( ( len( command[ x - 1 ] ) > 1 ) == ( len( command[ x ] ) == 1 ) == ( len( command[ x + 1 ] ) == 1 ) == True ) ) + "h" * ( ( len( command [ x - 1 ] ) > 1 ) == (len ( command[ x ] ) == 1 ) == ( len( command[ x + 1 ] ) == 1 ) ==  True ) for x in range( len( command ) ) ]
    
        if "h" in command:
            command = command[ :command.index( "h" ) + 1 ]+[ missing ] + command[ command.index( "h" ) + 1 :]
        
        elif len( command[0] ) == 1 :
            command = [ "h" ] + command
        
        elif len( command[ 0 ] ) > 1:
            command += [ "h" ]
        
        command=[self.holders.index(command[x]) for x in range(len(command))]
        self.command=command


                 
                 
                 