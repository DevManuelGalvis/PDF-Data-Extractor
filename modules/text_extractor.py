# Importamos las bibliotecas necesarias
from PIL import Image  # Biblioteca para manipulación de imágenes
import pytesseract  # Biblioteca para reconocimiento óptico de caracteres (OCR)

# Función para extraer texto de una imagen
def extract_text_from_image(image_path):
    """
    Extrae texto de una imagen usando Tesseract OCR.

    Args:
        image_path (str): Ruta de la imagen desde la que se extraerá el texto.

    Returns:
        str: Texto extraído de la imagen. En caso de error, devuelve una cadena vacía.
    """
    try:
        # Abre la imagen desde la ruta especificada
        image = Image.open(image_path)
        
        # Extrae el texto de la imagen usando Tesseract OCR
        # - "lang='spa'" indica que el idioma utilizado para la detección es español.
        # - "config='--psm 6'" establece el modo de segmentación de páginas. Aquí, el modo 6 trata de detectar un bloque uniforme de texto.
        return pytesseract.image_to_string(image, lang="spa", config="--psm 6")
    
    except Exception as e:
        # Manejo de errores si ocurre un problema al abrir o procesar la imagen
        print(f"Error al extraer texto de la imagen {image_path}: {e}")
        return ""  # Devuelve una cadena vacía en caso de error
