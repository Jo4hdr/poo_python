# POO en python

- El paradigma de poo esta basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## Clase

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancia.
- La clase es la definicion del concepto del mundo real y los objetos o instancias son el objeto de el mundo real.
- Las clases estan compuestas con dos elementos: atributod y metodos

### Atributos 
- Informacion que almacena la clase

### Metodos

- Operaciones que pueden realizar las clases

## Definicion de una clase en Python
```Python
class NombreClase: 

    def _init_(self,variable1, variable2):
        self,Atributo1 = valor1
        self,Atributo2 = valor2

    def nombreMetodo(self):
         bloqueCodigo
```
### Componentes

```class```: palabra reservada en python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def``: palabra reservada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas en clase) como los diferentes metodos que tiene.

```_init_```: palabra reservada en python para definir el ,etodo constructor de la clase. Es lo primero que se ejecuta cuabdo creas un objeto de una clase. 

```(self, varableX)```: parametro del constructor de la clase. El parametro self es obligatorio y despues puedes tener cuantos parametros quieras. La forma de añadir parametros es la misma de las funciones.

```self.AtributoX```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: nombre del metodo de la clase.

```(self)```: parametro del metodo. El parametro self es oblogatorio, y despues puedes tener tantos parametroos como quieras. La forma de añadir parametros es la misma que en las funciones.

```bloqueCodigo```: instrucciones que ejecutara el metodo.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
    - Puedes definir tantos atributos como necesites.
    -Puedes definir tantos metodos como necesites.
    - Puedes definir tantos parametros cen el constructor y en los metodos como necesites.

## Composicion
- Consiste en la creacion de nuevas clases a partir de clase ya existentes que actuan como elementos copositores de la nueva.
- Las clases existentes seran atributos de la nueva clase.
- En POO la composision significa que entre las dos clases existe una relacion del tipo "tiene un".
- Ejemplo:
    - Una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, esto podria ser una clase. Un cuadrado esta compuesta por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada.