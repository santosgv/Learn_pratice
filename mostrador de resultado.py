
# coding: utf-8

# In[ ]:


materia = input('digite o nome da materia (portugues, matematica, fisica): ')
nota_final = input('digite sua nota (0 a 100): ')
semestre = input('digite o semestre (1 a 4): ')

if materia == 'portugues' and nota_final >= '60' and int(semestre) !=1:
    print('voce foi aprovado em %s com media final %r!' %(materia, nota_final))

elif materia == 'matematica' and nota_final >= '60' and int(semestre) !=1:
    print('voce foi aprovado em %s com media final %r!' %(materia, nota_final))

elif materia == 'fisica' and nota_final >= '60' and int(semestre) !=1:
    print('voce foi aprovado em %s com media final %r!' %(materia, nota_final))

else:
    print('voce precisa estudar mais!')

