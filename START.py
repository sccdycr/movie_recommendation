import GUI.movieInfo_window
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import GlobalVar
import GUI.browseFootprints
import GUI.main_window
import GUI.search_window

#测试main_window
Root = GlobalVar.BigWindow
# style = ttk.Style("darkly")
Root.geometry('800x900')
Frame = tk.Frame(Root,width=800,height=900)
Frame.place(x=0,y=0,anchor="nw")
GUI.main_window.Main_window(Root,Frame,1,None)
Root.mainloop()

