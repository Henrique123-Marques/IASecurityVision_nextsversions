import tkinter, customtkinter, os, webbrowser, subprocess
from PIL import Image, ImageTk 
import tkinter
from time import strftime 

customtkinter.set_default_color_theme("files/theme.json")

class ChatBot(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False,False)
        self.title('I.A. Security Vision')
        self.iconbitmap('img\\icon.ico')
        self.fonte = customtkinter.CTkFont(family='Poppins', size=18, weight = 'bold')
        self.fonte14 = customtkinter.CTkFont(family='Poppins', size=14, weight = 'bold')

        self.chattitle = customtkinter.CTkLabel(self, text='ChatBot', font = self.fonte, text_color='#27C4B7').place(relx=0.65, rely=0.1, anchor=customtkinter.CENTER)
        self.buttonA = customtkinter.CTkButton(self, text="Pesquisa", command=self.clickA, fg_color='#27C4B7', font=self.fonte14, corner_radius=30).place(relx=0.1, rely=0.2)
        self.search = customtkinter.CTkImage(Image.open('img/search.png'), size=(25,25))
        self.search = customtkinter.CTkLabel(self, image=self.search, text='').place(relx=0.03, rely=0.2)

        self.buttonB = customtkinter.CTkButton(self, text="Lista de usuários", command=self.clickB, fg_color='#27C4B7', font=self.fonte14, corner_radius=30).place(relx=0.1, rely=0.32)
        self.list = customtkinter.CTkImage(Image.open('img/list.png'), size=(25,25))
        self.list = customtkinter.CTkLabel(self, image=self.list, text='').place(relx=0.03, rely=0.32)

        self.buttonC = customtkinter.CTkButton(self, text="Adicionar usuários", command=self.clickC, fg_color='#27C4B7', font=self.fonte14, corner_radius=30).place(relx=0.1, rely=0.45)
        self.add = customtkinter.CTkImage(Image.open('img/plus.png'), size=(25,25))
        self.add = customtkinter.CTkLabel(self, image=self.add, text='').place(relx=0.03, rely=0.45)

        self.buttonD = customtkinter.CTkButton(self, text="Remover usuários", command=self.clickD, fg_color='#27C4B7', font=self.fonte14, corner_radius=30).place(relx=0.1, rely=0.59)
        self.trash = customtkinter.CTkImage(Image.open('img/trash.png'), size=(25,30))
        self.trash = customtkinter.CTkLabel(self, image=self.trash, text='').place(relx=0.03, rely=0.59)

        self.buttonF = customtkinter.CTkButton(self, text='Limpar mensagens', command=self.clickF, fg_color="#27C4B7", font = self.fonte14, corner_radius=30).place(relx=0.1, rely=0.73)
        self.clear = customtkinter.CTkImage(Image.open('img/clear.png'), size=(25,30))
        self.clear = customtkinter.CTkLabel(self, image=self.clear, text='').place(relx=0.03, rely=0.73)

        self.buttonE = customtkinter.CTkButton(self, text='Encerrar ChatBot',command=self.destroy, fg_color="red", font=self.fonte14, corner_radius=30).place(relx=0.1, rely=0.85)
        self.exit = customtkinter.CTkImage(Image.open('img/exit.png'), size=(25,30))
        self.exit = customtkinter.CTkLabel(self, image=self.exit, text='').place(relx=0.03, rely=0.85)

        #Textbox
        self.text = customtkinter.CTkTextbox(self, width=350, height=350, fg_color='transparent', border_width=3, border_color='#27C4B7')
        self.text.place(relx=0.4, rely=0.2)

    def clickA(self):
        msg = 'Você clicou em Pesquisa\n'
        self.text.insert('end', msg)

    def clickB(self):
        msg2 = "Você clicou em Lista dos usuários\n"
        self.text.insert('end', msg2)

    def clickC(self):
        msg3 = "Você clicou em Adicionar usuários\n"
        self.text.insert('end', msg3)

    def clickD(self):
        msg4 = "Você clicou em Remover usuários\n"
        self.text.insert('end', msg4)

    def clickF(self):
        self.text.delete('1.0')
        


app = ChatBot()
app.mainloop()
