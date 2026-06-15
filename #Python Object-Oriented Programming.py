# Python Object-Oriented Programming (Programación Orientada a Objetos)

# Definimos una clase llamada Employee.
# Una clase es un "molde" a partir del cual se crean objetos.
class Employee:

    # Variable de clase.
    """
    Variables de clase: Son compartidas por todas las instancias (objetos) de esa clase. 
    Si cambias su valor en la clase, el cambio se refleja en todos los objetos que no tengan su propia versión de esa variable. 
    Se definen directamente dentro de la clase, fuera de cualquier método.
    """
    # Es compartida por TODOS los empleados.
    # Se utiliza para contar cuántos empleados se han creado.
    num_of_emps = 0

    # Variable de clase.
    # Representa un aumento salarial del 4%.
    # Todos los empleados tendrán acceso a esta variable.
    raise_amt = 1.04

    # Constructor.
    # Se ejecuta automáticamente cada vez que se crea un nuevo Employee.
    #
    # self representa la instancia actual (el objeto que se está creando).
    #
    # first = nombre
    # last = apellido
    # pay = salario
    def __init__(self, first, last, pay):#metodo inicializador o constructor con los atributos de instancia que se le pasan al crear un nuevo objeto Employee
 
        # Variables de instancia.
        """
        Variables de instancia: Son únicas para cada objeto. 
        Cada instancia tiene su propia copia independiente. 
        Se definen usualmente dentro del método
        """
        # Cada empleado tendrá sus propios valores.
        self.first = first
        self.last = last

        # Construimos automáticamente un email.
        self.email = first + '.' + last + '@company.com'

        # Guardamos el salario.nada     
        self.pay = pay

        # Incrementamos el contador de empleados.
        # Como pertenece a la clase, accedemos mediante Employee.
        Employee.num_of_emps += 1

    # Método de instancia.
    # Devuelve el nombre completo del empleado.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Método que aplica un aumento salarial.
    def apply_raise(self):

        # Multiplica el salario por raise_amount.
        #
        # Ejemplo:
        # 50000 * 1.04 = 52000
        #
        # int() elimina posibles decimales.
        self.pay = int(self.pay * self.raise_amount)
    

    @classmethod # Decorador que indica que este método es un método de clase.
    def set_raise_amt(cls, amount): # El primer argumento es cls, que representa la clase en sí (similar a self para instancias).#Este método se puede llamar tanto desde la clase como desde una instancia.
        cls.raise_amt = amount 
    
    @classmethod
    def from_string(cls, emp_str): # Método de clase que toma una cadena con formato
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day): # Método estático que no depende de la clase ni de la instancia. Se puede llamar desde la clase o desde una instancia.
        if day.weekday() == 5 or day.weekday() == 6: # Si el día es sábado (5) o domingo (6)
            return False
        return True

# Antes de crear empleados el contador vale 0.
print(Employee.num_of_emps)


# Creamos el primer objeto Employee.
#
# Python ejecuta internamente:
# Employee.__init__(emp_1, 'Corey', 'Schafer', 50000)
#
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2= Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2024, 6, 1)
print(Employee.is_workday(my_date)) # Llamada al método estático desde la clase.

# Creamos el segundo objeto Employee.
emp_2 = Employee('Test', 'User', 60000)




# Ahora el contador vale 2 porque creamos dos empleados.
print(Employee.num_of_emps)


# __dict__ muestra todos los atributos almacenados
# dentro de una instancia.
#
# Resultado esperado:
#
# {
#     'first': 'Corey',
#     'last': 'Schafer',
#     'email': 'Corey.Schafer@company.com',
#     'pay': 50000
# }
#

emp_1.set_raise_amt(1.05) # Cambiamos el aumento salarial a 5% utilizando el método de clase.

print(Employee.raise_amt) # Accedemos a la variable de clase a través de la clase Employee.
print(emp_1.raise_amt) # Accedemos a la variable de clase a través de la instancia emp_1.
print(emp_2.raise_amt) # Accedemos a la variable de clase a través de la instancia emp_2.

# Muestra los atributos del segundo empleado.
print(emp_2.__dict__)


# Variable de clase accesible desde la clase.
# print(Employee.raise_amount)

# Variable de clase accesible desde una instancia.
# Python primero busca dentro de la instancia.
# Si no la encuentra, busca en la clase.
# print(emp_1.raise_amount)
 
# print(emp_2.raise_amount)


# Llamada normal al método.
#
# Python transforma:
#
# emp_1.fullname()
#
# en:
#
# Employee.fullname(emp_1)
#
emp_1.fullname()


# Llamada explícita al método de la clase.
#
# Pasamos manualmente emp_1 como argumento self.
#
print(Employee.fullname(emp_1))


# Lo mismo para el segundo empleado.
emp_2.fullname()

print(Employee.fullname(emp_2))


# Imprimir la referencia del objeto.
# Como no existe un método __str__ o __repr__,
# Python mostraría algo parecido a:
#
# <__main__.Employee object at 0x000001F34A8B6C40>
#
# print(emp_1)
# print(emp_2)


# Estas líneas están comentadas porque ya se ejecutan
# automáticamente dentro del constructor __init__.
#
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000


