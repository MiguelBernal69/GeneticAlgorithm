import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
import customtkinter as ctk
import tkinter as tk
from PyQt5 import sip

class Prueba(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("1200x700")
        self.resizable(False,False)
        self.update_idletasks()
        self.color = "red"
        self.objetos = []

        #fondo frame principal
        self.main_frame = ctk.CTkFrame(self,width=1200,height=650, fg_color="white")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1,weight=3)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Crear un widget secundario de QWidget de PyQt5 para contener la tabla
        self.qt_widget_container = QWidget()

        # Crear la tabla de PyQt5
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        for i in range(5):
            for j in range(3):
                item = QTableWidgetItem(f"Row {i+1}, Column {j+1}")
                self.table.setItem(i, j, item)

        # Configurar el layout de la ventana de PyQt5
        layout = QVBoxLayout(self.qt_widget_container)
        layout.addWidget(self.table)
        self.qt_widget_container.setLayout(layout)

        # Obtener el identificador de la ventana de la aplicación principal de tkinter
        self.app_window_id = self.main_frame.winfo_id()

        # Obtener el identificador de la ventana de PyQt5
        self.qt_widget_id = sip.unwrapinstance(self.qt_widget_container.winId())

        # Cambiar el padre de la ventana de PyQt5 para que sea la ventana principal de tkinter
        self.table.setParent(self.app_window_id)

        # Mostrar la ventana principal de la aplicación de PyQt5
        self.qt_widget_container.show()

if __name__ == '__main__':
    # Crear una instancia de QApplication antes de crear cualquier widget de PyQt5
    app_qt = QApplication(sys.argv)
    
    # Crear una instancia de la aplicación
    app = Prueba()
    
    # Ejecutar el bucle de eventos de la aplicación de PyQt5
    sys.exit(app_qt.exec_())
