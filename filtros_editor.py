# Se debe poner en un nuevo archivo
from PIL import Image, ImageOps, ImageEnhance

def apply_grayscale(image):
    return ImageOps.grayscale(image).convert("RGB")

def apply_invert(image):
    return ImageOps.invert(image)

def apply_sepia(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            transform_red   = int(0.393*r + 0.769*g + 0.189*b)
            transform_green = int(0.349*r + 0.686*g + 0.168*b)
            transform_blue  = int(0.272*r + 0.534*g + 0.131*b)
            pixels[x, y] = (min(255, transform_red),
                            min(255, transform_green),
                            min(255, transform_blue))
    return image

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)
    
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)
