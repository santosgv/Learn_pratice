import _sqlite3

con=_sqlite3.connect("myapp.db")
c=con.cursor()

senha_master='senha123@'

senha=input('Digite a senha do app ')
if senha != senha_master:
    print('senha invalida')
    exit()

c.execute('''
CREATE TABLE IF NOT EXISTS compras (
vendedor int
cliente int not null,
produto text not null,
quantidade int not null
);
''')

def opcoes():
    print('*************** Oque deseja fazer ? ************')
    print('comprar ? C :')
    print('ver seu pedido ? P :')
    print('quantidade de estoque ? E :')
    print('Deseja encerrar o programa ? S :')


def compra_insert(vendedor,cliente,produto,quantidade):
    c.execute(f'''
    insert into compras(vendedor,cliente,produto,quantidade)
    values ('{vendedor}','{cliente}','{produto}','{quantidade}')
''')
    con.commit()


def pedido_view():
    c.execute(f'''
    select * from compras
''')
    for x in c.fetchall():
        print(x)

def estoque_view():
    pass

while True:
    opcoes()
    opc=input('?')
    if opc =='s':
        exit()
    elif opc =='c':
        vendedor=input('Codigo do vendedor ? ')
        cliente=input('CPF do cliente ?')
        produto=input('Produto comprado ? ')
        quantidade=input('Quantidade ? ')
        compra_insert(vendedor,cliente,produto,quantidade)
    elif opc =='p':
        pedido_view()
    elif opc =='e':
        estoque_view()
    else:
        print('Opçao invalida')