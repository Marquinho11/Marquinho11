import customtkinter
from tkinter import *
from Functions.functions_login import Functions
from Modulos.modulos import *


customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("green")


        
        
janela = customtkinter.CTk()


class MyApp(Functions):
    def __init__(self):
        self.janela = janela
        self.create_databases()
        self.config_screen()
        self.images()
        self.create_label()
        self.janela.mainloop()
    
    def config_screen(self):
        self.janela.geometry('1000x600+400+100')
        self.janela.title('JRMADEIRAS')
        self.janela.configure(bg="green")
        self.janela.maxsize(1000,600)
        
#janela.resizable(False, False)
    def images(self):
        self.img = PhotoImage(file='img/j.png')
        self.frame1 = Frame(self.janela, bg="green")
        self.frame1.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=0. + 20)
        self.frame1 = Frame(self.janela, bg="green")
        self.frame1.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=0.+20)
        
        
    def create_label(self):
        self.labe_image = customtkinter.CTkLabel(self.frame1,text='',image=self.img)
        self.labe_image.place(relx=0.10, rely=0.008)

        self.frame = customtkinter.CTkFrame(self.janela, width=439, height=600)
        self.frame.place(relx=0.56, rely=0.00)

        self.labe = customtkinter.CTkLabel(self.frame, text="SCANNER", text_color='#008000',font=('Roboto',30,"bold"))
        self.labe.place(relx=0.28, rely=0.15)



        self.input_login = customtkinter.CTkEntry(self.frame, placeholder_text="Digite seu nome:", width=300)
        self.input_login.place(relx=0.12, rely=0.30)

        self.input_senha = customtkinter.CTkEntry(self.frame, placeholder_text="Digite sua senha:",show='*', width=300)
        self.input_senha.place(relx=0.12, rely=0.40)

        self.check = customtkinter.CTkCheckBox(self.frame, text="Lembrar-me da proxima vez")
        self.check.place(relx=0.12, rely=0.50)

        self.button = customtkinter.CTkButton(self.frame, text="Logar", width=150,  command=self.login)
        self.button.place(relx=0.08, rely=0.60)

        self.button_cadastrar = customtkinter.CTkButton(self.frame,text='Cadastrar',width=150, command=self.screen_cadastre_user)
        self.button_cadastrar.place(relx=0.58,rely=0.60)


        
if __name__ == '__main__':
        MyApp()