#made by sand
import alsaaudio


def init_sound( self ):
    self.sound_manager = "base"#either base for linux and windows or alsa for linux 
    self.mute = 0
    
def start_sound( self ):    
    if self.sound_manager == "alsa":
        self.mixer = alsaaudio.Mixer()  
    self.volume = self.get_volume()
    
  
def change_sound_manager( self ):
    print( "0: base inclued in vlc" )
    print( "1: alsaaudio , use global volume ONLY on linux" )
    choice = input("votre choix:")
    
    if choice == "0":
        self.sound_manager = "base"
        
    if choice == "1":
        if "linux" in self.sys_os:
            print(1)
            self.sound_manager = "alsa"
            self.mixer = alsaaudio.Mixer()#start alsa session
    
def get_volume( self ):
    
    if self.sound_manager == "base":
       volume = self.player.audio_get_volume()
       return volume
    
    if self.sound_manager == "alsa":
        volume = self.mixer.getvolume()[ 0 ]
        return volume
        
def set_volume(self):
    
    if self.sound_manager == "base":
        self.player.audio_set_volume( self.volume )
        
    if self.sound_manager == "alsa":
        self.mixer.setvolume( self.volume )
        
def deafen(self):
    
    if self.sound_manager == "base":
        self.mute = 1 - self.mute
        self.player.audio_set_mute( self.mute )
        
    if self.sound_manager== "alsa":
        self.mute = 1 - self.mute
        self.mixer.setmute( self.mute )