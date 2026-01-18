# Archivo principal para ejecutar la aplicación

from modelos.videojuego import Videojuego
from servicios.tienda import Tienda

def main():
    # Crear instancia de la tienda
    tienda = Tienda()

    # Crear videojuegos (instancias de la clase derivada)
    juego1 = Videojuego("FIFA 24", 59.99, "PS5")
    juego2 = Videojuego("Minecraft", 29.99, "PC")
    juego3 = Videojuego("Zelda", 69.99, "Nintendo Switch")

    # Agregar productos a la tienda
    tienda.agregar_producto(juego1)
    tienda.agregar_producto(juego2)
    tienda.agregar_producto(juego3)

    # Mostrar productos
    tienda.mostrar_productos()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
