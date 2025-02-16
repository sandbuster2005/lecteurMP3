#made by sand 
class App:
    def __init__(self):
        self.init_main()
        self.init_battery()
        self.init_command()
        self.init_param()
        self.init_file()
        self.init_image()
        self.init_download()
        self.init_song()
        self.init_playlist()
        self.init_letter()
    from libs.handmade._external import external_call
    from libs.handmade._batterie import init_battery,battery_check,get_battery,get_battery_life
    from libs.handmade._command import init_command,sort_command,edit_command         
    from libs.handmade._param import init_param,get_param,write_param,reset 
    from libs.handmade._files import init_file,get_file,select_dir,switch_dir,find_file,check_adress,change_main_path,mani_file
    from libs.handmade._image import init_image,get_img,display_img,select_img
    from libs.handmade._download import init_download,yt_search,dl_yt_playlist  
    from libs.handmade._song import init_song,choose_song,add_song,load_songs,play_song
    from libs.handmade._playlist import init_playlist,create_playlist,load_playlist,select_playlist,get_psongs,edit_psong,show_psong
    from libs.handmade._main import init_main,main,update,get_input,display,help_menu,play,select,load_all,play_last,historic,wind
    from libs.handmade._letter import init_letter,suspend,a_f,b_f,c_f,d_f,e_f,f_f,g_f,h_f,i_f,j_f,k_f,l_f,m_f,n_f,o_f,p_f,q_f,r_f,s_f,t_f,u_f,v_f,w_f,x_f,y_f,z_f,plus_f,minus_f,dl_f,fv_f
app=App()
app.main()

