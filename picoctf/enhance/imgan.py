import tkimg_loader as tk  # Solo para recordar que usamos Tkinter
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os

def procesar_imagen():
    # 1. Pedir el nombre del archivo por consola
    nombre_archivo = input("Introduce el nombre de la imagen (ej: flag.png): ")
    
    # 2. Verificar si el archivo existe en el directorio actual
    if not os.path.exists(nombre_archivo):
        print(f"Error: No se encuentra el archivo '{nombre_archivo}' en esta carpeta.")
        return

    # 3. Configurar la ventana de Tkinter
    root = tk.Tk()
    root.title(f"Analizando: {nombre_archivo}")

    # Cargar la imagen original
    img_pil = Image.open(nombre_archivo).convert("RGB")
    
    # Guardamos una copia para manipular
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    def mostrar(img_para_mostrar):
        # Redimensionar visualmente sin perder el original
        temp_img = img_para_mostrar.copy()
        temp_img.thumbnail((800, 600))
        img_tk = ImageTk.PhotoImage(temp_img)
        canvas.image = img_tk  # Referencia para que no la borre el recolector de basura
        canvas.create_image(400, 300, image=img_tk)

    # --- BOTONES DE FILTROS ---
    btn_frame = tk.Frame(root)
    btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

    tk.Button(btn_frame, text="Original", command=lambda: mostrar(img_pil)).pack(side=tk.LEFT)
    tk.Button(btn_frame, text="Invertir", command=lambda: mostrar(ImageOps.invert(img_pil))).pack(side=tk.LEFT)
    
    # Filtro de Bit Plane (Extrae el bit menos significativo - LSB)
    def ver_lsb():
        # Este filtro resalta texto oculto en los bits más bajos
        pixel_data = img_pil.load()
        width, height = img_pil.size
        nueva_img = Image.new("RGB", (width, height))
        nueva_data = nueva_img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixel_data[x, y]
                # Si el bit es impar (1), pintamos blanco; si es par (0), negro
                res = 255 if (r & 1) else 0 
                nueva_data[x, y] = (res, res, res)
        mostrar(nueva_img)

    tk.Button(btn_frame, text="Ver LSB (Bit 0)", command=ver_lsb).pack(side=tk.LEFT)

    mostrar(img_pil)
    root.mainloop()

if __name__ == "__main__":
    procesar_imagen()
