"""
Ejemplo de Árbol Binario de Búsqueda (BST)
Estructuras de Datos - Ingeniería de Software
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq:
                self._insertar(nodo.izq, valor)
            else:
                nodo.izq = Nodo(valor)
        else:
            if nodo.der:
                self._insertar(nodo.der, valor)
            else:
                nodo.der = Nodo(valor)

    def inorder(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
            nodo = self.raiz
        if nodo:
            self.inorder(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self.inorder(nodo.der, resultado)
        return resultado


if __name__ == "__main__":
    arbol = ArbolBinario()
    for v in [50, 30, 70, 20, 40]:
        arbol.insertar(v)

    print(arbol.inorder())  # [20, 30, 40, 50, 70]
