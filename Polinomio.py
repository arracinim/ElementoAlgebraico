import sympy

class polinomio(object):
    def __init__(self,polinomio):
        self.polynomics = polinomio.lower()
        sympy.init_printing()
        self.x, self.y = sympy.symbols('x,y')

    def sumaPolinomios(self, polinomio):
        """
        Argumentos:
            - Polinomio: String

        Return: String con la suma de los polinomios
        """
        Poly1 = sympy.Poly(self.polynomics)
        Poly2 = sympy.Poly(polinomio.lower())

        return Poly1 + Poly2
        

    def restaPolinomios(self,polinomio):
        """
        Argumentos:
            - Polinomio: String
            
        Return: String con la resta de los polinomios
        """
        pass

    def multiplicarPolinomios(self,polinomio):
        """
        Argumentos:
            - Polinomio: String
            
        Return: String con la multiplicacion de los polinomios
        """
        pass

    def multEscalar(self,escalar):
        """
        Argumentos:
            - Escalar: String
            
        Return: String el polinomio original multiplicado por el escalar
        """
        pass

    def evaluarPolinomio(self,numero):
        """
        Argumentos:
            - Polinomio1: String
            - numero: String
            
        Return: Float con el resultado del polinomio evaluado sobre el numero entero
        """
        x = numero
        return eval(self.polynomics)


if __name__ == "__main__":
    polinomio = polinomio("X**3 + x**2 + x + 3")
    polinomio2 = "x**2"
    print("Suma de polinomios: ", polinomio.sumaPolinomios(polinomio2))
    print("Resta de polinomios: ", polinomio.restaPolinomios(polinomio2))
    print("multiplicacion de polinomios: ", polinomio.multiplicarPolinomios(polinomio2))
    print("multiplicacion por un escalar: ", polinomio.multiplicarPolinomios(polinomio2))
