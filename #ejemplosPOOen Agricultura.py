"""
POO APLICADA A AGRONOMÍA - Código maestro
Cubre: Abstracción, Encapsulamiento, Herencia, Polimorfismo, Composición
"""

from abc import ABC, abstractmethod  # ABC = Abstract Base Class, herramienta para forzar abstracción


# ============================================================
# 1) ABSTRACCIÓN
# ============================================================
# Una clase abstracta define QUÉ debe hacer un cultivo, sin decir CÓMO.
# No se puede instanciar directamente: Cultivo() tiraría error.
# Sirve como "contrato" que obligan a cumplir las clases hijas.

class Cultivo(ABC):

    def __init__(self, nombre: str, hectareas: float):
        # Atributos "protegidos" (convención _atributo) -> ver Encapsulamiento más abajo
        self._nombre = nombre
        self._hectareas = hectareas
        self._humedad_suelo = 50.0  # % inicial por defecto

    @abstractmethod
    def calcular_rendimiento(self) -> float:
        """Cada cultivo hijo DEBE implementar esto (quintales por hectárea).
        No tiene cuerpo real acá: es solo la firma del método."""
        pass

    @abstractmethod
    def dias_a_cosecha(self) -> int:
        """Idem: cada cultivo define sus propios días de ciclo."""
        pass

    def resumen(self) -> str:
        # Método concreto (no abstracto): compartido por todas las hijas tal cual.
        # Usa polimorfismo internamente al llamar self.calcular_rendimiento()
        return (f"{self._nombre} | {self._hectareas} ha | "
                f"Rinde estimado: {self.calcular_rendimiento():.1f} qq/ha | "
                f"Cosecha en {self.dias_a_cosecha()} días")


# ============================================================
# 2) ENCAPSULAMIENTO
# ============================================================
# Protegemos el estado interno (humedad del suelo) para que no se pueda
# asignar cualquier valor disparatado desde afuera (ej: humedad = -300).
# Usamos @property (getter) y @setter con validación.

class SensorHumedad:
    def __init__(self):
        self.__valor = 50.0  # doble guion bajo = "name mangling", más privado aún

    @property
    def valor(self) -> float:
        # Getter: permite leer sensor.valor como si fuera un atributo normal
        return self.__valor

    @valor.setter
    def valor(self, nuevo: float):
        # Setter: acá metemos la validación. Si alguien hace sensor.valor = -10,
        # esto lo intercepta y evita el dato corrupto.
        if not (0 <= nuevo <= 100):
            raise ValueError("La humedad debe estar entre 0 y 100%")
        self.__valor = nuevo


# ============================================================
# 3) HERENCIA
# ============================================================
# Soja, Maiz y Trigo heredan de Cultivo: reciben __init__, resumen(), etc.
# gratis, y solo agregan/sobreescriben lo que les es propio.

class Soja(Cultivo):
    def __init__(self, hectareas: float, grupo_madurez: str = "IV"):
        super().__init__("Soja", hectareas)  # llama al __init__ del padre
        self.grupo_madurez = grupo_madurez

    def calcular_rendimiento(self) -> float:
        # Implementación PROPIA del método abstracto del padre
        base = 32.0
        if self._humedad_suelo < 30:
            base *= 0.7  # estrés hídrico penaliza rinde
        return base

    def dias_a_cosecha(self) -> int:
        return 140


class Maiz(Cultivo):
    def __init__(self, hectareas: float, densidad_siembra: int = 75000):
        super().__init__("Maíz", hectareas)
        self.densidad_siembra = densidad_siembra  # plantas/ha

    def calcular_rendimiento(self) -> float:
        base = 95.0
        if self._humedad_suelo < 40:
            base *= 0.6  # el maíz es más sensible a falta de agua que la soja
        return base

    def dias_a_cosecha(self) -> int:
        return 150


class Trigo(Cultivo):
    def __init__(self, hectareas: float):
        super().__init__("Trigo", hectareas)

    def calcular_rendimiento(self) -> float:
        return 40.0 if self._humedad_suelo >= 25 else 28.0

    def dias_a_cosecha(self) -> int:
        return 120


# ============================================================
# 4) POLIMORFISMO
# ============================================================
# Distintos objetos (Soja, Maiz, Trigo) responden al MISMO método
# calcular_rendimiento() cada uno a su manera. El código que los usa
# no necesita saber de qué tipo es cada uno: los trata a todos como "Cultivo".

def informe_campana(cultivos: list[Cultivo]) -> None:
    print("=== INFORME DE CAMPAÑA ===")
    for c in cultivos:
        # Acá está el polimorfismo puro: mismo método, distinto comportamiento
        # según la clase real del objeto (Soja, Maiz o Trigo).
        print(c.resumen())


# ============================================================
# 5) COMPOSICIÓN
# ============================================================
# Una Parcela "TIENE" cultivos y "TIENE" un sensor -> composición ("has-a"),
# en vez de heredar de ellos ("is-a", que sería herencia y no aplica acá).
# Si la Parcela se destruye, sus sensores/cultivos internos dejan de tener sentido:
# esa dependencia fuerte de vida es la marca de la composición.

class Parcela:
    def __init__(self, id_parcela: str):
        self.id_parcela = id_parcela
        self.sensor = SensorHumedad()          # composición: Parcela tiene-un Sensor
        self.cultivos: list[Cultivo] = []       # composición: Parcela tiene-varios Cultivo

    def sembrar(self, cultivo: Cultivo):
        cultivo._humedad_suelo = self.sensor.valor  # sincroniza el sensor con el cultivo
        self.cultivos.append(cultivo)

    def actualizar_humedad(self, nueva_humedad: float):
        self.sensor.valor = nueva_humedad  # pasa por el setter validado (encapsulamiento)
        for cultivo in self.cultivos:
            cultivo._humedad_suelo = nueva_humedad


# ============================================================
# USO / DEMO
# ============================================================
if __name__ == "__main__":
    parcela_norte = Parcela("Lote 7 - Norte")

    parcela_norte.sembrar(Soja(hectareas=40))
    parcela_norte.sembrar(Maiz(hectareas=25))
    parcela_norte.sembrar(Trigo(hectareas=15))

    informe_campana(parcela_norte.cultivos)

    print("\n--- Baja la humedad por sequía ---")
    parcela_norte.actualizar_humedad(20)  # dispara validación del setter
    informe_campana(parcela_norte.cultivos)

    print("\n--- Probando encapsulamiento: valor inválido ---")
    try:
        parcela_norte.sensor.valor = 150  # esto va a fallar, humedad no puede ser > 100
    except ValueError as e:
        print(f"Error atrapado: {e}")