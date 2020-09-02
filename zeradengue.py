import sqlite3
conn= sqlite3.connect("senhas.db")
cursor= conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS OCORRENCIAS (
BAIRRO TEXT NOT NULL,
RUA text not null,
NUMERO interger not null,
SITUACAO interger not null
);
''')

def menu():
    print('''
                **** Bem Vindo ao Zer@Dengue ****
                ****                         ****
                ** 1 - Realizar denuncia :   ****
                ** 2 - Acompanhar status :   ****
                ** 3 - Realizar auditoria:   ****
                ** 4 - Sair do programa  :   ****
    ''')


def denuncia(BAIRRO,RUA,NUMERO,SITUACAO):
        cursor.execute(f'''
        insert into OCORRENCIAS(BAIRRO,RUA,NUMERO,SITUACAO)
        values ('{BAIRRO}','{RUA}','{NUMERO}','{SITUACAO}')
    ''')
        conn.commit()



def acompanha(): ##RUA,NUMERO
    cursor.execute(f'''
    SELECT * FROM OCORRENCIAS WHERE SITUACAO = 1
''') ##AND RUA LIKE ('%{RUA}%') AND ('%{NUMERO}%')
    for x in cursor.fetchall():
        print(x)


def audita():
    cursor.execute(f'''
    UPDATE OCORRENCIAS SET SITUACAO=2''')
    conn.commit()

while True:
    menu()
    opc=int(input('Qual Opçao ? : '))
    if opc not in (1,2,3,4):
        print('Opçao invalida')
        continue
    elif opc ==1:
        BAIRRO=str(input('Qual Bairro ? '))
        RUA=str(input('Qual rua? '))
        NUMERO=int(input('Qual numero ? '))
        SITUACAO=1
        denuncia(BAIRRO,RUA,NUMERO,SITUACAO)

    elif opc ==2:
        #r=str(input('Qual a rua ?'))
        #n=int(input('Qual o numero da rua ?'))
        acompanha()

    elif opc ==3:
        rua=str(input('QUal Rua a ser auditada ?'))
        num=int(input('Qual numero a ser auditado ?'))
        audita()
    elif opc ==4:
        break
conn.close()