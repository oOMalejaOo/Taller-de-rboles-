#Maria Alejandra Ramírez Torres
#Danie Felipe Cubillos Antonio

import tkinter as tk
from tkinter import messagebox

# ==========================================
# NODO DEL ÁRBOL
# ==========================================
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# ==========================================
# SISTEMA DE ARCHIVOS
# ==========================================
class SistemaArchivos:
    def __init__(self):
        self.raiz = None

    def crear_raiz(self, nombre):
        self.raiz = Nodo(nombre)

    def buscar_carpeta(self, nombre, nodo=None):
        """
        Busca una carpeta dentro del árbol. Utiliza DFS recursivo.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.nombre == nombre:
            return nodo
        
        for hijo in nodo.hijos:
            encontrado = self.buscar_carpeta(nombre, hijo)
            if encontrado:
                return encontrado
        return None

    def agregar_carpeta(self, padre, nombre):
        """
        Agrega una carpeta dentro de otra carpeta.
        """
        carpeta_padre = self.buscar_carpeta(padre)
        if carpeta_padre is None:
            return False
        nueva_carpeta = Nodo(nombre)
        carpeta_padre.agregar_hijo(nueva_carpeta)
        return True

    def dfs(self):
        """
        Recorrido DFS del árbol (Preorden corregido).
        """
        visitados = []
        
        def recorrer(nodo):
            if nodo is None:
                return
            visitados.append(nodo.nombre)
            for hijo in nodo.hijos:
                recorrer(hijo)
                
        if self.raiz:
            recorrer(self.raiz)
        return visitados

# ==========================================
# INTERFAZ GRÁFICA
# ==========================================
def mostrar_ventana(sistema):
    ventana = tk.Tk()
    ventana.title("Sistema de archivos - DFS")
    ventana.geometry("1000x700")
    ventana.config(bg="#f4f6f9")

    # --------------------------------------
    # TÍTULO
    # --------------------------------------
    titulo = tk.Label(
        ventana, 
        text="Sistema de Archivos - Recorrido DFS", 
        font=("Arial", 18, "bold"), 
        bg="#f4f6f9", 
        fg="#1f5f78"
    )
    titulo.pack(pady=10)

    subtitulo = tk.Label(
        ventana, 
        text="Recorrido de carpetas y subcarpetas utilizando búsqueda en profundidad", 
        font=("Arial", 11), 
        bg="#f4f6f9", 
        fg="#444444"
    )
    subtitulo.pack(pady=5)

    # --------------------------------------
    # CANVAS
    # --------------------------------------
    canvas = tk.Canvas(
        ventana, 
        bg="white", 
        highlightthickness=0
    )
    canvas.pack(
        fill=tk.BOTH, 
        expand=True, 
        padx=20, 
        pady=10
    )

    # --------------------------------------
    # DIBUJAR ÁRBOL (POSICIONES)
    # --------------------------------------
    posiciones = {}
    contador = [0]

    def calcular_posiciones(nodo, nivel=0):
        if nodo is None:
            return
        for hijo in nodo.hijos:
            calcular_posiciones(hijo, nivel + 1)
        contador[0] += 1
        x = contador[0] * 90
        y = 70 + nivel * 100
        posiciones[nodo] = (x, y)

    calcular_posiciones(sistema.raiz)

    # --------------------------------------
    # DIBUJAR CONEXIONES
    # --------------------------------------
    def dibujar_lineas(nodo):
        if nodo is None:
            return
        x, y = posiciones[nodo]
        for hijo in nodo.hijos:
            x_hijo, y_hijo = posiciones[hijo]
            canvas.create_line(
                x, y + 25, 
                x_hijo, y_hijo - 25, 
                fill="#7f8c8d", 
                width=2
            )
            dibujar_lineas(hijo)

    dibujar_lineas(sistema.raiz)

    # --------------------------------------
    # DIBUJAR NODOS
    # --------------------------------------
    def dibujar_nodos(nodo):
        if nodo is None:
            return
        x, y = posiciones[nodo]
        radio = 30
        canvas.create_oval(
            x - radio, y - radio, 
            x + radio, y + radio, 
            fill="#16a9c7", 
            outline="#0b7891", 
            width=2
        )
        canvas.create_text(
            x, y, 
            text=nodo.nombre, 
            font=("Arial", 8, "bold"), 
            fill="white"
        )
        for hijo in nodo.hijos:
            dibujar_nodos(hijo)

    dibujar_nodos(sistema.raiz)

    # --------------------------------------
    # RESULTADO DFS
    # --------------------------------------
    resultado = sistema.dfs()
    texto_dfs = tk.Label(
        ventana, 
        text="DFS: " + " → ".join(resultado), 
        font=("Arial", 11, "bold"), 
        bg="#f4f6f9", 
        fg="#1f5f78"
    )
    texto_dfs.pack(pady=10)

    # --------------------------------------
    # EXPLICACIÓN
    # --------------------------------------
    explicacion = tk.Label(
        ventana, 
        text=(
            "DFS visita una carpeta y luego explora sus subcarpetas "
            "hasta llegar al final de una rama antes de retroceder."
        ), 
        font=("Arial", 10), 
        bg="#f4f6f9", 
        fg="#333333"
    )
    explicacion.pack(pady=5)

    ventana.mainloop()

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
if __name__ == "__main__":
    sistema = SistemaArchivos()

    # Carpeta principal
    sistema.crear_raiz("Documentos")

    # Subcarpetas
    sistema.agregar_carpeta("Documentos", "Universidad")
    sistema.agregar_carpeta("Documentos", "Trabajo")
    sistema.agregar_carpeta("Documentos", "Personal")

    # Subcarpetas de Universidad
    sistema.agregar_carpeta("Universidad", "Programacion")
    sistema.agregar_carpeta("Universidad", "Matematicas")

    # Subcarpetas de Programacion
    sistema.agregar_carpeta("Programacion", "Python")
    sistema.agregar_carpeta("Programacion", "Java")

    # Subcarpetas de Trabajo
    sistema.agregar_carpeta("Trabajo", "Informes")
    sistema.agregar_carpeta("Trabajo", "Proyectos")

    # Subcarpetas de Personal
    sistema.agregar_carpeta("Personal", "Fotos")
    sistema.agregar_carpeta("Personal", "Documentos")

    # --------------------------------------
    # MOSTRAR RECORRIDO DFS EN CONSOLA
    # --------------------------------------
    print("======================================")
    print("       SISTEMA DE ARCHIVOS")
    print("======================================")
    print("\nRecorrido DFS:")
    recorrido = sistema.dfs()
    for i, carpeta in enumerate(recorrido, 1):
        print(f"{i}. {carpeta}")

    print("\nAbriendo representación gráfica...")
    mostrar_ventana(sistema)
