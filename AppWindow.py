from tkinter import colorchooser

import customtkinter as ctk
import tkinter as tk
from Controller import Controller

from app.HorarioIU import HorarioIU
ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")
class AppWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("1200x700")
        self.resizable(False,False)
        self.update_idletasks()
        self.color = "red"
        self.objetos =[]

        #fondo frame principal
        self.main_frame = ctk.CTkFrame(self,width=1200,height=650, fg_color="white")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1,weight=3)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        #frame de opciones y aqui estara la seleccion de materias
        self.options_frame = ctk.CTkFrame(self.main_frame, width=400,height=450) #, fg_color="#ffff89"
        self.options_frame.grid(row=1, column=0, sticky=tk.NSEW, ipadx=10, ipady=10)
        self.options_frame.columnconfigure(0,weight=2)
        
        self.label = ctk.CTkLabel(self.options_frame, text="AGENTES IA")
        self.label.grid(row=0, column=0, sticky=tk.NSEW)


        #frame de horario donde se mostrara el horario
        self.horario_frame = ctk.CTkFrame(self.main_frame, width=800,height=450, fg_color="blue")
        self.horario_frame.grid(row=1, column=1, sticky=tk.NSEW, ipadx=10, ipady=10) 
        self.horario_frame.columnconfigure(0,weight=2)

        #tabla de horario
        self.table_labels = []
        self.table_horizontal_labels = [
            'Lunes', 
            'Martes', 
            'Miercoles', 
            'Jueves', 
            'Viernes', 
            'Sabado'
        ]
        self.table_vertical_labels = [
            '6:45 - 8:15', 
            '8:15 - 9:45', 
            '9:45 - 11:15', 
            '11:15 - 12:45', 
            '12:45 - 14:15',
            '14:15 - 15:45',
            '15:45 - 17:15',
            '17:15 - 18:45',
            '18:45 - 20:15',
            '20:15 - 21:45'
        ]
        for i in range(len(self.table_vertical_labels)):
            row_labels = []
            for j in range(len(self.table_horizontal_labels)):
                label = ctk.CTkLabel(self.horario_frame, text=f"Row {i+1}, Col {j+1}", fg_color="white", bg_color="black")
                label.grid(row=i, column=j, padx=5, pady=5)
                row_labels.append(label)
            self.table_labels.append(row_labels)
       







        

        
        

if __name__ == "__main__":
    app = AppWindow()
    ctr = Controller(app)
