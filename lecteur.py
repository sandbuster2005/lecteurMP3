#made by sand
from libs.handmade.display import Display
from libs.handmade.command import Command
from libs.handmade.image import Image
from libs.handmade.battery import Batterie
from libs.handmade.core import Core
from libs.handmade.utils import *
from libs.handmade.ffiles import *

class App:
    def __init__( self ):
        self.init_main()
        self.init_letter()
        
        self.Core = Core()
        self.Batterie = Batterie()
        self.Image = Image()
        self.Command = Command()
        self.Display = Display()
    
    from libs.handmade._interface import select_img,edit_command,mani_file,check_adress,change_main_path,change_sound_manager,display,yt_search,dl_yt_playlist,select_dir       
    from libs.handmade._main import init_main,main,update,get_input,load_all,wind,get_param,write_param,reset,external_call,help_menu
    from libs.handmade._letter import init_letter,suspend,a_f,b_f,c_f,d_f,e_f,g_f,h_f,i_f,j_f,l_f,m_f,n_f,o_f,p_f,q_f,r_f,s_f,t_f,u_f,v_f,w_f,x_f,y_f,z_f,plus_f,minus_f,dl_f
    
       
app = App()
app.main()

