import sys

def out( text ):
    sys.stdout.write( text )
    sys.stdout.flush()

def up():
    out( '\x1b[1A' )

def down():
    out( '\n' )

def left(x):
    out( '\x1b[{ x }D' )
    
def right(x):
    out( '\x1b[{ x }C' )

def home():
    out('\x1b[H')

def wipe():
    out('\x1b[2J')

def save():
    out("\x1b7")
    
def load():
    out("\x1b8")

    