#made by sand

from .utils import *


def init_command( self ):
    self.holders = [ "h", "q", "r", "g", "i", "j", "o", "n", "+", "-", "p", "m", "d", "s", "a", "c", "b", "y", "l", "t", "u", "v", "w", "x", "dl", "z", "e" ]# commande defini par l'utilisateur ( modifiable )
    self.commands = [ "h", "q", "r", "g", "i", "j", "o", "n", "+", "-", "p", "m", "d", "s", "a", "c", "b", "y", "l", "t", "u", "v", "w", "x", "dl", "z", "e" ]# valeurs qui permet d appeler les fonction correspondante ( PAS TOUCHER )
    #abcdeghijlmnopqrstuvwxyz+- :list des commande utilisé de base
    #dl
    
def sort_command( self ):
    """
    cette fonction permet de trier les commandes modifié par l'utilisateur
    en fonction de leur taille puis alphabétiquement en gardant le h(help) en priorité dans l'alphabet
    """
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
        command = ["h"] + command
        
    elif len( command[ 0 ] ) > 1:
        command += [ "h" ]
        
    command=[self.holders.index(command[x]) for x in range(len(command))]
    self.command=command


def edit_command( self ):
    """
    cette fonction permet de de modifier les commande du programme a
    l'exception de h(help)
    """
    cmd = self.ask_list( self.help_menu(), text = "enter current command call :", num = False )
    if cmd=="h":
        self.out( "help cannot be modified" )
        return
    
    if cmd in self.holders:
        key = self.ask( "new command call :" )
        
        if not all_numbers( key ):
             if key not in self.holders:
                 self.holders[ self.holders.index( cmd ) ] = key
                 self.write_param()
                 self.sort_command()
             
             else:
                 self.out( "key already exist" )
