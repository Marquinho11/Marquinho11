import csv
import os
import sqlite3
import time
from tkinter import filedialog, ttk
from tkinter import *
import pandas as pd
import openpyxl
from tkinter.messagebox import showinfo
from tkinter import messagebox

class Arquivos():
    def __init__(self):

        self.list_cli = None
        self.row = None

    def clear_screen(self):
        self.entry_codigo.delete(0, END)
        self.entry_qtd.delete(0, END)
        self.entry_r.delete(0, END)
        self.entry_M.delete(0, END)
        self.entry_D.delete(0, END)
        self.entry_UN.delete(0, END)


    def vars(self):
        self.cods = self.entry_codigo.get()
        self.com = self.chk.get()


        self.cd = self.IDS.get()
    def conecta_banco(self):
        self.conexao = sqlite3.connect('bancodeDados.db')
        self.cursor = self.conexao.cursor()


    def desliga_banco(self):
        self.conexao.close()

    def criando_tabela(self):
        self.conecta_banco()
        self.cursor.execute("""
                  CREATE TABLE IF NOT EXISTS contact(
                        ids INTEGER PRIMARY KEY,
                        id INTEGER(20),
                        complemento INTEGER(40),
                        largura INTEGER(40),
                        avulso TEXT,
                        modelo TEXT,
                        ambiente TEXT,
                        id_peça INTEGER(40),
                        codigo_barras TEXT,
                        id_de_peça TEXT,
                        vazio1 TEXT,
                        vazio2 TEXT,
                        cliente TEXT,
                        codigo_avulso TEXT,
                        vazio3 TEXT,
                        mod TEXT,
                        codigo_de_barras TEXT,
                        espessura TEXT,
                        identidade_da_peça TEXT,
                        status TEXT
                        
                      

                      );
                      """)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS state(codigo INTEGER,modulo TEXT, verificado)")

        self.conexao.commit()
        self.desliga_banco()



    def dialog(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    def add_dados(self):
        self.conecta_banco()
        self.dialog()
        csv_file = open(self.file_path, 'r')
        self.reader = csv.reader(csv_file, delimiter=';')
        next(self.reader)  # Pule o cabeçalho se houver um


        for self.row in self.reader:

            self.cod = self.row[0]
            self.comple = self.row[1]
            self.largura = self.row[2]
            self.avulso = self.row[3]
            self.modelo = self.row[4]
            self.ambi = self.row[5]
            self.id_peca = self.row[6]
            self.codigo_barras = self.row[7]
            self.id_dePeca = self.row[8]
            self.vazio1 = self.row[9]
            self.vazio2 = self.row[10]
            self.cliente = self.row[11]
            self.codigoavulso = self.row[12]
            self.vazio3 = self.row[13]
            self.mod = self.row[14]
            self.codigoDeBarras = self.row[15]
            self.espessura = self.row[16]
            self.identidadeDaPeça = self.row[17]



            self.cursor.execute("INSERT INTO contact(id, complemento,largura,avulso,modelo,ambiente,id_peça,codigo_barras,id_de_peça,vazio1,vazio2,cliente,codigo_avulso,vazio3,mod,codigo_de_barras,espessura,identidade_da_peça) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                   (self.cod, self.comple, self.largura, self.avulso, self.modelo, self.ambi, self.id_peca, self.codigo_barras, self.id_dePeca, self.vazio1, self.vazio2,
                                        self.cliente, self.codigoavulso,self.vazio3, self.mod, self.codigoDeBarras, self.espessura, self.identidadeDaPeça))
        showinfo(title='Successo', message='Importado com Successo')



        self.conexao.commit()
        self.conexao.close()
        self.select_lista()





    def select_lista(self):
        self.list_cli.delete(*self.list_cli.get_children())

        self.conecta_banco()
        self.listando = self.cursor.execute("SELECT ids,id, complemento,largura,avulso,modelo,ambiente,id_peça,codigo_barras,id_de_peça,vazio1,vazio2,cliente,codigo_avulso,vazio3,mod,codigo_de_barras,espessura,identidade_da_peça, status FROM contact ORDER BY id ASC;")
        for i in self.listando:
            self.list_cli.insert("", END, values=i)


        self.desliga_banco()

    def Ondoubleclick(self, event):

        self.clear_screen()
        self.list_cli.selection()

        for n in self.list_cli.selection():
            col1, col2, col3, col4, col5, col6= self.list_cli.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_qtd.insert(END, col2)
            self.entry_r.insert(END, col3)
            self.entry_M.insert(END, col4)
            self.entry_D.insert(END, col5)
            self.entry_UN.insert(END, col6)



    def delete(self):

        self.vars()
        #print(self.cods)
        self.conecta_banco()
        self.cursor.execute("SELECT ids,identidade_da_peça FROM contact WHERE codigo_de_barras=?",(self.cods,))
        result = self.cursor.fetchone()

        r = self.cursor.execute("SELECT codigo_de_barras,identidade_da_peça FROM contact WHERE codigo_de_barras=?", (self.cods,))
        s = r.fetchone()
        print("aqui", s[0], s[1])

        self.cursor.execute("INSERT INTO state(codigo, modulo, verificado) VALUES (?,?, 'ok')", (s[0], s[1]))

        rs = self.cursor.execute("SELECT  codigo, modulo FROM state")
        sd = rs.fetchall()
        print(sd)


        if result:

            record = result[0]
            time.sleep(1)
            self.cursor.execute("DELETE FROM contact WHERE ids=?",(record,))
            #showinfo(title='Deletado', message='Deletado com sucesso!!!')

            self.conexao.commit()
            self.conexao.close()


        else:
            #showinfo(title='Falha', message='Nenhum codigo encontrado!!!')
            pass



        self.conexao.close()
        self.clear_screen()
        #return self.delete



    def exporta_clientes(self):
        self.conecta_banco()
        # Inserir dados na tabela:
        self.cursor.execute("SELECT * FROM state")
        clientes_cadastrados = self.cursor.fetchall()
        clientes_cadastrados = pd.DataFrame(clientes_cadastrados,
                                                columns=['codigo', 'modulo', 'verificado'])
        clientes_cadastrados.to_excel('Documento/Relatorio.xlsx')


            # Commit as mudanças:
        self.conexao.commit()

            # Fechar o banco de dados:
        self.conexao.close()

    def buscar(self):
        self.conecta_banco()
        self.vars()
        self.list_cli.delete(*self.list_cli.get_children())
        self.entry_codigo.insert(END,"" )
        self.names = self.entry_codigo.get()

        self.cursor.execute("SELECT ids,id, complemento,largura,avulso,modelo,ambiente,id_peça,codigo_barras,id_de_peça,vazio1,vazio2,cliente,codigo_avulso,vazio3,mod,codigo_de_barras,espessura,identidade_da_peça FROM contact WHERE codigo_de_barras  LIKE '%s' ORDER BY codigo_de_barras ASC " % self.names)
        self.buscadordeCliente = self.cursor.fetchall()

        for i in self.buscadordeCliente:
            self.list_cli.insert("", END, values=i)

        self.conexao.close()
        self.delete()
        self.select_lista()

        return self.buscar


    def deletando_banco(self):
        teste = 'bancodeDados.db'
        if os.path.exists(teste):
            os.remove(teste)
            showinfo(title='Banco', message='Deletado e Pronto para novo arquivo, reinecie para adicionar o novo arquivo')









