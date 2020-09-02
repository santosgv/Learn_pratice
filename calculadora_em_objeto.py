from projetos.classes.calculadora import calculadora

def menu():
    print('''
          BEM VINDO A CALCULADORA EM OBJETO QUAL OPERAÇAOD DESEIJA REALIZAR ?
          1 -- SOMA
          2 -- MUTIPLICA
          3 -- DIVIDE
          4 -- SAI DO PROGRAMA
        ''')



a=calculadora('HP','vitor')

while True:
    menu()
    opc=int(input('Oque deseja ? '))
    if opc not in (1,2,3,4):
        print('Opçao invalida')

    elif opc == 1:
        a.soma(int(input('Qual o valor do primeiro numero ?')),int(input('Qual o valor do segundo numero ?')))

    elif opc == 2:
        a.mutiplica(int(input('Qual o valor do primeiro numero ?')),int(input('Qual o valor do segundo numero?')))

    elif opc == 3:
        a.divide(int(input('qual valor do primeiro numero')),int(input('Qual valor do segundo numero?')))

    elif opc == 4:
        break