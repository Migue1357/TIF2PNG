import os
from pathlib import Path
from tifffile import imread
from PIL import Image
from tkinter import Tk, filedialog

# Abrir ventana para elegir carpeta
Tk().withdraw()  # Oculta la ventana principal de tkinter
folder_selected = filedialog.askdirectory(title="Selecciona la carpeta con las imágenes TIFF")

if not folder_selected:
    print("No se seleccionó ninguna carpeta. Saliendo.")
    exit()

# Usar la carpeta seleccionada
input_folder = Path(folder_selected)
output_folder = input_folder / "PNG_Convertidas"
output_folder.mkdir(exist_ok=True)

# Buscar todos los archivos .tif o .tiff
tif_files = list(input_folder.glob("*.tif")) + list(input_folder.glob("*.tiff"))

print(f"Se encontraron {len(tif_files)} archivos TIFF.")

for tif_file in tif_files:
    try:
        # Leer la imagen
        img = imread(tif_file)

        # Si la imagen es de un solo canal (grayscale), asegúrate de convertir bien
        if img.ndim == 2:
            img_pil = Image.fromarray(img)
        elif img.ndim == 3:
            # Si es multicanal pero compatible (por ejemplo RGB), usa directamente
            img_pil = Image.fromarray(img[:, :, :3])
        else:
            print(f"⚠️ No se pudo procesar {tif_file.name}: dimensión no compatible.")
            continue

        # Guardar como PNG
        output_file = output_folder / f"{tif_file.stem}.png"
        img_pil.save(output_file)

        print(f"✅ {tif_file.name} → {output_file.name}")

    except Exception as e:
        print(f"❌ Error con {tif_file.name}: {e}")
