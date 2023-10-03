#!/Users/dinog/source/repos/proyecto04Python
# -*- coding: latin-1 -*-
import os, sys
import tkinter as TK
from tkinter import messagebox


def limpiar_campos():
    entry_nombres.delete(0, TK.END)
    entry_apellidos.delete(0, TK.END)
    entry_edad.delete(0, TK.END)
    entry_estatura.delete(0, TK.END)
    entry_Telefono.delete(0, TK.END)
    var_genero.set(0)
    

def borrar_datos():
    limpiar_campos()

def guardar_datos():
    nombre=entry_nombres.get()
    apellidos=entry_apellidos.get()
    edad=entry_edad.get()
    estatura=entry_estatura.get()
    telefono=entry_Telefono.get()
    
    #obtener gebero seleccionado
    genero=""
    if var_genero.get()==1:
        genero="hombre"
    elif var_genero.get()==2:
        genero="mujer"
        
    #crear cadena de datos
    datos= f"Nombres:{nombre}\nApellidos:{apellidos}\nEdad:{edad} años\nEstatura:{estatura} m\nTelefono:{telefono} \nGenero:{genero}"


    with open("datos99.txt","a") as archivo:
        archivo.write(datos+"\n\n")
        
    #Mostrar mensaje
    messagebox.showinfo("Informacion", "Datos guardados con exito:\n\n"+ datos)
    

    #Resetear
    entry_nombres.delete(0, TK.END)
    entry_apellidos.delete(0, TK.END)
    entry_edad.delete(0, TK.END)
    entry_estatura.delete(0, TK.END)
    entry_Telefono.delete(0, TK.END)
    var_genero.set(0)
    
#crear la ventana principal
Pantalla =TK.Tk()
Pantalla.title("Formulario")

#Crear variable para los radiobutton
var_genero=TK.IntVar()

#crear etiquetas y campos de entrada
lbl_nombres=TK.Label(Pantalla, text="Nombre").pack()

entry_nombres=TK.Entry(Pantalla)
entry_nombres.pack()

lbl_apellidos=TK.Label(Pantalla, text="Apellidos").pack()
entry_apellidos=TK.Entry(Pantalla)
entry_apellidos.pack()

lbl_edad=TK.Label(Pantalla, text="Edad").pack()
entry_edad=TK.Entry(Pantalla)
entry_edad.pack()

lbl_estatura=TK.Label(Pantalla, text="Estatura").pack()
entry_estatura=TK.Entry(Pantalla)
entry_estatura.pack()

lbl_Telefono=TK.Label(Pantalla, text="Telefono").pack()
entry_Telefono=TK.Entry(Pantalla)
entry_Telefono.pack()

lbl_genero=TK.Label(Pantalla, text="Genero").pack()

rb_hombre=TK.Radiobutton(Pantalla, text="Hombre", variable=var_genero, value=1)
rb_hombre.pack()
rb_mujer=TK.Radiobutton(Pantalla, text="Mujer", variable=var_genero, value=2)
rb_mujer.pack()

#Boton para guardar datos

btn_guardar=TK.Button(Pantalla, text="Guardar", command= guardar_datos)
btn_guardar.pack()

#boton para borrar datos
btn_borrar=TK.Button(Pantalla, text="Borrar campos", command= borrar_datos).pack()

#Inicial la aplicacion
Pantalla.mainloop()


