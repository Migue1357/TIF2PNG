# TIF2PNG
Este script en Python permite convertir de forma automática imágenes en formato TIFF (.tif o .tiff) a PNG.

Aplicación sencilla en Python para convertir imágenes TIFF (.tif, .tiff) a formato PNG mediante una interfaz gráfica para seleccionar la carpeta origen.

## 🔧 Requisitos

- Python ≥ 3.10
- tifffile
- Pillow
- tkinter (usually included with standard Python distributions)

Para instalar las librerías necesarias, ejecuta en tu terminal (bash, PowerShell o CMD):

```bash
pip install tifffile
```
```bash
pip install Pillow
```
```bash
pip install tkinter
```
## Descripción del script

El script abre una ventana típica de selección de carpeta para que el usuario elija la ubicación donde están las imágenes TIFF. Luego:

- Busca todas las imágenes con extensión .tif y .tiff.

- Convierte cada imagen a formato PNG.

- Guarda las imágenes convertidas en una subcarpeta llamada PNG_Convertidas.

- Muestra en consola el progreso y posibles errores durante la conversión.

- Soporta imágenes en escala de grises y RGB.

## Cómo usarlo

1. Descarga y ejecuta el script en tu terminal o entorno Python:

```bash
python TIF2PNG.py
```

2. Se abrirá una ventana para seleccionar la carpeta que contiene las imágenes TIFF.

3. El script realizará la conversión y guardará las imágenes PNG en la carpeta PNG_Convertidas dentro de la carpeta seleccionada.

## Contacto

Para dudas o sugerencias, puedes abrir un issue en este repositorio.

## Licencia

Este proyecto está bajo licencia MIT. Puedes usarlo y modificarlo libremente siempre que incluyas el aviso de derechos de autor incluido en LICENSE en todas las copias o porciones sustanciales del Software.
