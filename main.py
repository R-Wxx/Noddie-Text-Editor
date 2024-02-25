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
    
    def __init__(self, **kwargs):
        # Setting Icon
        try:
            self.__root.wm_iconbitmap("icon.ico")
        except:
            pass

        # Setting Window Size
        try:
            self.__thisWidth = kwargs['width']
            self.__thisHeight = kwargs['height']
        except:
            pass

        # Placing the window at the center of the screen
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth - self.__thisWidth) / 2
        top = (screenHeight - self.__thisHeight) / 2

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # Making it resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        self.__textArea.grid(sticky=N+E+S+W)

        self.__menuFile.add_command(label="New", command=self.__newFile)
        self.__menuFile.add_command(label="Open", command=self.__openFile)
        self.__menuFile.add_command(label="Save", command=self.__saveFile)
        self.__menuFile.add_separator()
        self.__menuFile.add_command(label="Exit", command=self.__quitApplication)
        self.__menuBar.add_cascade(label='File', menu=self.__menuFile)

        self.__menuEdit.add_command('Cut', command=self.__cut)
        self.__menuEdit.add_command('Copy', command=self.__copy)
        self.__menuEdit.add_command('Paste', command=self.__paste)
        self.__menuBar.add_cascade(label='Edit', menu=self.__menuEdit)
        
        self.__menuHelp.add_command('About', command=self.__about)
        self.__menuBar.add_cascade(label='Edit', menu=self.__menuHelp)

        self.__scrollBar.config(command=self.__textArea.yview)
        self.__textArea.config(yscrollcommand=self.__scrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __about(self):
        showinfo("Notepad", "Alp")

# Main Application
text_editor = Text_Editor(width=600, height=400)
text_editor.run()