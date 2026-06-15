
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
