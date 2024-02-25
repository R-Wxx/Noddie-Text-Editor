from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

class Text_Editor:
    __root = Tk()
    
    # default settings
    __windowWidth = 300
    __windowHeight = 400
    __textArea = Text(__root)
    __menuBar = Menu(__root)

    # menus in the menu bar
    __menuFile = Menu(__menuBar)
    __menuEdit = Menu(__menuBar)
    __menuHelp = Menu(__menuBar)

    # scrollbars
    __scrollBar = Scrollbar(__textArea)
    __file = None
    

# Main Application
text_editor = Text_Editor(width=600, height=400)
text_editor.run()