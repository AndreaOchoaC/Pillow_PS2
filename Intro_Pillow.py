import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# podemos importar imágenes o crearlas con la librería

img1 = Image.new("RGB", (100,100), color="blue")
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
# la usaremos para este ejercicio pero recordemos que normalmente se guardan con img.save("nombre_imagen.png")

def save_image(img, filename):
    save_path = os.path.join(output_folder, filename)
    img.save(save_path)
    print(f"Guardado: {filename}")

# Abrir una imagen de la computadora
with Image.open("kuky_original.png") as border:
    border.show()

'''try:
    img2 = Image.open("example.jpg")
    img2.show()
    print("Imagen existente")
except FileNotFoundError:
    print("No se encuentra la imagen")'''

# Guardar imágenes en distintos formatos

img1.save("red_image.png")
img1.save("img1_red.jpeg")
print("Se guardaron las imágenes.")

# ----- Edición de imágenes -----

border = Image.open("kuky_original.png") # imagen que usaremos en todas las ediciones

# cambiar tamaño
img3 = Image.new("RGB", (100,100), color="blue") # nueva imagen
img3_resized = img3.resize((50,50)) # imagen modificada
# img3_resized.show()

# podemos cambiarlo incluso sin conocer el tamaño original
size = border.size
new_size = (int(size[0]/5), int(size[1]/5))
border_resized = border.resize(new_size)
#border_resized.show()
save_image(border_resized, "pequenia.png")

# Rotar imágenes (en múltiplos de 45 grados)

border_rotar1 = border.rotate(45)
border_rotar2 = border.rotate(90)
border_rotar = border.rotate(120)
save_image(border_rotar, "kuky_rotar120.png")
save_image(border_rotar1, "kuky_rotar45.png")
save_image(border_rotar2, "kuky_rotar90.png")

# ----- Agregar texto y formas simples sbre la imagen -----

# Dibujos simples sobre una imagen
img_draw = Image.new("RGB", (120,60), color="white")
draw = ImageDraw.Draw(img_draw)
draw.rectangle([10,10,110,50], outline="black", width=2) # especificar [x1, y1, x2, y2]
save_image(img_draw, "dibujo1.png")

copia = border.copy()
rect1 = ImageDraw.Draw(copia)
rect1.rectangle([100, 900, 800, 1300], fill="blue", outline="black", width=8)
#copia.show()
save_image(copia, "kuky_rect_azul.png")

# Agregar texto sobre la imagen

# La fuente por defecto es de tamaño pequeño
font = ImageFont.truetype("arial.ttf", size=40) # hacemos el texto más grande y con fuente específica

img_text = Image.new("RGB", (120,60), color="white")
text1 = ImageDraw.Draw(img_text)
text1.text((15,20), "¡Hola!", fill="blue", font=font) # especificar coordenadas para colocarlo
save_image(img_text, "img_texto.png")

copia2 = border.copy()
copia_texto = ImageDraw.Draw(copia2)
# para poner texto muy largo usamos \n
copia_texto.text((500, 200), "Hola, me llamo Kuky \n Tengo 6 años \n Me gusta jugar con botellas de plástico ", fill="blue")
#copia2.show()
save_image(copia2, "kuky_texto.png")

# ----- Identificando las regiones de la imagen -----

# podemos colocar etiquetas en ciertas coordenadas de la imagen, como guía
print("Tamaño de la imagen:", border.size) # (900, 1600)
img_etiquetas = border.copy()

# Agregamos etiquetas en seis puntos de la imagen
text1 = ImageDraw.Draw(img_etiquetas)
text1.text((100,100), "100, 100", fill="blue", font=font)
text2 = ImageDraw.Draw(img_etiquetas)
text2.text((100,800), "100, 800", fill="blue", font=font)

text3 = ImageDraw.Draw(img_etiquetas)
text3.text((500, 100), "500, 100", fill="blue", font=font)
text4 = ImageDraw.Draw(img_etiquetas)
text4.text((500, 800), "500, 800", fill="blue", font=font)

text5 = ImageDraw.Draw(img_etiquetas)
text5.text((100, 1400), "100, 1400", fill="blue", font=font)
text6 = ImageDraw.Draw(img_etiquetas)
text6.text((500, 1400), "500, 1400", fill="blue", font=font)

# también le ponemos un borde
print("Tamaño de la imagen:", border.size) # (900, 1600)
borde = ImageDraw.Draw(img_etiquetas)
# dibujar rectangulo de borde alrededor de la imagen, especificando el ancho del borde
borde.rectangle([20, 20, 780, 1480], outline="red", width=8) # especificar [x1, y1, x2, y2]

# Guardar imagen con etiquetas + borde
save_image(img_etiquetas, "kuky_etiquetas.png")

# Cortar secciones de la imagen
left, top, right, bottom = 100, 100, 800, 1000 # definir la región a cortar
border_cropped = border.crop((left, top, right, bottom))
#border_cropped.show()
save_image(border_cropped, "kuky_cropped.png")

# Combinar/Pegar una imagen sobre otra

border = Image.open("kuky_original.png")
dino = Image.open("dino.jpg") 

fondo = border.copy()
top = dino.resize([500,500])

fondo.paste(top, (100,900)) # especificar la posición en donde se coloca
#fondo.show()
save_image(fondo, "kuky_dino1.png")

# Nota: Podemos crear stickers/emojis si la imagen "top" es transparente

fondo2 = border.copy()
fondo2 = fondo2.convert("RGBA")
dino_transp = Image.open("dino_transp.png")
dino_transp_rgba = dino_transp.convert("RGBA")
top2 = dino_transp_rgba.resize([400,400])
fondo2.paste(top2, (500, 1100), top2)
save_image(fondo2, "kuky_dino2.png")

# Combinar dibujos y texto
img_draw2 = Image.new("RGB", (200,200), color="white")
draw2 = ImageDraw.Draw(img_draw2)
draw2.rectangle([10,10,110,50], outline="blue", width=8)
draw2.text((15,20), "Combinamos imágenes y texto", fill="green")
save_image(img_draw2, "img_dibujo_texto.png")

# Combinar texto y stickers
img_texto_sticker = border.copy()
draw_kuky = ImageDraw.Draw(img_texto_sticker)
draw_kuky.rectangle([400, 1000, 800, 1400], outline="black", fill="green")
draw_kuky.text((500, 900), "Hola", fill="blue", font=font)
#img_texto_sticker.show()
save_image(img_texto_sticker, "kuky_texto_sticker.png")

exit()
# ----- APLICAR FILTROS A LAS IMÁGENES -----

border_grey = border.convert("L") # escala de grises
save_image(border_grey, "kuky_grey.png")

border_blur = border.filter(ImageFilter.BLUR) # borrosa
save_image(border_blur, "kuky_blur.png")

border_contornos = border.filter(ImageFilter.CONTOUR) # contornos --efecto lápiz
save_image(border_contornos, "kuky_contornos.png")

border_details = border.filter(ImageFilter.DETAIL) # ilumina los detalles de la imagen
save_image(border_details, "kuky_details.png")

border_edges = border.filter(ImageFilter.EDGE_ENHANCE) # hace énfasis en los bordes
save_image(border_edges, "kuky_edges.png")

border_sombras = border.filter(ImageFilter.EMBOSS) # sombras y luces
save_image(border_sombras, "kuky_sombras.png")

# ----- AGREGAR MARCA DE AGUA -----

'''img2 = Image.open("imagen.jpg")
img2.show()'''