# Imprime el email generado automáticamente.
#
# print(emp_1.email)
# print(emp_2.email)


# Imprime el nombre y apellido utilizando format().
#
# Resultado:
# Corey Schafer
#
# print('{} {}'.format(emp_1.first, emp_1.last))




"""
Programación Orientada a Objetos en Python

Este código muestra los conceptos fundamentales de POO (Programación Orientada a Objetos) en Python: clases, objetos, atributos, métodos de instancia, métodos de clase y métodos estáticos.

1. Definición de la clase

Aquí definimos una clase llamada Employee.

¿Qué es una clase?

Una clase es un molde o plantilla para crear objetos.

Por ejemplo:

emp_1 y emp_2 son objetos (instancias) creados a partir de la clase Employee.

2. Variables de clase

Estas variables pertenecen a la clase, no a un objeto individual.

num_of_emps

Cuenta cuántos empleados se han creado.

Se comparte entre todas las instancias.

raise_amt

Representa un aumento salarial del 4%.

1.04 significa:

1 = 100% del salario original

0.04 = 4% extra

Diferencia importante

Variables de clase → compartidas por todos los objetos.

Variables de instancia → cada objeto tiene su propia copia.

3. Constructor __init__

Este es el constructor.

Se ejecuta automáticamente cuando se crea un nuevo objeto.

Parámetros

self → representa la instancia actual del objeto.

first → nombre del empleado.

last → apellido.

pay → salario.

Dentro del constructor

Aquí se crean atributos de instancia.

Cada empleado tendrá sus propios valores:

first
last
email
pay
Ejemplo

Para:

los atributos quedan así:

4. Incrementar el contador de empleados

Cada vez que se crea un nuevo empleado:

0 → 1

1 → 2

2 → 3

Se accede mediante Employee porque num_of_emps es una variable de clase.

5. Método de instancia fullname

Este método devuelve el nombre completo del empleado.

Ejemplo

devuelve:

Importante

Los métodos de instancia siempre reciben self como primer argumento.

Python automáticamente pasa la instancia actual.

6. Método de instancia apply_raise

Aplica un aumento salarial al empleado.

Paso a paso

Si:

Entonces:

int() convierte el resultado a entero.

Resultado

El salario del empleado queda actualizado.

7. Método de clase set_raise_amt

Este es un método de clase.

¿Qué significa @classmethod?

El decorador @classmethod indica que el método recibe la clase como primer argumento en lugar de una instancia.

cls representa la clase Employee.

¿Para qué sirve?

Permite modificar datos compartidos por toda la clase.

Ejemplo

Internamente Python hace algo similar a:

Y ahora:

Todos los empleados verán el nuevo valor.

8. Método de clase alternativo from_string

Este método permite crear empleados a partir de una cadena de texto.

Ejemplo
Qué ocurre

split('-') divide la cadena.

Se obtienen first, last y pay.

return cls(...) crea y devuelve un nuevo objeto Employee.

Ventaja

Es una forma alternativa y limpia de crear objetos.

9. Método estático is_workday

Este es un método estático.

¿Qué significa @staticmethod?

El método:

no recibe self

no recibe cls

no depende ni de la instancia ni de la clase

Es simplemente una función relacionada lógicamente con la clase.

Qué hace

Determina si un día es laborable.

weekday() devuelve un número:

0 = lunes

1 = martes

...

5 = sábado

6 = domingo

Si el día es sábado o domingo, devuelve False.

Ejemplo

2024-06-01 es sábado, por lo tanto imprime:

10. Creación de objetos y contador

Antes de crear empleados:

Luego:

Ahora el contador vale:

porque el constructor incrementó num_of_emps dos veces.

11. __dict__

__dict__ muestra todos los atributos almacenados en la instancia.

Resultado:

Es útil para depuración y para entender qué datos contiene el objeto.

12. Acceso a variables de clase

Todas imprimen el mismo valor.

¿Por qué?

Cuando accedes desde una instancia:

Python busca:

Primero en la instancia emp_1

Si no lo encuentra, busca en la clase Employee

Como raise_amt está en la clase, las instancias lo heredan.

13. Llamada a métodos

Python internamente lo transforma en:

Por eso también funciona:

emp_1 se pasa manualmente como argumento self.

14. Conceptos clave que enseña este código
Clase

El molde:

Instancia/Objeto

Los objetos creados:

Atributos de instancia

Datos propios de cada empleado:

first
last
email
pay
Atributos de clase

Datos compartidos:

num_of_emps
raise_amt
Métodos de instancia

Trabajan con datos del objeto:

fullname
apply_raise
Métodos de clase

Trabajan con la clase:

set_raise_amt
from_string
Métodos estáticos

Funciones relacionadas con la clase pero independientes:

is_workday
15. Relación con Django

Todo esto es fundamental para Django porque:

Un modelo Django es una clase.

Los registros de la base de datos son instancias de esa clase.

Los métodos de modelo funcionan igual que fullname o apply_raise.

Los managers y métodos de clase en Django usan los mismos conceptos de @classmethod.

Por ejemplo:

Es exactamente la misma idea de orientación a objetos que aprendiste con Employee.
"""