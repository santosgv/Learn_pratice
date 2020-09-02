
# coding: utf-8

# In[ ]:


def calculate():
    operation = input('''
Por favor escolha um tipo de operaçao matematica que deseja completar:
+ para adiçao
- para subtraçao
* para multiplicaçao
/ para divisao
''')

    number_1 = int(input('Porfavor digite o primeiro numero: '))
    number_2 = int(input('Porfavor digite o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Voce nao selecionou um operador valido, tente rodar o programa novamente.')

    # Adicionado a funçao again() para a funçao calculate().
    again()

def again():
    calc_again = input('''
voce gostaria de realizar outra operaçao?
precione Y para sim ou N para nao.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ate breve !!!.')
    else:
        again()

calculate()