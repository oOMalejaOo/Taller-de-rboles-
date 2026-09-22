import tkinter as tk


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


def mostrar_ventana_grafica(catalogo):
  ventana = tk.Tk()
  ventana.title("Visualizador Gráfico - Árbol Binario de Búsqueda")
  ventana.geometry("800x600")
  ventana.config(bg="#f4f6f9")

  titulo = tk.Label(
      ventana,
      text="Catálogo de Productos (Estructura de Árbol)",
      font=("Arial", 14, "bold"),
      bg="#f4f6f9",
      fg="#333333",
  )
  titulo.pack(pady=10)

  canvas = tk.Canvas(ventana, bg="white", highlightthickness=0)
  canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

  def dibujar_nodo(nodo, x, y, dx):
    if nodo is None:
      return

    radio = 26

    # Dibujar líneas hacia los hijos antes de dibujar los círculos
    if nodo.izq:
      x_hijo = x - dx
      y_hijo = y + 70
      canvas.create_line(
          x, y, x_hijo, y_hijo, fill="#7f8c8d", width=2, arrow=tk.LAST
      )
      dibujar_nodo(nodo.izq, x_hijo, y_hijo, dx / 2)

    if nodo.der:
      x_hijo = x + dx
      y_hijo = y + 70
      canvas.create_line(
          x, y, x_hijo, y_hijo, fill="#7f8c8d", width=2, arrow=tk.LAST
      )
      dibujar_nodo(nodo.der, x_hijo, y_hijo, dx / 2)

    # Dibujar el nodo actual (círculo y texto)
    canvas.create_oval(
        x - radio,
        y - radio,
        x + radio,
        y + radio,
        fill="#3498db",
        outline="#2980b9",
        width=2,
    )
    canvas.create_text(
        x,
        y - 6,
        text=str(nodo.producto.codigo),
        font=("Arial", 10, "bold"),
        fill="white",
    )
    canvas.create_text(
        x,
        y + 10,
        text=nodo.producto.nombre.split()[0],
        font=("Arial", 8),
        fill="white",
    )

  if catalogo.raiz:
    # Dibujar recursivamente empezando desde la parte superior central
    dibujar_nodo(catalogo.raiz, x=400, y=50, dx=180)
  else:
    canvas.create_text(
        400,
        250,
        text="El catálogo está vacío",
        font=("Arial", 12),
        fill="#e74c3c",
    )

  ventana.mainloop()


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

  print("\nAbriendo ventana gráfica con el árbol...")
  mostrar_ventana_grafica(catalogo)
        print(f"Encontrado: {resultado}")
    else:
        print(f"No existe un producto con código {codigo_buscado}")
