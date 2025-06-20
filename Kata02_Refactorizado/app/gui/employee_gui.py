from tkinter import ttk, messagebox, END
import tkinter as tk
from app.services.employee_service import EmployeeService
from app.models.employee import Employee


class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        self.service = EmployeeService()
        self.row = None

        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.doj = tk.StringVar()
        self.email = tk.StringVar()
        self.gender = tk.StringVar()
        self.contact = tk.StringVar()
        self.address = tk.StringVar()  

        self.create_ui()
        self.display_employees()  # Mostrar empleados al iniciar

    def create_ui(self):
        self.root.title("Employee Management System")
        self.root.geometry("1280x720")
        self.root.config(bg="#2c3e50")
        self.root.attributes("-zoomed", True)

        entries_frame = tk.Frame(self.root, bg="#535c68")
        entries_frame.pack(side=tk.TOP, fill=tk.X)

        title = tk.Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"),
                          bg="#535c68", fg="white")
        title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Campos del formulario
        tk.Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.name, font=("Calibri", 16), width=30).grid(
            row=1, column=1, padx=10, pady=10, sticky="w")

        tk.Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=1, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.age, font=("Calibri", 16), width=30).grid(
            row=1, column=3, padx=10, pady=10, sticky="w")

        tk.Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.doj, font=("Calibri", 16), width=30).grid(
            row=2, column=1, padx=10, pady=10, sticky="w")

        tk.Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=2, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.email, font=("Calibri", 16), width=30).grid(
            row=2, column=3, padx=10, pady=10, sticky="w")

        tk.Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        combo_gender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28,
                                    textvariable=self.gender, state="readonly")
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=3, column=1, padx=10, sticky="w")

        tk.Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=3, column=2, padx=10, pady=10, sticky="w")
        tk.Entry(entries_frame, textvariable=self.contact, font=("Calibri", 16), width=30).grid(
            row=3, column=3, padx=10, sticky="w")

        tk.Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")

        self.txt_address = tk.Text(entries_frame, width=85, height=5, font=("Calibri", 16))
        self.txt_address.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

        btn_frame = tk.Frame(entries_frame, bg="#535c68")
        btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        tk.Button(btn_frame, command=self.add_employee, text="Add Details", width=15,
                  font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0).grid(row=0, column=0)

        tk.Button(btn_frame, command=self.update_employee, text="Update Details", width=15,
                  font=("Calibri", 16, "bold"), fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, command=self.delete_employee, text="Delete Details", width=15,
                  font=("Calibri", 16, "bold"), fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)

        tk.Button(btn_frame, command=self.clear_fields, text="Clear Details", width=15,
                  font=("Calibri", 16, "bold"), fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

        # Tabla para mostrar empleados
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "DOJ", "Email", "Gender", "Contact", "Address"), show="headings")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Age", width=60, anchor="center")
        self.tree.column("DOJ", width=100, anchor="center")
        self.tree.column("Email", width=180)
        self.tree.column("Gender", width=80, anchor="center")
        self.tree.column("Contact", width=100)
        self.tree.column("Address", width=200)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Evento para seleccionar empleado al hacer clic en la fila
        self.tree.bind("<ButtonRelease-1>", self.get_data)

        # Boton inferior para salir
        exit_button = tk.Button(self.root, text="Salir", command=self.root.destroy, bg="#e74c3c", fg="white", font=("Calibri", 14, "bold"))
        exit_button.pack(side=tk.BOTTOM, pady=20)

        # Botón "Acerca de" en la esquina inferior derecha
        about_button = tk.Button(
            self.root,
            text="Acerca de",
            command=self.show_about,
            bg="#34495e",
            fg="#f1c40f",
            font=("Calibri", 13, "bold"),
            activebackground="#2c3e50",
            activeforeground="#f9e79f",
            relief="raised",
            bd=2
        )
        about_button.place(relx=0.99, rely=0.97, anchor="se")

    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.overrideredirect(True)
        about_window.configure(bg="#222831")

        # Tamaño de la ventana acerca de
        width, height = 600, 260

        # Obtener posición y tamaño de la ventana principal
        self.root.update_idletasks()
        x_root = self.root.winfo_x()
        y_root = self.root.winfo_y()
        w_root = self.root.winfo_width()
        h_root = self.root.winfo_height()

        # Calcular posición centrada respecto a la ventana principal
        x = x_root + (w_root // 2) - (width // 2)
        y = y_root + (h_root // 2) - (height // 2)
        about_window.geometry(f"{width}x{height}+{x}+{y}")

        msg = (
            "Si te gustó este proyecto considera donar al autor\n"
            "Carlos Guariglia\n"
            "un café pero que no sea del buffet, ya que actualmente\n"
            "lo está manejando Remy, luego de que cerro\n"
            "su restaurante en Paris por la pandemia.\n"
        )
        label = tk.Label(
            about_window,
            text=msg,
            bg="#222831",
            fg="#f1c40f",
            font=("Calibri", 16, "bold"),
            wraplength=580,
            justify="center"
        )
        label.pack(expand=True, fill="both", padx=20, pady=(30,10))

        btn_frame = tk.Frame(about_window, bg="#222831")
        btn_frame.pack(pady=(0, 20))

        def close_about():
            about_window.destroy()

        btn1 = tk.Button(
            btn_frame,
            text="Por supuesto",
            command=close_about,
            bg="#27ae60",
            fg="white",
            font=("Calibri", 12, "bold"),
            width=16
        )
        btn1.pack(side="left", padx=10)

        btn2 = tk.Button(
            btn_frame,
            text="Conseguite un empleo honesto",
            command=close_about,
            bg="#e74c3c",
            fg="white",
            font=("Calibri", 12, "bold"),
            width=24
        )
        btn2.pack(side="left", padx=10)

    def display_employees(self):
        # Limpia la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Obtiene empleados y los muestra
        employees = self.service.get_all_employees()
        for emp in employees:
            self.tree.insert("", END, values=(emp.id, emp.name, emp.age, emp.doj, emp.email, emp.gender, emp.contact, emp.address))

    def get_data(self, event):
        selected_row = self.tree.focus()
        data = self.tree.item(selected_row)
        self.row = data["values"]
        if len(self.row) >= 8:
            self.name.set(self.row[1])
            self.age.set(self.row[2])
            self.doj.set(self.row[3])
            self.email.set(self.row[4])
            self.gender.set(self.row[5])
            self.contact.set(self.row[6])
            self.txt_address.delete(1.0, tk.END)
            self.txt_address.insert(tk.END, self.row[7])

    def add_employee(self):
        # Crea un objeto Employee con los datos del formulario
        employee = Employee(
            name=self.name.get(),
            age=self.age.get(),
            doj=self.doj.get(),
            email=self.email.get(),
            gender=self.gender.get(),
            contact=self.contact.get(),
            address=self.address.get()
        )
        self.service.add_employee(employee)
        self.display_employees()
        self.clear_fields()

    def update_employee(self):
        if not hasattr(self, "row") or not self.row:
            return
        employee = Employee(
            id=self.row[0],
            name=self.name.get(),
            age=self.age.get(),
            doj=self.doj.get(),
            email=self.email.get(),
            gender=self.gender.get(),
            contact=self.contact.get(),
            address=self.txt_address.get(1.0, tk.END).strip()
        )
        self.service.update_employee(employee)
        messagebox.showinfo("Success", "Record Updated")
        self.clear_fields()
        self.display_employees()

    def delete_employee(self):
        if not hasattr(self, "row") or not self.row:
            return
        self.service.delete_employee(self.row[0])
        self.clear_fields()
        self.display_employees()

    def clear_fields(self):
        self.name.set("")
        self.age.set("")
        self.doj.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.txt_address.delete(1.0, tk.END)
        self.row = None