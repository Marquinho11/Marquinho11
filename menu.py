import customtkinter

from Modulos.modulos import *
from Functions.abrir_arquivos import Arquivos




customtkinter.set_appearance_mode("blue")
customtkinter.set_default_color_theme("dark-blue")


# Classe original
class Screen_menu(Arquivos):
    def __init__(self) -> None:
        self.root_menu = customtkinter.CTk()
        self.conecta_banco()
        self.criando_tabela()
        self.config()
        self.create_frame()
        self.create_entry()
        self.create_bt()
        self.tree_view()
        self.select_lista()

        self.root_menu.mainloop()
    
    def config(self):
        self.root_menu.title('Menu')
        self.root_menu.config(bg="#CACFD2")
        self.root_menu.geometry('1280x780+400+100')
        self.root_menu.title('JRMADEIRAS')

    def create_frame(self):
        self.frame = Frame(self.root_menu, bg="green")
        self.frame.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=0.13)

    def create_entry(self):
        self.entry_codigo = customtkinter.CTkEntry(self.frame, placeholder_text="Scaneie o codigo")
        self.entry_codigo.place(relx=0.02, rely=0.10, relwidth=0.20)
        self.entry_codigo.bind("<KeyRelease-Return>", lambda event: self.buscar())

        self.IDS = customtkinter.CTkEntry(self.frame,placeholder_text='')
        self.entry_qtd = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_r = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_M = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_D = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_UN = customtkinter.CTkEntry(self.frame, placeholder_text="")
        v = ['GIR6156A', 'GIR5810A','GIR5651A','GIR6550A', 'GIR6211A','GIR6216A','15M6628A','15M6637A']
        self.chk =  customtkinter.CTkComboBox(self.frame, values=v)
        self.chk.place(relx=0.50, rely=0.10)




    def create_bt(self):
        self.verificar = customtkinter.CTkButton(self.frame, text="Buscar",width=100, font=('Roboto', 15), command=self.buscar)
        self.verificar.place(relx=0.24, rely=0.10)


        self.arq = customtkinter.CTkButton(self.frame, text="Arquivo", width=100, font=('Roboto', 15), command=self.add_dados)
        self.arq.place(relx=0.30, rely=0.10)

        self.exe = customtkinter.CTkButton(self.frame, text="Excel", width=100, font=('Roboto', 15), command=self.exporta_clientes)
        self.exe.place(relx=0.36, rely=0.10)

        self.exe = customtkinter.CTkButton(self.frame, text="Remover Banco", width=100, font=('Roboto', 15),
                                           command=self.deletando_banco
                                           )
        self.exe.place(relx=0.42, rely=0.10)










    def tree_view(self):

        self.list_cli = ttk.Treeview(self.root_menu, height=3,column=("col1", "col2", "col3", "col4", "col5", "col6","col7","col8","col9","col10","col11","col12","col13","col14","col15","col16", "col17", "col18",'col19'))

        self.list_cli.heading("#0", text="")
        self.list_cli.heading("#1", text="Código")
        self.list_cli.heading("#2", text="ID")
        self.list_cli.heading("#3", text="Complemento")
        self.list_cli.heading("#4", text="Largura")
        self.list_cli.heading("#5", text="Avulso")
        self.list_cli.heading("#6", text="Modelo")
        self.list_cli.heading("#7", text="Ambiente")
        self.list_cli.heading("#8", text="Id da Peça")
        self.list_cli.heading("#9", text="codigo 1")
        self.list_cli.heading("10", text="Descrição")
        self.list_cli.heading("#11", text="vazio 1")
        self.list_cli.heading("#12", text="vazio 2")
        self.list_cli.heading("#13", text="Cliente")
        self.list_cli.heading("#14", text="Identificação")
        self.list_cli.heading("#15", text="Vazio")
        self.list_cli.heading("#16", text="Mod")
        self.list_cli.heading("#17", text="Codigo de Barras")
        self.list_cli.heading("#18", text="Espessura")
        self.list_cli.heading("#19", text="Status")



        self.list_cli.column("#0", width=0)
        self.list_cli.column("#1", width=10)
        self.list_cli.column("#2", width=40)
        self.list_cli.column("#3", width=20)
        self.list_cli.column("#4", width=10)
        self.list_cli.column("#5", width=50)
        self.list_cli.column("#6", width=50)
        self.list_cli.column("#7", width=20)
        self.list_cli.column("#8", width=50)
        self.list_cli.column("#9", width=20)
        self.list_cli.column("#10", width=20)
        self.list_cli.column("#11", width=50)
        self.list_cli.column("#12", width=50)
        self.list_cli.column("#13", width=50)
        self.list_cli.column("#14", width=50)
        self.list_cli.column("#15", width=50)
        self.list_cli.column("#16", width=50)
        self.list_cli.column("#17", width=50)
        self.list_cli.column("#18", width=40)
        self.list_cli.column("#19", width=50)



        self.list_cli.place(relx=0.00, rely=0.13, relwidth=0.99, relheight=0.999)


        self.scroolist = Scrollbar(self.root_menu, orient='vertical', command=self.list_cli.yview)
        self.list_cli.configure(yscroll=self.scroolist.set)
        self.scroolist.place(relx=0.99, rely=0.13, relwidth=0.01, relheight=0.88)
        self.list_cli.bind("<Double-1>", self.Ondoubleclick)





if __name__ == '__main__':
    root = Screen_menu()
