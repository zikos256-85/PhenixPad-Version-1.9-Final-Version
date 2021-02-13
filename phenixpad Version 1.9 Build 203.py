import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#code Name : Colombo
#Build:203
class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisdeveloper = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
        		self.__root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            print("Error please to restart")
           

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("New file- phenixpad : version 1.9 Build:203")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy",command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="this information the version phenixpad",command=self.__showAbout)
        self.__thisHelpMenu.add_command(label="About the phenixpad",command=self.__showAbout3)
        self.__thisHelpMenu.add_command(label="SLOPPY SOFTWARE AGREEMENT TERMS",command=self.__showAbout4)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__thisdeveloper.add_command(label="New",command=self.__newFile)
        self.__thisdeveloper.add_command(label="Open",command=self.__openFile)
        self.__thisdeveloper.add_command(label="Save",command=self.__saveFile)
        self.__thisdeveloper.add_command(label="information on this feature",command=self.__showAbout2)
        self.__thisMenuBar.add_cascade(label="developer",menu=self.__thisdeveloper)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("phenixpad","Created by: Sloopy : Version 1.9: if you have encountered a problem in the software, please let us know with this e-mail: phenixdeveloppement85@gmail.com")


    def __showAbout2(self):
        showinfo("developer functionality","the developer functionality allows the developer to continue working with their coding project while using our notepad. you can open your source code created new and even save the rework of your code or project in the notepad.") 

    def __showAbout3(self):
        showinfo("About the phenixpad","Easy to use, we have designed this notepad with useful features.\n It will be updated every month to improve the use of the phenixpad.\n Remember to always update to benefit from the latest improvements.\n created by sloppy technology corporation. All rights reserved.\n This product is provided under the terms of the software contract provided by sloppy.\n Software creation date: 2020.\n Latest version: 1.9 build:203\n created by sloppy.") 
    def __showAbout4(self):
          showinfo("SLOPPY SOFTWARE AGREEMENT TERMS","TERME DU CONTRAT LOGICIEL SLOPPY FOURNIT AUX PHENIX PAD:Le logiciel est protégez par le groupe sloppy ,c'est le groupe sloppy qui se charge du devellopment et de l amelioration de l aplication.\n sloppy ce chargera de faire dans l aplication:\n . Les mise a jour,J'usqua sa fin du support qui est programmée pour le 31 décembre 2021.\nAssurez l amelioration du produit.\nAssurez les correction de bug trouvée dans le produit.\nAssurez le service technique  d aide si un utlisateur recontre des probleme d utilisation de l aplication.\ncondition d instalation du logiciel :nous fournisson le logiciel gratuitement , il n ya pas de restricion d installation  par nombre d'ordinateur , vous pouvez deployez le logiciel sur tout votre parc informatique")
    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:

            #try to open the file 

            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - phenixpad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()





        


    