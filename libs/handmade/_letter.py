#made by sand
def init_letter(self):
    pass

def suspend(self,fonction):
    """
    cette fonction met en pause l'affichage le temps que la fonction
    fonction s'execute
    """
    self.search=1
    getattr(self,fonction)()
    self.search=0

#les fonctions sont relié a self.commands
def q_f(self):
    self.stay=False

def r_f(self):
    self.select()

def k_f(self):
    self.suspend("create_playlist")

def e_f(self):
    self.suspend("add_song")

def f_f(self):
    self.suspend("load_songs")

def g_f(self):
    pass

def i_f(self):
    self.suspend("historic")

def j_f(self):
    self.suspend("select_img")

def o_f(self):
    self.wind(8)

def n_f(self):
    self.play_song()

def plus_f(self):
    self.wind(1)

def minus_f(self):
    self.wind(2)

def p_f(self):
    self.wind(3)

def m_f(self):
    self.wind(4)

def d_f(self):
    self.wind(5)

def s_f(self):
    self.wind(9)

def a_f(self):
    self.load_all()

def c_f(self):
    self.suspend("select_dir")
    self.load_songs(self.playlist)

def b_f(self):
    self.play_last()

def dl_f(self):
    self.yt_search()

def l_f(self):
    self.suspend("display")

def t_f(self):
    self.wind(7)

def u_f(self):
    self.write_param()

def v_f(self):
    self.suspend("edit_command")

def w_f(self):
    self.reset()

def x_f(self):
    self.dl_yt_playlist()
    self.pause=True

def y_f(self):
    self.change_main_path()

def z_f(self):
    self.suspend("mani_file")

def fv_f(self):
    self.add_favorite()#wip
    
def h_f(self):
    self.help_menu()
