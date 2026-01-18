# Clase base Producto
# Aplica encapsulación y sirve como base para herencia

class Producto:
    def __init__(self, nombre, precio):
        # Atributos protegidos (encapsulación)
        self._nombre = nombre
        self._precio = precio

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    # Método que será sobrescrito (polimorfismo)
    def mostrar_info(self):
        return f"Producto: {self._nombre} - Precio: ${self._precio}"
