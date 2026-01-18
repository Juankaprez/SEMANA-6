# Clase Tienda
# Maneja la lógica del sistema

class Tienda:
    def __init__(self):
        self.productos = []

    # Método para agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar todos los productos
    def mostrar_productos(self):
        print("=== Productos disponibles ===")
        for producto in self.productos:
            # Polimorfismo: cada objeto ejecuta su propia versión del método
            print(producto.mostrar_info())
