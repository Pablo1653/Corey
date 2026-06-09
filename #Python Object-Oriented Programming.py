# Python Object-Oriented Programming (Programación Orientada a Objetos)

# Definimos una clase llamada Employee.
# Una clase es un "molde" a partir del cual se crean objetos.
class Employee:

    # Variable de clase.
    # Es compartida por TODOS los empleados.
    # Se utiliza para contar cuántos empleados se han creado.
    num_of_emps = 0

    # Variable de clase.
    # Representa un aumento salarial del 4%.
    # Todos los empleados tendrán acceso a esta variable.
    raise_amount = 1.04

    # Constructor.
    # Se ejecuta automáticamente cada vez que se crea un nuevo Employee.
    #
    # self representa la instancia actual (el objeto que se está creando).
    #
    # first = nombre
    # last = apellido
    # pay = salario
    def __init__(self, first, last, pay):

        # Variables de instancia.
        # Cada empleado tendrá sus propios valores.
        self.first = first
        self.last = last

        # Construimos automáticamente un email.
        self.email = first + '.' + last + '@company.com'

        # Guardamos el salario.
        self.pay = pay

        # Incrementamos el contador de empleados.
        # Como pertenece a la clase, accedemos mediante Employee.
        Employee.num_of_emps += 1

    # Método de instancia.
    # Devuelve el nombre completo del empleado.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # ESTE MÉTODO ESTÁ DUPLICADO.
    # Python sobrescribirá el método anterior y conservará solamente este.
    # En este caso no genera problemas porque ambos hacen exactamente lo mismo.
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


# Antes de crear empleados el contador vale 0.
print(Employee.num_of_emps)


# Creamos el primer objeto Employee.
#
# Python ejecuta internamente:
# Employee.__init__(emp_1, 'Corey', 'Schafer', 50000)
#
emp_1 = Employee('Corey', 'Schafer', 50000)


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
print(emp_1.__dict__)


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