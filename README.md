# Kata_02_AYED2

CONSIGNA DEL KATA:
Kata 02 - 28/05/2025 - Python Tkinter SQLite
jose Luis Oemig

Hola Jovenes Padawan.
Adjunto el Kata que Deben hacer el Próximo Miércoles.
Dado que han reaccionado excelente al anterior kata, quería proponer (en función de lo Hablado Ayer) que si quieren trabajarlo antes estaría Muy Bueno y podríamos usar "Parte" de esa Clase para Una Master Class de Arquitectura y Patrones.
Por supuesto lo pongo a Consideración (postear acá).
El Kata consiste en crear una GUI en Python y TKinter que conecte con SQLite para gestionar una "Nomina de Empleados".
Sucede que el Anterior programador en un Brote Místico comenzó a dedicarse a otra cosa y a dejado a nuestro cliente a la deriva, razón x la cual nos convoca.
Por suerte tiene el Código fuente (que comparte), pero desea hacer unas modificaciones y comenzar a aplicar un diseño que contenga aspectos de Ingeniería de Software, asi que el desarrollo del Kata será Refactorizar el Diseño, rearmarlo, proveyendo Modularidad, Encapsulamiento, Seguridad, Escalabilidad, Flexibilidad....
Pero como no nos andamos con Chiquitas, Mañana lo van a Trabajar y Refactorizar en Ingeniería de Software.
Quedamos en Contacto.

Un abrazo.
Jose Luis.

En la carpeta ORIGINAL se encuentran los archivos orignales, fuera se encuentra la refactorizacion.
para iniciar el programa ejecutar:
python main.py
en la carpeta _ORIGINAL se encuentra el prooyecto en el que tenemos que trabajar
en kata02_refactorizado la refactorizacion separando en modulos segun funcionalidad
Breve explicación de la función principal de cada archivo .py:

- **main.py**: Es el punto de entrada de la aplicación. Inicializa la ventana principal de Tkinter y lanza la interfaz gráfica (`EmployeeGUI`).

- **employee.py**: Define la clase `Employee`, que representa la estructura de los datos de un empleado (id, nombre, edad, email, etc.).

- **employee_repository.py**: Contiene la clase `EmployeeRepository`, encargada de todas las operaciones con la base de datos SQLite (crear tabla, insertar, actualizar, eliminar y consultar empleados).

- **employee_service.py**: Define la clase `EmployeeService`, que actúa como intermediario entre la interfaz gráfica y el repositorio, gestionando la lógica de negocio relacionada con los empleados.

- **employee_gui.py**: Implementa la clase `EmployeeGUI`, que construye y gestiona la interfaz gráfica de usuario, permitiendo interactuar con los datos de los empleados (agregar, mostrar, editar, eliminar).
