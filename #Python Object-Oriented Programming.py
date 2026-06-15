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
        self.pay = int(self.pay * self.raise_amt)




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

class Developer(Employee): # La clase Developer hereda de Employee, lo que significa que tiene acceso a todos los atributos y métodos de Employee.
    raise_amt = 1.10 # Sobrescribimos la variable de clase para los desarrolladores, que tendrán un aumento salarial del 10% en lugar del 4% general.

    def __init__(self, first, last, pay,prog_lang): # Agregamos un nuevo atributo prog_lang para los desarrolladores.
        super().__init__(first, last, pay) # Llamamos al constructor de la clase padre (Employee) para inicializar los atributos heredados.#usamos super() para llamar al constructor de la clase padre y evitar repetir código.
        self.prog_lang = prog_lang # Inicializamos el nuevo atributo prog_lang específico de los desarrolladores.


class Manager(Employee): # La clase Manager también hereda de Employee.
    def __init__(self, first, last, pay, employees=None): # Agregamos un nuevo atributo employees para los gerentes, que es una lista de empleados que supervisan.
        super().__init__(first, last, pay) # Llamamos al constructor de la clase padre (Employee) para inicializar los atributos heredados.
        if employees is None: # Si no se proporciona una lista de empleados, inicializamos con una lista vacía.
            self.employees = []
        else:
            self.employees = employees # Inicializamos el nuevo atributo employees específico de los gerentes.

    def add_emp(self, emp): # Método para agregar un empleado a la lista de empleados supervisados por el gerente.
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp): # Método para eliminar un empleado de la lista de empleados supervisados por el gerente.
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self): # Método para imprimir la lista de empleados supervisados por el gerente.
        for emp in self.employees:
            print('-->', emp.fullname()) # Imprime el nombre completo de cada empleado supervisado por el gerente.


# Antes de crear empleados el contador vale 0.
print(Employee.num_of_emps)


# Creamos el primer objeto Employee.
#
# Python ejecuta internamente:
# Employee.__init__(emp_1, 'Corey', 'Schafer', 50000)
#
emp_1 = Developer ('Corey','Schafer',50000,'Python') # Creamos una instancia de Employee con los atributos especificados.
emp_2= Developer('Test', 'User', 60000,'Java')

emp_3 = Manager('Sue', 'Smith', 90000, [emp_1]) # Creamos una instancia de Manager que supervisa a emp_1.

print(emp_1.email) # Imprime el email generado automáticamente para emp_1.
print(emp_2.email) # Imprime el email generado automáticamente para emp_2.
print(emp_2.prog_lang) # Imprime el lenguaje de programación específico del desarrollador emp_2.
print(emp_1.prog_lang) # Imprime el lenguaje de programación específico del desarrollador emp_1.
print(emp_3.email) # Imprime el email generado automáticamente para emp_3.
emp_3.print_emps() # Imprime la lista de empleados supervisados por emp_

emp_3.add_emp(emp_2) # Agrega emp_2 a la lista de empleados supervisados por emp_3.
emp_3.print_emps() # Imprime la lista actualizada de empleados supervisados por emp_3.
emp_3.remove_emp(emp_2) # Elimina emp_1 de la lista de empleados supervisados por emp_3.
emp_3.print_emps() # Imprime la lista actualizada de empleados supervisados por

import datetime
my_date = datetime.date(2024, 6, 1)
print(Employee.is_workday(my_date)) # Llamada al método estático desde la clase.






# Ahora el contador vale 2 porque creamos dos empleados.
#(una instancia de Employee y otra de Developer, que también es un tipo de Employee).
print(Employee.num_of_emps)

print(issubclass(Developer, Employee)) # Verifica si Developer es una subclase de Employee. Devuelve True.
print(isinstance(emp_1, Employee)) # Verifica si emp_1 es una instancia de Employee. Devuelve True.
print(isinstance(emp_1, Developer)) # Verifica si emp_1 es una instancia

print(isinstance(emp_3, Manager)) # Verifica si emp_1 es una instancia de Manager.
print(issubclass(Manager, Employee)) # Verifica si Manager es una subclase de Employee.

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
print(emp_1.raise_amt) # Accedemos a la variable de clase a través de la instancia dev_1.
print(emp_2.raise_amt) # Accedemos a la variable de clase a través de la instancia dev_2.

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




