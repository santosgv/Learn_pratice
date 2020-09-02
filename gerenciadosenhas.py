import sqlite3

app_senha="senha123@"

senha=input("Insira a senha: ")
if senha !=senha:
    print("senha invalida ! encerrando...")
    exit()

conn= sqlite3.connect("senhas.db")

cursor= conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
servico text not null,
usuario text not null,
senha interger not null
);
''')



def menu():
    print("********************************")
    print("* i : inserir uma nova senha  *")
    print("* l : listar todos os serviços salvos")
    print("* r : recuperar um senha **")
    print("* s : sair do programa **")
    print("*********************************")

def get_password(services):
    cursor.execute(f'''
    select usuario, senha 
    from users 
    where servico ='{services}'
''')

    if cursor.rowcount ==0:
        print(" Nao foi cadastrado nem uma senha (use l para listar todas as senhas) ")
    else:
        for i in cursor.fetchall():
            print(i)

def insert_password(servicoes,loginn,senhaa):
    cursor.execute(f'''
    insert into users(servico,usuario,senha)
    values ('{servicoes}','{loginn}','{senhaa}')
''')
    conn.commit()

def show_passwords():
    cursor.execute('''
    select * from users;
    ''')
    for x in cursor.fetchall():
        print(x)

while True :
    menu()
    opc=input("O que deseja fazer ? :")
    if opc not in ['i','l','r','s']:
        print("Opcao invalida !")
        continue

    elif opc =='s':
        break

    elif  opc =='l':
        show_passwords()

    elif opc =='i':
        servicoes=input('Qual serviço deseja armazenar ? ')
        loginn=input('Qual o usuario ? ')
        senhaa=input('Qual a senha ? ')
        insert_password(servicoes,loginn,senhaa)

    elif opc =='r':
        servico=input('Qual servico voce quer recuperar a senha ? ')
        get_password(servico)

conn.close()
