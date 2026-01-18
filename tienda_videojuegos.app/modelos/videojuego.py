# Clase Videojuego
# Hereda de Producto (herencia)

from modelos.producto import Producto

class Videojuego(Producto):
    def __init__(self, nombre, precio, plataforma):
        # Llamada al constructor de la clase base
        super().__init__(nombre, precio)
        self.plataforma = plataforma

    # Sobrescritura del método (polimorfismo)
    def mostrar_info(self):
        return (f"Videojuego: {self._nombre} | "
                f"Plataforma: {self.plataforma} | "
                f"Precio: ${self._precio}")
            
