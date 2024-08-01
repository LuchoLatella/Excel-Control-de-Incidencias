import pandas as pd
from tkinter import Tk, filedialog

# Crear una ventana de diálogo para seleccionar el archivo Excel
root = Tk()
root.withdraw()  # Ocultar la ventana principal de Tkinter
file_path = filedialog.askopenfilename(title="Selecciona un archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])

# Leer el archivo Excel
data = pd.read_excel(file_path)

# Mostrar los primeros 5 registros de los datos
print(data.head())

# Manipulación de datos (ejemplo: seleccionar solo una columna)
columna_seleccionada = data['Nombre_de_la_columna']

# Guardar los datos manipulados en un nuevo archivo Excel
data.to_excel('datos_modificados.xlsx', index=False)
