#made by sand
import subprocess


def external_call( self, arg, shell = False ):
    if shell == False :
        subprocess.Popen(arg).wait()
        
    elif shell == True:
        subprocess.Popen( arg, shell = True ).wait()