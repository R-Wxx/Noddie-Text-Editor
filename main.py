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
    __menuFile = Menu(__menuBar, tearoff=0)
    __menuEdit = Menu(__menuBar, tearoff=0)
    __menuHelp = Menu(__menuBar, tearoff=0)

    # scrollbars
    __scrollBar = Scrollbar(__textArea)
    __file = None
    
    def __init__(self, **kwargs):
        # Setting Icon
        try:
            self.__root.wm_iconbitmap("noddie_icon.ico")
        except Exception as e:
            print(e)

        # Setting Window Size
        try:
            self.__thisWidth = kwargs['width']
            self.__thisHeight = kwargs['height']
        except:
            pass

        self.__root.title("Untitled - Noddie")

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

        self.__menuEdit.add_command(label='Cut', command=self.__cut)
        self.__menuEdit.add_command(label='Copy', command=self.__copy)
        self.__menuEdit.add_command(label='Paste', command=self.__paste)
        self.__menuBar.add_cascade(label='Edit', menu=self.__menuEdit)
        
        self.__menuHelp.add_command(label='About', command=self.__about)
        self.__menuBar.add_cascade(label='Help', menu=self.__menuHelp)

        self.__root.config(menu=self.__menuBar)
        self.__scrollBar.pack(side=RIGHT, fill=Y)

        self.__scrollBar.config(command=self.__textArea.yview)
        self.__textArea.config(yscrollcommand=self.__scrollBar.set)

    def __newFile(self):
        self.__root.title("Untitled - Noddie")
        self.__file = None
        self.__textArea.delete(1.0, END)
    
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Noddie")
            self.__textArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__textArea.insert(1.0, file.read())

            file.close()

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Noddie_Document.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__textArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + " - Noddie")
        
        else:
            file = open(self.__file, "w")
            file.write(self.__textArea.get(1.0, END))
            file.close()
    
    def __quitApplication(self):
        self.__root.destroy()

    def __cut(self):
        self.__textArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__textArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__textArea.event_generate("<<Paste>>")

    def __about(self):
        showinfo("Notepad", "Alp")

    def run(self):
        self.__root.mainloop()

# Main Application
text_editor = Text_Editor(width=600, height=400)
text_editor.run()