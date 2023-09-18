from tkinter import *
from tkinter import ttk
import sqlite3





tela = Tk()

class Funcs():
    def clear_screen(self ):
        self.id.delete(0, END)
        self.frame_name.delete(0, END)
        self.frame_tele.delete(0, END)
        self.frame_email.delete(0, END)
        self.frame_rama.delete(0, END)
        self.frame_depart.delete(0, END)

    def conecta_db(self):
        self.conn = sqlite3.connect('contatos_cli.db')
        self.cursor = self.conn.cursor()

    def desconect_db(self):
        self.conn.close()

    def create_db(self):
        self.conecta_db(); print(" conectando ao banco de dados")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact(
            cod_cli INTEGER PRIMARY KEY ,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20) NOT NULL,
            email CHAR(40) NOT NULL,
            ramal INTEGER(20) NOT NULL,
            departamento CHAR(40)NOT NULL
            );
            """)

        self.conn.commit(), print("banco criado")
        self.desconect_db(), print("desconectou")
    def variavel(self):
        self.codigo = self.id.get()
        self.nome = self.frame_name.get()
        self.fone = self.frame_tele.get()
        self.email = self.frame_email.get()
        self.ramals = self.frame_rama.get()
        self.departa = self.frame_depart.get()
    def add_contatos(self):
        self.codigo = self.id.get()
        self.nome = self.frame_name.get()
        self.fone = self.frame_tele.get()
        self.email = self.frame_email.get()
        self.ramals = self.frame_rama.get()
        self.departa = self.frame_depart.get()
        self.conecta_db()
        self.cursor.execute("INSERT INTO contact(nome_cliente, telefone, email, ramal, departamento ) VALUES(?, ?, ?, ?, ?)", (self.nome, self.fone, self.email,self.ramals, self.departa))
        self.conn.commit()
        self.desconect_db()
        self.select_lista()
        self.clear_screen()

    def select_lista(self):
        self.list_cli.delete(*self.list_cli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("SELECT cod_cli, nome_cliente, telefone, email, ramal, departamento FROM contact ORDER BY nome_cliente ASC; ")
        for i in lista:
            self.list_cli.insert("", END, values=i)
        self.desconect_db()

    def Ondoubleclick(self, event):
        self.clear_screen()
        self.list_cli.selection()

        for n in self.list_cli.selection():
            col1,col2,col3,col4,col5,col6 = self.list_cli.item(n, 'values')
            self.id.insert(END, col1)
            self.frame_name.insert(END, col2)
            self.frame_tele.insert(END, col3)
            self.frame_email.insert(END, col4)
            self.frame_rama.insert(END, col5)
            self.frame_depart.insert(END, col6)


    def delete_client(self):
        self.variavel()
        self.conecta_db()
        self.cursor.execute("DELETE FROM contact WHERE cod_cli= ?", [self.codigo])
        self.conn.commit()
        self.desconect_db()
        self.clear_screen()
        self.select_lista()

    def alterar_client(self):
        self.variavel()
        self.conecta_db()
        self.cursor.execute("UPDATE contact SET nome_cliente = ?, telefone = ?, email = ?, ramal = ?, departamento = ? WHERE cod_cli = ?",(self.codigo,self.nome, self.fone, self.email, self.ramals, self.departa))
        self.conn.commit()
        self.desconect_db()
        self.select_lista()
        self.clear_screen()

    def buscar(self):
        self.conecta_db()
        self.list_cli.delete(*self.list_cli.get_children())
        self.frame_name.insert(END, '%')
        names = self.frame_name.get()
        self.cursor.execute("SELECT cod_cli, nome_cliente, telefone,email, ramal, departamento FROM contact WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC " % names)
        buscadordeCliente = self.cursor.fetchall()
        for i in buscadordeCliente:
            self.list_cli.insert("", END, values=i)
        self.clear_screen()
        self.desconect_db()


    def menu_bar(self):
        menubar = Menu(self.tela)
        self.tela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        def Quit(): self.tela.destroy()

        menubar.add_cascade(label= "Opções", menu=filemenu)
        menubar.add_cascade(label= "Sobre", menu= filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu2.add_command(label="Ligar")






class App(Funcs):
    def __init__(self):
        self.tela = tela
        self.config_window()
        self.create_label()
        self.create_frame()
        self.create_buttons()
        self.create_frame_data()
        self.tree_view()
        self.create_db()
        self.select_lista()
        self.menu_bar()
        tela.mainloop()


    def config_window(self):
        self.tela.title("Jrmadeiras Agenda")
        self.tela.geometry('800x500')
        self.tela.configure(bg='green')
        self.tela.maxsize(800, 500)
        self.tela.minsize(800,500)


    def create_label(self):
        self.name = Label(self.tela, text=" NOME: ", bg="green")
        self.name.place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.05)

        self.frame_phone = Label(self.tela, text=" TELEFONE: ", bg="green")
        self.frame_phone.place(relx=0.20, rely=0.01, relwidth=0.19, relheight=0.05)

        self.frame_email1 = Label(self.tela, text=" E-MAIL: ", bg="green")
        self.frame_email1.place(relx=0.40, rely=0.01, relwidth=0.15, relheight=0.05)

        self.frame_ramal = Label(self.tela, text=" RAMAL: ", bg="green")
        self.frame_ramal.place(relx=0.60, rely=0.01, relwidth=0.15, relheight=0.05)


        self.frame_DEPAR = Label(self.tela, text=" DEPARTAMENTO: ", bg="green")
        self.frame_DEPAR.place(relx=0.01, rely=0.10, relwidth=0.15, relheight=0.05)
    def create_frame(self):
        self.id = ttk.Entry(self.tela)
        self.id.place(relx=0.22, rely=0.15, relwidth=0.10, relheight=0.05)
        self.frame_name = ttk.Entry(self.tela)
        self.frame_name.place(relx=0.01, rely=0.05, relwidth=0.15, relheight=0.05)

        self.frame_tele = ttk.Entry(self.tela)
        self.frame_tele.place(relx=0.20, rely=0.05, relwidth=0.19, relheight=0.05)

        self.frame_email = ttk.Entry(self.tela)
        self.frame_email.place(relx=0.40, rely=0.05, relwidth=0.19, relheight=0.05)

        self.frame_rama = ttk.Entry(self.tela)
        self.frame_rama.place(relx=0.60, rely=0.05, relwidth=0.19, relheight=0.05)

        self.frame_depart = ttk.Entry(self.tela)
        self.frame_depart.place(relx=0.01, rely=0.15, relwidth=0.19, relheight=0.05)


    def create_buttons(self):
        self.save = ttk.Button(self.tela, text='Salvar', command=self.add_contatos)
        self.save.place(relx=0.80, rely=0.05, relwidth=0.15, relheight=0.05)

        self.clear = ttk.Button(self.tela, text='Limpar', command=self.clear_screen)
        self.clear.place(relx=0.80, rely=0.11, relwidth=0.15, relheight=0.05)

        self.get_user = ttk.Button(self.tela, text='Pesquisar', command=self.buscar)
        self.get_user.place(relx=0.80, rely=0.17, relwidth=0.15, relheight=0.05)

        self.get_delete = ttk.Button(self.tela, text='Apagar usuario', command=self.delete_client)
        self.get_delete.place(relx=0.80, rely=0.23, relwidth=0.15, relheight=0.05)

        self.get_alterar = ttk.Button(self.tela, text='Editar', command=self.alterar_client)
        self.get_alterar.place(relx=0.63, rely=0.11, relwidth=0.15, relheight=0.05)

    def create_frame_data(self):
        self.frame_data = ttk.Frame(self.tela)
        self.frame_data.place(relx=0.001, rely=0.30, relwidth=0.999, relheight=0.69)

    def tree_view(self):
        self.list_cli = ttk.Treeview(self.frame_data, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.list_cli.heading("#0", text="")
        self.list_cli.heading("#1", text="ID")
        self.list_cli.heading("#2", text="NOME")
        self.list_cli.heading("#3", text="TELEFONE")
        self.list_cli.heading("#4", text="EMAIL")
        self.list_cli.heading("#5", text="RAMAL")
        self.list_cli.heading("#6", text="DEPARTAMENTO")

        self.list_cli.column("#0", width=1)
        self.list_cli.column("#1", width=50)
        self.list_cli.column("#2", width=200)
        self.list_cli.column("#3", width=125)
        self.list_cli.column("#4", width=150)
        self.list_cli.column("#5", width=30)
        self.list_cli.column("#6", width=100)

        self.list_cli.place(relx=0.001, rely=0.001, relwidth=0.999, relheight=0.999)

        self.scroolist = Scrollbar(self.frame_data, orient='vertical')
        self.list_cli.configure(yscroll=self.scroolist.set)
        self.scroolist.place(relx=0.001, rely=0.01, relwidth=0.04, relheight=0.999)
        self.list_cli.bind("<Double-1>", self.Ondoubleclick)

App()