from Modulos.modulos import *


from Functions.functions_cliente import Functions

class Screen_cadastro_cliente(Functions):

    def __init__(self):
        
        # self.root_cadastro_cliente = Tk()
        
        self.config()
        self.labels()
        self.insert_treeview()


        # self.root_cadastro_cliente.mainloop()
    
    def config(self):

        self.root_cadastro_cliente = Toplevel()
        self.root_cadastro_cliente.title('Cadastro de clientes')
        
        self.root_cadastro_cliente.resizable(False,False)
        self.root_cadastro_cliente.geometry('400x400+250+50')
        # self.root_cadastro_cliente.attributes('-fullscreen',True)

        self.root_cadastro_cliente.focus_force()
        self.root_cadastro_cliente.grab_set()


    
    def labels(self):

    # --------------------------- ID ---------------------------------
        self.txt_id = Label(self.root_cadastro_cliente,text='ID:')
        self.txt_id.place(relheight=0.05,relwidth=0.20, relx=0.03,rely=0.10)

        self.input_id = Entry(self.root_cadastro_cliente)
        self.input_id.place(relheight=0.05,relwidth=0.50, relx=0.25,rely=0.10)

        self.input_id.config(state='disabled')
    # --------------------------------------------------------------------

    # --------------------------- Nome ---------------------------------
        self.txt_nome = Label(self.root_cadastro_cliente,text='Nome:')
        self.txt_nome.place(relheight=0.05,relwidth=0.20, relx=0.03,rely=0.20)

        self.input_nome = Entry(self.root_cadastro_cliente)
        self.input_nome.place(relheight=0.05,relwidth=0.50, relx=0.25,rely=0.20)
    # --------------------------------------------------------------------
        
    # --------------------------- Endereço ---------------------------------
        self.txt_endereco = Label(self.root_cadastro_cliente,text='Descrição:')
        self.txt_endereco.place(relheight=0.05,relwidth=0.20, relx=0.03,rely=0.30)

        self.input_endereco = Entry(self.root_cadastro_cliente)
        self.input_endereco.place(relheight=0.05,relwidth=0.50, relx=0.25,rely=0.30)
    # -------------------------------------------------------------------------
    
    # --------------------------- Telefone -------------------------------------
        self.txt_telefone = Label(self.root_cadastro_cliente,text='Telefone:')
        self.txt_telefone.place(relheight=0.05,relwidth=0.20, relx=0.03,rely=0.40)

        self.input_telefone = Entry(self.root_cadastro_cliente)
        self.input_telefone.place(relheight=0.05,relwidth=0.50, relx=0.25,rely=0.40)
    # ---------------------------------------------------------------------------

    # --------------------------- button salvar ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Adicionar',command=self.salvar)
        self.button_adicionar.place(relheight=0.05,relwidth=0.20, relx=0.03,rely=0.50)
    # ---------------------------------------------------------------------------

    # --------------------------- button Editar ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Editar',font=self.font,background=self.collor_button,fg=self.font_color,command=self.editar)
        self.button_adicionar.place(relheight=0.05,relwidth=0.20, relx=0.25,rely=0.50)
    # ---------------------------------------------------------------------------

    # --------------------------- button Excluir ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Excluir',font=self.font,background=self.collor_button,fg=self.font_color,command=self.excluir)
        self.button_adicionar.place(relheight=0.05,relwidth=0.20, relx=0.47,rely=0.50)
    # ----------------------------------------------------------------------------

    # --------------------------- treeview ---------------------------------
        columns = ('id','nome','endereco','telefone')
        self.treeview_cliente = ttk.Treeview(self.root_cadastro_cliente,columns=columns,show='headings')

        self.treeview_cliente.heading('#1',text='id')
        self.treeview_cliente.heading('#2',text='Nome')
        self.treeview_cliente.heading('#3',text='Endereço')
        self.treeview_cliente.heading('#4',text='Telefone')

        self.treeview_cliente.column('#1',width=1)
        self.treeview_cliente.column('#2',width=20)
        self.treeview_cliente.column('#3',width=100)
        self.treeview_cliente.column('#4',width=20)

        self.listbar = Scrollbar(self.root_cadastro_cliente, orient='vertical')
        self.treeview_cliente.config(yscrollcommand=self.listbar)

        self.listbar.place(relheight=0.40,relwidth=0.04,relx=0.92,rely=0.56)
        self.treeview_cliente.place(relheight=0.40,relwidth=0.90,relx=0.03,rely=0.56)

        self.treeview_cliente.bind('<Double-1>',self.double_click)
    # ----------------------------------------------------------------------------






if __name__ == '__main__':
    root = Screen_cadastro_cliente()