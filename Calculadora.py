from tkinter import *
from tkinter import ttk  
import math 

def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")
    
    estilos_label1.configure('Label1.TLabel',  background="#010924", foreground="white")
    estilos_label2.configure('Label2.TLabel',  background="#010924", foreground="white")
    
    estilos_botones_numeros.configure('Botones_numeros.TButton', background="#00044A",  foreground="white")
    estilos_botones_numeros.map('Botones_numeros.TButton',  background=[('active', '#020A90')])
    
    estilos_botones_borrar.configure('Botones_borrar.TButton', background="#010924", foreground="white")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active','#000AB1')])
    estilos_botones_restantes.configure('Botones_restantes.TButton', background="#010924", foreground="white")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active','#000AB1')])


def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")
    
    estilos_label1.configure('Label1.TLabel',background="#DBDBDB",foreground="black")
    estilos_label2.configure('Label2.TLabel',background="#DBDBDB",foreground="black")
    
    estilos_botones_numeros.configure('Botones_numeros.TButton',  background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map('Botones_numeros.TButton',  background=[('active', '#898989')])
    
    estilos_botones_borrar.configure('Botones_borrar.TButton', background="#CECECE", foreground="black")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])
    
    estilos_botones_restantes.configure('Botones_restantes.TButton', background="#CECECE", foreground="black")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

def ingresarValores(tecla):
    
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
        
    if tecla == 'x' or tecla == '÷' or tecla == '-' or tecla == '+':
        if tecla == 'x':
            entrada1.set(entrada2.get() + '*')
            entrada2.set('')
        elif tecla == '÷':
            entrada1.set(entrada2.get() + '/')  # Usamos ÷ en lugar de "/"
            entrada2.set('')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
            entrada2.set('')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
            entrada2.set('')
           
    if tecla ==   '=':
        entrada1.set(entrada1.get() + entrada2.get())   
        try:
            resultado = eval(entrada1.get())
            entrada2.set(resultado)
        except:
            entrada2.set('ERROR')

def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(event=""):
    inicio = 0
    final = len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:final-1])   
     
 
 
def borrarTodo():
    entrada1.set('')
    entrada2.set('')
        
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
