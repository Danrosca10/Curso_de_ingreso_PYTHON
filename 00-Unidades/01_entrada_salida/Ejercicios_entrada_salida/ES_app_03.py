import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Danilo 
apellido: Scapicchi
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto para luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Me quedo con vos")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        me_quedo_con_vos = self.txt_nombre.get()
        me_quedo_con_vos = "me quedo con vos" + me_quedo_con_vos
        alert(title="ciudad magica", message="voy a buscarte qué noche mágica ciudad de Buenos Aires") 

                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()