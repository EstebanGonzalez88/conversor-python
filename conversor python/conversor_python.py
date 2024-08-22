#20/08/2024
#import tkinter as tk
#def Farenheint_celsius():
#    farenheint = float(txtFar.get())
#    celsius = (farenheint-32)*5.0/9.0
#    txtCelsius.delete(0,tk.END)
#    txtCel.insert(0, celsius)    
#ventana=tk.Tk()
#ventana.title("Act03 - Conversor de temperatura")
from cProfile import label
from distutils.util import convert_path
import tkinter as tk
def rest():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")
    
def covert_fahrenheit():
    celsius = float (entry2.get())
    fahrenheit = (celsius * 9/5) +32
    entry1.delete(0, tk.END)
    entry1.insert(0, f"{fahrenheit:.2f}")
    
def convert_celsius():
    fahrenheit = float (entry1.get())
    celsius = (fahrenheit -32)*5.0 /9.0
    entry2.delete(0, tk.END)
    entry2.insert(0, f"{celsius:.2f}")
    
app = tk.Tk()
app.title("==conversor de temperatura de Esteban==")

label1 = tk.Label(app, text="FAHRENHEIT: ")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text= "CONVERTIR TO CELSIUS", command=convert_celsius)
button1.grid(row=0, column =2)

label2 = tk.Label(app, text="CELSIUS")
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

buton2 = tk.Button(app, text= "CONVERTIR A FAHRENHEIT", command=covert_fahrenheit)
buton2.grid(row=1, column=2)

button3 = tk.Button(app, text="RESTABLECER VALORES", command=rest)
button3.grid(row=2, column=1)

app.mainloop()