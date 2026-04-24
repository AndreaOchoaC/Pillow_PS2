import sys
import os
from PIL import Image
from PIL import ImageDraw, ImageFont
from PIL import ImageFilter

# podemos importar imágenes o crearlas con la librería

img1 = Image.new("RGB", (100,100), color="red")
print("Objeto de tipo:", type(img1))

# Propiedades de la imagen
print("Tamaño:", img1.size)
print("Modo de color:", img1.mode)
#img1.show()---

# También podemos abrir imágenes desde nuestra computadora

# Definir las rutas de las carpetas de entrada y salida
input_folder = 'C:/Users/coach/Desktop/Python Start 2 AOC/Módulo 3 PIL'
output_folder = 'C:/Users/coach/Desktop/Python Start 2 AOC/Módulo 3 PIL/imgs_modificadas'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Busca las imágenes en la carpeta de entrada y las guarda en la carpeta de salida
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Construir la ruta completa de la imagen
        img_path = os.path.join(input_folder, filename) 

# ----- GUARDAR LAS IMÁGENES MODIFICADAS EN UNA CARPETA -----

# creamos una función "save_image" para guardar las imágenes modificadas en la carpeta de salida
# la usaremos para este ejercicio
# pero recordemos que normalmente se guardan con img.save("nombre_imagen.png")

def save_image(img, filename):
    save_path = os.path.join(output_folder, filename)
    img.save(save_path)
    print(f"Saved: {filename}")

# Abrir una imagen de la computadora
with Image.open("kuky_original.png") as border:
    border.show()
    
# ----- Edición de imágenes -----

# cambiar tamaño
img3 = Image.new("RGB", (100,100), color="blue")
img3_resized = img3.resize((50,50))

# rotar
border_rotar1 = border.rotate(45)

# aplicar filtros
border_grey = border.convert("L")
save_image(border_grey, "kuky_grey.png")

# como guía para las modificaciones, colocamos etiquetas en ciertas coordeanadas de la imagen
print("Tamaño de la imagen:", border.size) # (900, 1600)
img_etiquetas = border.copy()
# hacemos el texto más grande tamaño 20
font = ImageFont.truetype("arial.ttf", size=40)

text1 = ImageDraw.Draw(img_etiquetas)
text1.text((100,100), "100, 100", fill="blue", font=font)
text2 = ImageDraw.Draw(img_etiquetas)
text2.text((100,800), "100, 800", fill="blue", font=font)

text3 = ImageDraw.Draw(img_etiquetas)
text3.text((500, 100), "500, 100", fill="blue", font=font)
text4 = ImageDraw.Draw(img_etiquetas)
text4.text((500, 800), "500, 8800", fill="blue", font=font)

text5 = ImageDraw.Draw(img_etiquetas)
text5.text((100, 1400), "100, 1400", fill="blue", font=font)
text6 = ImageDraw.Draw(img_etiquetas)
text6.text((500, 1400), "500, 1400", fill="blue", font=font)

# también le ponemos un borde
borde = ImageDraw.Draw(img_etiquetas)
# dibujar rectangulo de borde alrededor de la imagen, especificando el ancho del borde
borde.rectangle([100, 100, 800, 1000], outline="red", width=8) # especificar [x, y, largo, ancho]

#img_etiquetas.show()
save_image(img_etiquetas, "kuky_etiquetas.png")
img_etiquetas.save("kuky_etiquetas.png")

# Cortar secciones de la imagen
left, top, right, bottom = 100, 100, 800, 1000 # definir la región a cortar
border_cropped = border.crop((left, top, right, bottom))
#border_cropped.show()
save_image(border_cropped, "kuky_cropped.png")

# Combinar/Pegar una imagen sobre otra

with Image.open("kuky_original.png") as border:
    border.show()

with Image.open("dino.jpg") as dino:
    dino.show()

fondo = border
top = dino.resize([500,500])

fondo.paste(top, (100,900)) # especificar la posición en donde se coloca
fondo.show()
save_image(fondo, "imgs_combinadas.png")

# Dibujar formas simples sobre una imagen
img_draw = Image.new("RGB", (120,60), color="white")
draw = ImageDraw.Draw(img_draw)
draw.rectangle([10,10,110,50], outline="black", width=2) # especificar [largo, ancho, x, y]
save_image(img_draw, "dibujo1.png")

# Agregar texto sobre la imagen
img_text = Image.new("RGB", (120,60), color="white")
text1 = ImageDraw.Draw(img_text)
text1.text((15,20), "¡Hola!", fill="blue")
save_image(img_text, "img_texto.png")

# Combinar dibujos y texto
img_draw2 = Image.new("RGB", (200,200), color="white")
draw2 = ImageDraw.Draw(img_draw2)
draw2.rectangle([10,10,110,50], outline="blue", width=2)
draw2.text((15,20), "Combinamos imágenesy texto", fill="green")
save_image(img_draw2, "img_dibujo_texto.png")

# ----- APLICAR FILTROS A LAS IMÁGENES -----

border_blur = border.filter(ImageFilter.BLUR)
save_image(border_blur, "kuky_blur.png")

# CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS

# ----- AGREGAR MARCA DE AGUA -----

'''img2 = Image.open("imagen.jpg")
img2.show()'''
