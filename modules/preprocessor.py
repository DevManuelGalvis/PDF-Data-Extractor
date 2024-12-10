#  Se encarga de mejorar la calidad de las imágenes.

# Importamos las bibliotecas necesarias
import cv2  # OpenCV para procesamiento de imágenes
import os  # Para manejar rutas y archivos
from pdf2image import convert_from_path, exceptions  # Para convertir PDF a imágenes
from concurrent.futures import ThreadPoolExecutor  # Para procesamiento paralelo
import time  # Para medir tiempos de ejecución

# Preprocesa una imagen mejorando su calidad
def preprocess_image(input_path, output_path):
    """
    Preprocesa una imagen convirtiéndola a escala de grises y aplicando un umbral binario.
    Esto mejora la calidad para la extracción de texto o procesamiento posterior.
    """
    # Verifica que el archivo de entrada exista
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"El archivo no existe: {input_path}")
    
    # Lee la imagen en escala de grises
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"No se pudo leer el archivo: {input_path}")
    
    # Aplicar un umbral binario para mejorar el contraste de la imagen
    _, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    # Guardar la imagen procesada en la ruta de salida
    cv2.imwrite(output_path, thresh_image)
    # print(f"Imagen procesada guardada en: {output_path}")

# Procesa una sola página de un PDF y la convierte a imagen
def process_single_page(page, page_number, output_dir):

    # Inicia el temporizador para medir el tiempo de procesamiento de esta página
    start_time = time.time()
    
    # Define la ruta de salida para la imagen
    output_path = os.path.join(output_dir, f"page_{page_number}.png")
    
    # Guarda la página como una imagen PNG
    page.save(output_path, "PNG")
    
    # Calcula el tiempo transcurrido y lo imprime
    end_time = time.time()
    print(f"Página {page_number} generada en {end_time - start_time:.2f} segundos.")
    
    return output_path

# Convierte un PDF a una lista de imágenes de forma paralela
def pdf_to_images_parallel(pdf_path, output_dir, max_workers=4):
    """
    Convierte un archivo PDF en una lista de imágenes, procesando páginas en paralelo para mayor eficiencia.
    """
    # Verifica que el archivo PDF de entrada exista
    if not os.path.exists(pdf_path):
        print(f"Error: El archivo PDF no existe: {pdf_path}")
        return []

    # Crea el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Inicia el temporizador total para medir el tiempo completo de conversión
        total_start_time = time.time()
        
        # Convierte todas las páginas del PDF a una lista de imágenes
        print("Iniciando la conversión de PDF a imágenes...")
        pages = convert_from_path(pdf_path, dpi=150)  # dpi define la calidad de las imágenes generadas
        
        image_paths = []  # Lista para almacenar las rutas de las imágenes generadas
        
        # Utiliza un ThreadPoolExecutor para procesar las páginas en paralelo
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Crea tareas para cada página
            futures = [
                executor.submit(process_single_page, page, i + 1, output_dir)
                for i, page in enumerate(pages)
            ]
            
            # Recupera los resultados de cada tarea
            for future in futures:
                image_paths.append(future.result())

        # Calcula el tiempo total y lo imprime
        total_end_time = time.time()
        print(f"Conversión completa de PDF a imágenes en {total_end_time - total_start_time:.2f} segundos.")
        
        return image_paths  # Devuelve la lista de rutas de imágenes generadas
    
    except exceptions.PDFException as e:
        # Manejo de errores durante la conversión
        print(f"Error al convertir PDF a imágenes: {e}")
        return []
