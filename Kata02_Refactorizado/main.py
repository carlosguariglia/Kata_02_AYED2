from tkinter import Tk
from app.gui.employee_gui import EmployeeGUI

if __name__ == "__main__":
    root = Tk()
    app = EmployeeGUI(root)
    root.mainloop()