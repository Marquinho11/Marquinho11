import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='dados_csv'
)
#para ligar o banco de dados
curso = conexao.cursor()

id_in = 1
complemento = 1673.0
largura = 70.0
fantasma = 601534
descricao = 'Painel'
modelo = 'Dormitorio'
cod = 3930
descricao_cod = 'pain15-34/3931'
codigo_barras = 'BASS733A'
passada = 0
passada_2 = 0
localidade = 'FERNANDO'
codigo_verdadeiro = 'LAT5833A'
un = 0
codigo_avulso = 5818
previa_ultima = 38305724
espesura = 18
codigo_rr = 'GIR5810A'









#para inserir dados dentro da tabela
commando = f'INSERT INTO csv_data(id_in,complemento,largura,fantasma,descricao,modelo,cod,descricao_cod,codigo_barras,passada,passada_2,localidade,codigo_verdadeiro,un, codigo_avulso, previa, ultima,ultima_one)' \
           f' VALUES("{id_in}","{complemento}","{largura}","{fantasma}","{descricao}","{modelo}","{cod}","{descricao_cod}","{codigo_barras}","{passada}","{passada_2}","{localidade}","{codigo_verdadeiro}"' \
           f',"{un}","{codigo_avulso}","{previa_ultima}","{espesura}","{codigo_rr}")'

curso.execute(commando)
conexao.commit()
#para encerrar o banco de dados
curso.close()
conexao.close()