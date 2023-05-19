import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Clase que representa el editor de texto
class Editor:
    def __init__(self):
        self.texto = ""

    def escribir(self, texto):
        self.texto += texto

    def guardar_estado(self):
        # Crea un objeto Memento para guardar el estado actual del editor
        return Memento(self.texto)

    def restaurar_estado(self, memento):
        # Restaura el estado del editor a partir de un objeto Memento
        self.texto = memento.obtener_estado()

    def obtener_texto(self):
        # Devuelve el texto actual del editor
        return self.texto


# Clase que representa un Memento, que guarda un estado del editor en un momento dado
class Memento:
    def __init__(self, estado):
        self.estado = estado

    def obtener_estado(self):
        # Devuelve el estado guardado en el Memento
        return self.estado


# Clase que maneja el historial de estados del editor
class CaretakerEditor:
    def __init__(self):
        self.historial = []

    def guardar_estado(self, estado):
        # Guarda un estado en el historial
        self.historial.append(estado)

    def obtener_estado(self, indice):
        # Obtiene un estado del historial dado un índice
        if 0 <= indice < len(self.historial):
            return self.historial[indice]
        return None

    def deshacer(self):
        # Elimina el estado más reciente del historial (deshacer un cambio)
        if self.historial:
            self.historial.pop()


# Clase que maneja una lista de caretakers
class CaretakerList:
    def __init__(self):
        self.caretakers = []

    def agregar_caretaker(self, caretaker):
        # Agrega un caretaker a la lista
        self.caretakers.append(caretaker)

    def obtener_caretaker(self, indice):
        # Obtiene un caretaker de la lista dado un índice
        if 0 <= indice < len(self.caretakers):
            return self.caretakers[indice]
        return None

    def eliminar_caretaker(self, indice):
        # Elimina un caretaker de la lista dado un índice
        if 0 <= indice < len(self.caretakers):
            del self.caretakers[indice]

    def deshacer_todos(self):
        # Realiza la operación de deshacer en todos los caretakers de la lista
        for caretaker in self.caretakers:
            caretaker.deshacer()


# Clase que representa la interfaz de usuario del editor
class EditorInterfaz:
    def __init__(self, editor):
        self.editor = editor
        self.ventana = tk.Tk()
        self.ventana.title("Editor de Texto")
        self.ventana.geometry("600x500")

        self.ventana.resizable(False, False) # para desabilitar la opcion de maximizar
        self.ventana.configure(bg= "#9EDDE5")  # PARA CAMBIAR DE COLOR 

        self.area_texto = tk.Text(self.ventana)
        self.area_texto.pack()

        boton_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar)
        boton_guardar.pack()
        boton_guardar.place(x= 30, y=400)
        boton_guardar.configure(width=17, height=1)

        boton_deshacer = tk.Button(self.ventana, text="Deshacer", command=self.deshacer)
        boton_deshacer.pack()
        boton_deshacer.place(x= 170, y=400)
        boton_deshacer.configure(width=17, height=1)

        boton_abrir = tk.Button(self.ventana, text="Abrir", command=self.abrir_archivo)
        boton_abrir.pack()
        boton_abrir.place(x= 170, y=440)
        boton_abrir.configure(width=17, height=1)  

        boton_guardar_como = tk.Button(self.ventana, text="Guardar como...", command=self.guardar_como)
        boton_guardar_como.pack()
        boton_guardar_como.place(x= 310, y=440)  # UBICACION DEL BOTON
        #boton_guardar_como.configure(bg="RED")   # CAMBIAR EL COLOR DEL BOTON
        boton_guardar_como.configure(width=17, height=1)  # para asignar el tamaño del boton

        self.archivo_actual = None

    def guardar(self):
        # Guarda el estado actual del editor en el historial y actualiza el texto del editor
        estado = self.editor.guardar_estado()
        self.editor.escribir(self.area_texto.get("1.0", tk.END))
        estado_editor = self.editor.guardar_estado()
        estado.restaurar_estado(estado_editor)

    def deshacer(self):
        # Restaura el estado anterior del editor y actualiza el texto de la interfaz
        estado_anterior = self.editor.guardar_estado()
        self.editor.restaurar_estado(estado_anterior)
        self.area_texto.delete("1.0", tk.END)
        self.area_texto.insert(tk.END, self.editor.obtener_texto())


    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as f:
                contenido = f.read()
                self.editor.restaurar_estado(Memento(contenido))
                self.area_texto.delete("1.0", tk.END)
                self.area_texto.insert(tk.END, contenido)
                self.archivo_actual = archivo

    def guardar_archivo(self):
        contenido = self.area_texto.get("1.0", tk.END)
        if self.archivo_actual:
            with open(self.archivo_actual, "w") as f:
                f.write(contenido)
        else:
            self.guardar_como()

    def guardar_como(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.archivo_actual = archivo
            self.guardar_archivo()

    def iniciar(self):
        # Inicia la interfaz de usuario
        self.ventana.mainloop()


# Clase que representa una interfaz avanzada del editor con funcionalidades adicionales
class EditorInterfazAvanzado(EditorInterfaz):
    def __init__(self, editor):
        super().__init__(editor)

        boton_contar_palabras = tk.Button(self.ventana, text="Contar Palabras", command=self.contar_palabras)
        boton_contar_palabras.pack()
        boton_contar_palabras.place(x= 310, y=400)
        boton_contar_palabras.configure(width=17, height=1)

        boton_mayusculas = tk.Button(self.ventana, text="Convertir a Mayúscula", command=self.mayusculas)
        boton_mayusculas.pack()
        boton_mayusculas.place(x= 450, y=400)
        boton_mayusculas.configure(width=17, height=1)

    def contar_palabras(self):
        # Cuenta la cantidad de palabras en el texto del editor y muestra un mensaje emergente
        texto = self.editor.obtener_texto()
        palabras = texto.split()
        cantidad_palabras = len(palabras)
        messagebox.showinfo("Contador de Palabras", f"El texto contiene {cantidad_palabras} palabras.")

        
    def mayusculas(self):
        # Convierte el texto del editor a mayúsculas y actualiza el texto de la interfaz
        texto = self.editor.obtener_texto()
        texto_mayusculas = texto.upper()
        self.editor.escribir(texto_mayusculas)
        self.area_texto.delete("1.0", tk.END)
        self.area_texto.insert(tk.END, texto_mayusculas)

editor = Editor()
historial = CaretakerEditor()
caretaker_list = CaretakerList()
caretaker_list.agregar_caretaker(historial)
interfaz = EditorInterfazAvanzado(editor)

interfaz.iniciar()

