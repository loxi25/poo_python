# poo_python
intrduccion ala poo en python

- el paradigma de poo esta basado en una abstruccion del mundo real que nos va a permitir desarrolar programas de forma mas cercana a como vemos el mundo , pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos

## clase
- una clase es un tipo de dato cuyas variables se llaman objetos o instancias .
- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio objeto de mundo real.
- las clases estan compuestas por dos elementos atributos y metodos.

### atributos
- informacion que almacena la clase 

### metodos
- las operaciones que pueden realizar las clases


## definicion de una clase  en python
```python
class nombre clase:
  def__init_(self,variable1,variable2)
self.atributo1 = valor1
self.atributo2 = valor

def nombremetodo(self):
   bloquecodigo
```


### componentes

``class``: palabra reservada en python para definir una clase.

```nombreclase```: nombre de la clase que quieres crear.

```def```: palabra reservada en python que se utiliza para definir tato el constructor de la clase(metodo que se ejecuta la primera vez que usas una clase )como los diferentes metodos que tiene

```_init_```: palabra reservada en python para definir el metodo constructor de la clase. es el metodo que se ejecuta cuando creas un objeto de una clase . 

```(self, variable x)```: parametro del constructor de la clase el parametro self es obligatorio y despues puedes tener tantos parametro como quieras. la forma de añadir parametros es la misma que en las funciones.

```self.atributox```: forma de utilizacion y acceso a los atributos de la clase.

```nombremetodo```: nombre del metodo de la clase

```(self)```:parametros del metodo. el parametro self es obligatorioself es obligatorio y despues puedes tener tantos parametro como quieras. la forma de añadir parametros es la misma que en las funciones.

```bloquecodigo```: instrucciones que ejecutara el metodo

- cuando defines una clase deber tener en cuenta los siguientes puntos:
-  puedes definir tantos atributos como quieras
-  puedes definir tantos metodos como necesites 
- puedes definir tantos parametros en el constructor y en los metodos como necesites