

# clase coordenada

class Coordenada:
    # método constructor
    def __init__(self, x, y):
        # atributos privados
        self._X = x
        self._Y = y

    # método de lectura y escritura de cada atributo
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def setX(self, x):
        self._X = x

    def setY(self, y):
        self._y = y

    
    # metodo para mostrar coordenada
    def MostrarCoordenada(self):
        print("(", self._X, ",", self._Y, ")")

# clase cuadrado

class Cuadrado:
    # método constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4




# metodos privados para los vertices
def _mostrarcoordenadasV1(self):
    print("(" , self.__v1.getX()," ,", self.__v1.getY(),")")

def _mostrarcoordenadasV2(self):
    print("(" , self.__v2.getX()," ,", self.__v2.getY(),")")

def _mostrarcoordenadasV3(self):
    print("(" , self.__v3.getX()," ,", self.__v3.getY(),")")

def _mostrarcoordenadasV4(self):
    print("(" , self.__v4.getX()," ,", self.__v4.getY(),")")


  
  
    # metodo para mostrar los vertice
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.V1.MostrarCoordenada()
        self.V2.MostrarCoordenada()
        self.V3.MostrarCoordenada()
        self.V4.MostrarCoordenada()

# metodo principal
def main():
    # input
    x1 = int(input("dijite el valor de x: "))
    x2 = int(input("dijite el valor de y: "))

    c1 = Coordenada(x1,x2)
    c1.MostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)




# que ocurre si el metodo getx()lo hacemos: privado :__getx()?

if __name__ == "__main__":
    main()