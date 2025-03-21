""" - una coordenada en dos dimensiones esta compuesta por dos valores el valor en el eje de las x y el valor en el eje y , esto podria ser una clase.un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices , esto podria ser una clase que esta comppuesta por 4 clases del objeto coordenada."""


# clase coordenad


def __init__(self, x , y):
        self.X = x
        self.Y = y


def mostrarcoordenada(self):
      def mostrarcoordenada(self):
        print("(", self.X, ",", self.Y, ")")

# clase cuadrado

class Cuadrado:
    # método constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.V1.mostrarcoordenada()
        self.V2.mostrarcoordenada()
        self.V3.mostrarcoordenada()
        self.V4.mostrarcoordenada()

# metodo principal

def main():
    
    X1 = int(input("dijite el valor de x:"))
    X2 = int(input("dijite el valor de y: "))


# processing 

c1 = coordenada(X1,X2)
c1.mostrarcoordenada()

v1 = coordenada(7,8)
v2 = coordenada(10,8)
v3 = coordenada(7,5)
v4 = coordenada(10,5)

cuadrado1 = cuadrado(v1 , v2 ,v3 , v4 )
cuadrado1.mostrarvertices()

if __name__ == "__main__":
    main()