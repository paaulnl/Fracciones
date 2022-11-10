## realizar la clase

class Fraction():
    numerator=0
    denominator=0

    #realizar los constructores
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    ## realiizar los metodos a utilizar
    def multiplication(self,other):
        numerator = (self.numerator * other.numerator)
        denominator = (self.denominator * other.denominator)
        print("El resultado de la multiplicacion es : ",numerator,"/",denominator)
    def division(self,other):       
        numerator = (self.numerator     /    other.numerator)
        denominator = (self.denominator /   other.denominator)
        print("El resultado de esta division es :",numerator,"/",denominator)
    def addition  (slf,other):
        if (other.denominator == self.denominator):
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            denominator = self.denominator
            print("El resultado de la suma es:",numerator,"/",denominator)
        else:
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator )  
            denominator = (self.denominator * other.denominator)
            print ("El resultado de la suma es  : ",numerator ,"/",denominator)    
    def subtracion(self,other):
        if(self.denominator == other.denominator):
            numerator = (self.numerator * other.denominator) - (other.numerator - self.numerator)
            denominator = self.denominator
            print("El resultado de la resta es :".numerator ,"/",denominator)
        else:
            numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator )  
            denominator = (self.denominator * other.denominator)         
            print ("El resultado de la resta es  : ",numerator ,"/",denominator)
    ##INICIALIZAR VARIABLES 
    numerator_i = 0
    denominator_i = 1  ## no pueden ser 0 
    numerator_ii = 0
    denominator_ii = 1 ## no peude ser 0 
    Fraction_A = 0
    Fraction_B = 0

    # INPUTS PARA QUE INGRESEN LOS VALORES
    numerator_i = int(input("Ingrese el valor de el numerador de la primera fraccion:"))
    denominator_i = int(input("Ingrese el valor del denominador de la primera fraccion:"))
    print(numerator_i,"/",denominator_i)
    
    
    numerator_ii = int(input("Ingrese el valor del numerador de la segunda fraccion"))
    denominator_ii = int(input("Ingrese el valor del denominador de la segunda fraccion:"))
    print(numerator_ii,"/",denominator_ii)
    
    #ARMAS LAS FRACCIONES
    Fraction_A = Fraction(numerator_i,denominator_i)
    Fraction_B = Fraction(numerator_ii,denominator_ii)
    #MENU DE OPCIONES QUE MUESTRE LAS OPERACIONES
    operation = input ("Ingrese la operacion que desee realizar con las fracciones: + , - , x y dv")
    if (operation == "+"):
        Fraction_A.addition(Fraction_B)
    elif(operation == "-"):
        Fraction_A.subtracion(Fraction_B)
    elif(operation == "x"):
        Fraction_A.multiplication(Fraction_B)
    elif(operation == "dv"):
        Fraction_A.division(Fraction_B)
    else:
        print("Los valores que ingresaste no son validos.")
