import numpy as np

def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
    return datos

if __name__ == "__main__":
    ruta_archivo = 'https://github.com/hypatiagarcia/retail-sales-analysis/blob/main/data/retail_sales_dataset.csv'
    datos = cargar_datos(ruta_archivo)
    print(datos)
