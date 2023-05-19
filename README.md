# Patron de diseño de comportamiento "Memento"
---INTEGRANTES---.

■  Sánchez Cabrera, Kevin Kennedy.<br>
■  Marcelo Luyo, Jhimi Misael.


El programa se trata de Editor de Texto escrito en el lenguaje Python con la librería Tkinter y aplicando principalmente el patrón de diseño de comportamiento “MEMENTO”.

# 1.	
Inicialmente se importan los módulos o bibliotecas necesarios de Tkinter: 

•	Tkinter: Para la creación de la interfaz gráfica del programa<br>
•	Messagebox: Para la salida de una ventana emergente con el resultado esperado.<br>
•	Filedialog: Para abrir y guardar archivos en este caso solo en formato texto.<br>

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/38e82f77-0b19-4f37-b50f-20e95c1969cf)

# 2.	
Se define la primera clase Editor que representa el editor de texto. Tiene su atributo y los siguientes métodos:<br>
ATRIBUTO<br>
Texto (string): inicializa la instancia del editor con un atributo de texto vacío.<br>
MÉTODOS<br>
•	escribir(self, texto): agrega el texto proporcionado al atributo de texto existente.<br>
•	guardar_estado(self): crea y devuelve un objeto Memento para guardar el estado actual del editor.<br>
•	restaurar_estado(self, memento): restaura el estado del editor utilizando un objeto Memento.<br>
•	obtener_texto(self): devuelve el texto actual del editor.<br>

# 3.	
Se define la clase Memento que representa un objeto que guarda un estado del editor en un momento dado. Tiene su atributo y los siguientes métodos:<br>
ATRIBUTO<br>
      Estado(string): Inicializa el objeto Memento con un estado dado.<br>
MÉTODO<br>
•	obtener_estado(self): devuelve el estado guardado en el Memento.<br>

# 4.	
Se define la clase CaretakerEditor que maneja el historial de estados del editor. Tiene su atributo y los siguientes métodos:
ATRIBUTO 
Historial(tipo lista): inicializa la instancia de CaretakerEditor con una lista vacía para almacenar el historial de estados.
MÉTODOS
•	guardar_estado(self, estado): guarda un estado en el historial.
•	obtener_estado(self, indice): obtiene un estado del historial dado un índice.
•	deshacer(self): elimina el estado más reciente del historial (deshacer un cambio).

# 5.	
Se define la clase CaretakerList que maneja una lista de CaretakerEditor. Tiene su atributo y los siguientes métodos:
ATRIBUTO
CaretakerList(tipo lista): inicializa la instancia de CaretakerList con una lista vacía para almacenar los caretakers.
MÉTODOS
•	agregar_caretaker(self, caretaker): agrega un caretaker a la lista.
•	obtener_caretaker(self, indice): obtiene un caretaker de la lista dado un índice.
•	eliminar_caretaker(self, indice): elimina un caretaker de la lista dado un índice.
•	deshacer_todos(self): realiza la operación de deshacer en todos los caretakers de la lista.

# 6.	
Se define la clase EditorInterfaz que representa la interfaz de usuario del editor. Tiene sus atributos y los siguientes métodos:
ATRIBUTO
Editor(Editor): Inicializa la interfaz de usuario con una instancia de Editor.
Ventana(tk.Tk): Crea la ventana principal.
Area_texto(tk.Text): Campo para digitar el texto.
Archivo_actual (String)
MÉTODOS
•	guardar(self): guarda el estado actual del editor en el historial y actualiza el texto del editor.
•	deshacer(self): restaura el estado anterior del editor y actualiza el texto de la interfaz.
•	abrir_archivo(self): abre un archivo de texto y muestra su contenido en el editor.
•	guardar_archivo(self): guarda el contenido del editor en el archivo actualmente abierto.
•	guardar_como(self): guarda el contenido del editor en un archivo nuevo.
•	iniciar(self): inicia la interfaz de usuario del editor.
7.	Se define la clase EditorInterfazAvanzado que se hereda de la clase EditorInterfaz y agrega métodos adicionales. 
•	__init__(self, editor): inicializa la interfaz de usuario avanzada y agrega botones adicionales de contar palabras y conversor de texto a mayúscula.
•	contar_palabras(self): cuenta la cantidad de palabras en el texto del editor y muestra un mensaje emergente.
•	mayúsculas(self): convierte el texto del editor a mayúsculas y actualiza el texto de la interfaz.
8.	Se crean instancias de las clases Editor, CaretakerEditor, CaretakerList y EditorInterfazAvanzado.
9.	Se llama al método iniciar() de la instancia de EditorInterfazAvanzado para iniciar la interfaz de usuario del editor.
INTERFAZ DEL EDITOR DE TEXTO CON EL PATRÓN MEMENTO
