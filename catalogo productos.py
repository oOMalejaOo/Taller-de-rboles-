"""
Caso real: Catálogo de productos de una tienda
Se usa un Árbol Binario de Búsqueda para mantener los productos
ordenados por código, permitiendo búsquedas rápidas y listados
ordenados sin tener que ordenar el arreglo cada vez.
"""


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"


class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.izq = None
        self.der = None


class CatalogoProductos:
    def __init__(self):
        self.raiz = None

    def agregar(self, codigo, nombre, precio):
        nuevo = Producto(codigo, nombre, precio)
        if not self.raiz:
            self.raiz = Nodo(nuevo)
        else:
            self._agregar(self.raiz, nuevo)

    def _agregar(self, nodo, producto):
        if producto.codigo < nodo.producto.codigo:
            if nodo.izq:
                self._agregar(nodo.izq, producto)
            else:
                nodo.izq = Nodo(producto)
        else:
            if nodo.der:
                self._agregar(nodo.der, producto)
            else:
                nodo.der = Nodo(producto)

    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if codigo == nodo.producto.codigo:
            return nodo.producto
        elif codigo < nodo.producto.codigo:
            return self._buscar(nodo.izq, codigo)
        else:
            return self._buscar(nodo.der, codigo)

    def listar_ordenado(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
            nodo = self.raiz
        if nodo:
            self.listar_ordenado(nodo.izq, resultado)
            resultado.append(nodo.producto)
            self.listar_ordenado(nodo.der, resultado)
        return resultado


if __name__ == "__main__":
    catalogo = CatalogoProductos()

    catalogo.agregar(105, "Teclado mecánico", 45.99)
    catalogo.agregar(102, "Mouse inalámbrico", 19.50)
    catalogo.agregar(110, "Monitor 24\"", 150.00)
    catalogo.agregar(101, "Cable HDMI", 8.75)
    catalogo.agregar(108, "Audífonos", 35.00)

    print("=== Catálogo ordenado por código ===")
    for producto in catalogo.listar_ordenado():
        print(producto)

    print("\n=== Búsqueda ===")
    codigo_buscado = 108
    resultado = catalogo.buscar(codigo_buscado)
    if resultado:
        print(f"Encontrado: {resultado}")
    else:
        print(f"No existe un producto con código {codigo_buscado}")
