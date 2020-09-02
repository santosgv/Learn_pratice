class calculadora:
    def __init__(self,MARCA,FABRICANTE):
        self.MARCA=MARCA
        self.FABRICANTE=FABRICANTE

    def show(self):
        print(self.MARCA,self.FABRICANTE)

    def soma(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        print(c)

    def mutiplica(self,a,b):
        self.a=a
        self.b=b
        c=a*b
        print(c)

    def divide(self,a,b):
        self.a=a
        self.b=b
        c=a/b
        print(c)
