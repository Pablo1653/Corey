Programación Orientada a Objetos en Python

Este proyecto muestra los conceptos fundamentales e intermedios de Programación Orientada a Objetos (POO) en Python utilizando una estructura similar a la que se utiliza en frameworks profesionales como Django.

A lo largo del código se trabajan:

Clases
Objetos
Atributos de instancia
Atributos de clase
Métodos de instancia
Métodos de clase
Métodos estáticos
Herencia
Sobrescritura de atributos
Uso de super()
Relaciones entre objetos
isinstance()
issubclass()
1. Clase Employee

La clase Employee representa un empleado genérico.

Es la clase base del proyecto.

class Employee:

Todos los empleados tendrán:

Nombre
Apellido
Email
Salario
2. Variables de Clase

Las variables de clase son compartidas por todas las instancias.

num_of_emps = 0
raise_amt = 1.04
num_of_emps

Cuenta cuántos empleados fueron creados.

raise_amt

Representa un aumento salarial del 4%.

1.04

Significa:

100% del salario original
4% adicional
3. Constructor (init)

El constructor se ejecuta automáticamente cuando creamos un objeto.

def __init__(self, first, last, pay):

Parámetros:

self → instancia actual
first → nombre
last → apellido
pay → salario
4. Variables de Instancia

Dentro del constructor se crean atributos propios de cada objeto.

self.first = first
self.last = last
self.email = first + '.' + last + '@company.com'
self.pay = pay

Cada empleado tendrá sus propios valores.

5. Contador de Empleados

Cada vez que se crea una instancia:

Employee.num_of_emps += 1

El contador aumenta automáticamente.

Ejemplo:

0 → 1 → 2 → 3
6. Método fullname()

Devuelve el nombre completo del empleado.

def fullname(self):
    return '{} {}'.format(self.first, self.last)

Ejemplo:

emp_1.fullname()

Resultado:

Corey Schafer
7. Método apply_raise()

Aplica un aumento salarial.

self.pay = int(self.pay * self.raise_amt)

Ejemplo:

50000 × 1.04 = 52000
8. Métodos de Clase
set_raise_amt()

Permite modificar el aumento salarial de toda la clase.

@classmethod
def set_raise_amt(cls, amount):

Ejemplo:

Employee.set_raise_amt(1.05)

Ahora todos los empleados utilizan:

raise_amt = 1.05
from_string()

Permite crear empleados a partir de texto.

emp_str = 'John-Doe-70000'

Internamente:

first, last, pay = emp_str.split('-')

y luego:

return cls(first, last, pay)
9. Métodos Estáticos
is_workday()

Verifica si una fecha corresponde a un día laboral.

@staticmethod

No utiliza:

self
cls

Simplemente está relacionada lógicamente con la clase.

Ejemplo:

datetime.date(2024, 6, 1)

Resultado:

False

porque es sábado.

10. Herencia

Una de las características más importantes de la POO.

class Developer(Employee):

Significa:

Developer ES un Employee

Por lo tanto hereda:

fullname()
apply_raise()
set_raise_amt()
from_string()
is_workday()
email
pay
first
last
11. Sobrescritura de Variables de Clase

La clase Developer redefine:

raise_amt = 1.10

Ahora los desarrolladores reciben:

10% de aumento

mientras que los empleados normales reciben:

4% de aumento
12. Uso de super()

El constructor de Developer utiliza:

super().__init__(first, last, pay)

Esto ejecuta el constructor de Employee.

Equivale a:

Employee.__init__(self, first, last, pay)

pero es más limpio y recomendable.

13. Atributos Exclusivos de Developer

Los desarrolladores poseen un atributo adicional:

prog_lang

Ejemplo:

dev_1 = Developer(
    'Corey',
    'Schafer',
    50000,
    'Python'
)
print(dev_1.prog_lang)

Resultado:

Python
14. Clase Manager

La clase Manager también hereda de Employee.

class Manager(Employee):

Además posee una lista de empleados supervisados.

employees
15. Relaciones entre Objetos

Un Manager puede contener objetos Employee o Developer.

emp_3 = Manager(
    'Sue',
    'Smith',
    90000,
    [emp_1]
)

Esto crea una relación:

Manager
│
├── Developer (Corey)
16. Agregar Empleados
emp_3.add_emp(emp_2)

Resultado:

Manager
│
├── Corey
└── Test
17. Eliminar Empleados
emp_3.remove_emp(emp_2)

Resultado:

Manager
│
└── Corey
18. Mostrar Empleados Supervisados
emp_3.print_emps()

Salida:

--> Corey Schafer
--> Test User
19. isinstance()

Permite verificar si un objeto pertenece a una clase.

isinstance(emp_1, Employee)

Resultado:

True
isinstance(emp_1, Developer)

Resultado:

True

porque un Developer también es un Employee.

20. issubclass()

Permite verificar relaciones entre clases.

issubclass(Developer, Employee)

Resultado:

True
issubclass(Manager, Employee)

Resultado:

True
21. dict

Muestra todos los atributos almacenados en un objeto.

print(emp_1.__dict__)

Resultado:

{
    'first': 'Corey',
    'last': 'Schafer',
    'email': 'Corey.Schafer@company.com',
    'pay': 50000,
    'prog_lang': 'Python'
}

Muy útil para depuración.

22. Conceptos de POO Aprendidos
Concepto	Ejemplo
Clase	Employee
Objeto	emp_1
Herencia	Developer(Employee)
Constructor	init
Método de instancia	fullname()
Método de clase	set_raise_amt()
Método estático	is_workday()
Variable de clase	raise_amt
Variable de instancia	first
Sobrescritura	raise_amt = 1.10
super()	super().init()
Relación entre objetos	Manager → Employees
Verificación de tipos	isinstance()
Verificación de herencia	issubclass()
23. Relación con Django

Este proyecto es una excelente introducción a Django porque los mismos conceptos aparecen constantemente.

Por ejemplo:

class Product(models.Model):
    name = models.CharField(max_length=100)

es simplemente una clase.

Cada registro de la base de datos es una instancia:

product = Product.objects.get(id=1)

Además:

Los modelos usan herencia.
Los managers funcionan como métodos de clase.
Las relaciones ForeignKey son similares a la relación Manager → Employees.
Los métodos de modelo funcionan igual que fullname() o apply_raise().