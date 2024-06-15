import tkinter, customtkinter, os, webbrowser, subprocess
from PIL import Image, ImageTk 
from tkinter import font  
from time import strftime

customtkinter.set_default_color_theme("files/theme.json")

def reconhecimento():
    os.system('camera.py')

def chatbot():
    os.system('chatbot.py')

def solicitacaoPDF():
    os.system('files\\solicitacao.pdf')

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master ,**kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Inicio")
        self.add('Solicitação')
        self.add("Sobre")
        self.add('Desenvolvedores')
        self.fonteMax = customtkinter.CTkFont(family='Poppins', size=25, weight='bold')
        self.fonte = customtkinter.CTkFont(family='Poppins', size=16, weight = 'bold')
        self.fonte14 = customtkinter.CTkFont(family='Poppins', size=14, weight = 'bold')

        #Backgrounds
        self.backgroundInicio = customtkinter.CTkImage(Image.open('img/BackgroundImage.png'), size=(1000,500))
        self.backgroundInicio = customtkinter.CTkLabel(master=self.tab('Inicio'), image=self.backgroundInicio, text='').place(relx=0.0001, rely=0.001)
        self.backgroundSolicitacao = customtkinter.CTkImage(Image.open('img/BackgroundImage.png'), size=(1000,500))
        self.backgroundSolicitacao = customtkinter.CTkLabel(master=self.tab('Solicitação'), image=self.backgroundSolicitacao, text='').place(relx=0.0001, rely=0.001)
        self.backgroundSobre = customtkinter.CTkImage(Image.open('img/BackgroundImage.png'), size=(1000,500))
        self.backgroundSobre = customtkinter.CTkLabel(master=self.tab('Sobre'), image=self.backgroundSobre, text='').place(relx=0.0001, rely=0.001)
        self.backgroundDevs = customtkinter.CTkImage(Image.open('img/BackgroundImage.png'), size=(1000,500))
        self.backgroundDevs = customtkinter.CTkLabel(master=self.tab('Desenvolvedores'), image=self.backgroundDevs, text='').place(relx=0.0001, rely=0.001)

        #Logo
        self.logo = customtkinter.CTkImage(Image.open("img/IASecurityVisionPNGVersion-250.png"), size=(200,200))
        self.logo_label = customtkinter.CTkLabel(master=self.tab('Inicio'), image=self.logo, text='', fg_color='#161c2e', bg_color="#161c2e").place(relx=0.2, rely=0.01)

        #Relógio digital
        def update_time():
            horario = strftime('%H:%M:%S %p')
            self.relogio_lbl.configure(text=horario)
            self.relogio_lbl.after(1000, update_time)

        self.relogio_lbl = customtkinter.CTkLabel(master=self.tab('Inicio'), font=self.fonteMax, text_color="#27C4B7", bg_color='#161c2e')
        self.relogio_lbl.place(relx=0.5, rely=0.23)
        update_time()
        #Textos
        self.iasv = customtkinter.CTkLabel(master=self.tab("Inicio"), text='I.A. Security Vision. O reconhecimento facial a seu favor!'
            , text_color="#27C4B7",fg_color='#161c2e', width=80, height=80, font= self.fonte)
        self.iasv.place(relx = 0.22, rely=0.4)

        #Funcoes do app
        self.camera = customtkinter.CTkImage(Image.open('img/Teste.png'), size=(70,70))
        self.camera = customtkinter.CTkButton(master=self.tab('Inicio'), text='', image=self.camera, bg_color='#161c2e', fg_color='#161c2e', width=1, command=reconhecimento).place(relx=0.35, rely=0.6)

        self.chat = customtkinter.CTkImage(Image.open('img/chat.png'), size=(70,70))
        self.chat = customtkinter.CTkButton(master=self.tab('Inicio'), text='', image=self.chat, bg_color='#161c2e', fg_color='#161c2e', width=1, command=chatbot).place(relx=0.52, rely=0.61)

        self.ano = customtkinter.CTkLabel(master= self, text='2024', text_color='#27C4B7',fg_color="#161c2e", font=self.fonte).place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        #Solocitacao
        self.pdf = customtkinter.CTkImage(Image.open('img/pdf.png'), size=(80, 80))
        self.pdf = customtkinter.CTkLabel(master= self.tab('Solicitação'), image = self.pdf, text='', fg_color='#161c2e', bg_color='#161c2e').place(relx=0.45, rely=0.2)
        self.solicitar = customtkinter.CTkLabel(master=self.tab('Solicitação'), text='Clique no botão abaixo para acessar o documento de autorização do uso de imagem', 
            font = self.fonte14, text_color="#27C4B7",fg_color='#161c2e', width=80, height=80).place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        self.solicitacao = customtkinter.CTkButton(master=self.tab('Solicitação'), text="Solcitação", fg_color='#27C4B7', width=80, command=solicitacaoPDF, corner_radius=30).place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        #Uso
        #self.uso = customtkinter.CTkButton(master=self.tab('Solicitação'), text='Guia de uso', width=80, bg_color = '#161c2e', fg_color='#27C4B7', corner_radius=30).place(relx=0.55, rely=0.463)
        
        self.email = customtkinter.CTkImage(Image.open('img/email.png'), size=(50, 50))
        self.email = customtkinter.CTkLabel(master=self.tab('Solicitação'), image = self.email, text='', fg_color='#161c2e', bg_color='#161c2e').place(relx=0.47, rely=0.58)
        self.ajuda = customtkinter.CTkLabel(master=self.tab('Solicitação'), text='Em caso de problemas, envie um e-mail para: \nhenriquemarquessantossilva@hotmail.com', text_color="#27C4B7", 
            width=80, height=80, font=self.fonte14, fg_color='#161c2e').place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        #Sobre
        self.sobre = customtkinter.CTkLabel(master=self.tab('Sobre'), font=self.fonte14, text_color='#27C4B7',fg_color='#161c2e', 
            text='O aplicativo de reconhecimento facial I.A. Security Vision foi feito para auxiliar os usuários \nque vivem em apartamentos e condomínios, incluindo um chatbot de \n interação que pode auxilia-los. Sua finalidade é aumentar a segurança com uso \ndo reconhecimento facial dos indivíduos \ncadastrados com uso de imagens.').place(relx = 0.06, rely=0.55)
        self.imgSobre = customtkinter.CTkImage(Image.open('img/reconhecimento.png'), size=(150,150))
        self.imgSobre = customtkinter.CTkLabel(master=self.tab('Sobre'), image=self.imgSobre, text='', fg_color='#161c2e', bg_color='#161c2e').place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        #Desenvolvedores
        self.devs =  customtkinter.CTkLabel(master = self.tab('Desenvolvedores'), font=self.fonteMax, 
            text_color='#27C4B7', text='Desenvolvedores', 
            fg_color='#161c2e').place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.devsInfo = customtkinter.CTkLabel(master=self.tab('Desenvolvedores'), font=self.fonte14, 
            text_color='#27C4B7', 
            text='Alex Plínio Ribeiro Alves, Caio Guilherme Lopes Alves, Carina Gonçalves Farias,\n Henrique Marques Santos Silva e Jennifer Cristine Farias Alves: ', fg_color="#161c2e").place(relx=0.1, rely=0.2)

        self.instituicao = customtkinter.CTkLabel(master=self.tab('Desenvolvedores'), 
            text='Instituição na qual foi desenvolvido o aplicativo: ', text_color='#27C4B7', 
            font=self.fonte14, fg_color='#161c2e').place(relx=0.1, rely=0.5)

        self.etecsm = customtkinter.CTkImage(Image.open('img/etecsm2.png'), size=(150,100))
        self.etecsm = customtkinter.CTkLabel(master=self.tab('Desenvolvedores'), image=self.etecsm, text='', 
            fg_color='#161c2e', bg_color='#161c2e').place(relx=0.6, rely=0.4)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        self.tab_view.configure(width = 750, height = 430, fg_color='#161c2e')
        self.geometry("800x480")
        self.title('I.A. Security Vision')
        self.resizable(False, False)

        #Icon
        self.iconbitmap('img\\icon.ico')

app = App()
app.mainloop()
