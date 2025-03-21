# Herencia multiple
"""La herencia múltiple en Python permite que una clase herede de más de una clase base. Un caso práctico donde esto es útil es en un sistema de empleados en una empresa donde algunos trabajadores pueden ser tanto empleados como freelancers."""

## Ejemplo

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

class Freelancer:
    def __init__(self, tarifa_por_hora):
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self, horas):
        return self.tarifa_por_hora * horas

# Clase que hereda de Empleado y Freelancer
class TrabajadorHibrido(Empleado, Freelancer):
    def __init__(self, nombre, salario, tarifa_por_hora):
        Empleado.__init__(self, nombre, salario)
        Freelancer.__init__(self, tarifa_por_hora)

    def mostrar_info(self):
        return f"Trabajador Híbrido: {self.nombre}, Salario: {self.salario}, Tarifa por hora: {self.tarifa_por_hora}"

# Uso del sistema
trabajador = TrabajadorHibrido("Camilo", 3000, 20)
print(trabajador.mostrar_info())
print(f"Pago por 10 horas extra: {trabajador.calcular_pago(10)}")

## Explicacion
"""
1.´´´Empleado´´´ tiene atributos de salario.
2.´´´Freelancer´´´ tiene una tarifa por hora y un método para calcular el pago.
3.´´´TrabajadorHibrido´´´ combina ambas clases y puede actuar como empleado o freelancer.
4.Se usa herencia múltiple para aprovechar los métodos y atributos de ambas clases.

Este enfoque es útil cuando se necesita combinar comportamientos de diferentes clases sin duplicar código."""








