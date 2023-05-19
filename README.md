# Patron de diseño de comportamiento "Memento"
---INTEGRANTES---

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
Se define la primera clase Editor que representa el editor de texto. Tiene su atributo y los siguientes métodos:<br><br>
ATRIBUTO<br>
Texto (string): inicializa la instancia del editor con un atributo de texto vacío.<br>
MÉTODOS<br>
•	escribir(self, texto): agrega el texto proporcionado al atributo de texto existente.<br>
•	guardar_estado(self): crea y devuelve un objeto Memento para guardar el estado actual del editor.<br>
•	restaurar_estado(self, memento): restaura el estado del editor utilizando un objeto Memento.<br>
•	obtener_texto(self): devuelve el texto actual del editor.<br>

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/d6a14d63-43af-4d22-b534-6840a95b661d)


# 3.	
Se define la clase Memento que representa un objeto que guarda un estado del editor en un momento dado. Tiene su atributo y los siguientes métodos:<br><br>
ATRIBUTO<br>
      Estado(string): Inicializa el objeto Memento con un estado dado.<br>
MÉTODO<br>
•	obtener_estado(self): devuelve el estado guardado en el Memento.<br>

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/46d93539-cb71-4df5-bdf8-9471aa875a2b)

# 4.	
Se define la clase CaretakerEditor que maneja el historial de estados del editor. Tiene su atributo y los siguientes métodos:<br><br>
ATRIBUTO <br>
Historial(tipo lista): inicializa la instancia de CaretakerEditor con una lista vacía para almacenar el historial de estados.<br>
MÉTODOS<br>
•	guardar_estado(self, estado): guarda un estado en el historial.<br>
•	obtener_estado(self, indice): obtiene un estado del historial dado un índice.<br>
•	deshacer(self): elimina el estado más reciente del historial (deshacer un cambio).<br>

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/4997b969-a64e-4b09-91ce-919bfe3b6d5b)

# 5.	
Se define la clase CaretakerList que maneja una lista de CaretakerEditor. Tiene su atributo y los siguientes métodos:<br><br>
ATRIBUTO<br>
CaretakerList(tipo lista): inicializa la instancia de CaretakerList con una lista vacía para almacenar los caretakers.<br>
MÉTODOS<br>
•	agregar_caretaker(self, caretaker): agrega un caretaker a la lista.<br>
•	obtener_caretaker(self, indice): obtiene un caretaker de la lista dado un índice.<br>
•	eliminar_caretaker(self, indice): elimina un caretaker de la lista dado un índice.<br>
•	deshacer_todos(self): realiza la operación de deshacer en todos los caretakers de la lista.<br>

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/bf4bd12c-1f5b-4ac3-af21-3b5ed8da47e3)

# 6.	
Se define la clase EditorInterfaz que representa la interfaz de usuario del editor. Tiene sus atributos y los siguientes métodos:<br><br>
ATRIBUTO<br>
Editor(Editor): Inicializa la interfaz de usuario con una instancia de Editor.<br>
Ventana(tk.Tk): Crea la ventana principal.<br>
Area_texto(tk.Text): Campo para digitar el texto.<br>
Archivo_actual (String)<br><br>
MÉTODOS<br>
•	guardar(self): guarda el estado actual del editor en el historial y actualiza el texto del editor.<br>
•	deshacer(self): restaura el estado anterior del editor y actualiza el texto de la interfaz.<br>
•	abrir_archivo(self): abre un archivo de texto y muestra su contenido en el editor.<br>
•	guardar_archivo(self): guarda el contenido del editor en el archivo actualmente abierto.<br>
•	guardar_como(self): guarda el contenido del editor en un archivo nuevo.<br>
•	iniciar(self): inicia la interfaz de usuario del editor.<br>

# 7.	
Se define la clase EditorInterfazAvanzado que se hereda de la clase EditorInterfaz y agrega métodos adicionales. <br><br>
•	__init__(self, editor): inicializa la interfaz de usuario avanzada y agrega botones adicionales de contar palabras y conversor de texto a mayúscula.<br>
•	contar_palabras(self): cuenta la cantidad de palabras en el texto del editor y muestra un mensaje emergente.<br>
•	mayúsculas(self): convierte el texto del editor a mayúsculas y actualiza el texto de la interfaz.<br>

# 8.	
Se crean instancias de las clases Editor, CaretakerEditor, CaretakerList y EditorInterfazAvanzado.

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/20d7eb17-1493-43cf-bbce-095d0b1062ac)

# 10.	
Se llama al método iniciar() de la instancia de EditorInterfazAvanzado para iniciar la interfaz de usuario del editor.<br>
INTERFAZ DEL EDITOR DE TEXTO CON EL PATRÓN MEMENTO

![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/d0fda09a-c046-41b7-a061-15702bcbdbca)

# Interfaz del editor de texto con el patrón memento
![image](https://github.com/jhimi17/Patron_Memento/assets/101279472/777d20cd-e60c-4bff-8157-9c522512d1b3)

