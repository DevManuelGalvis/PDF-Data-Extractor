# Importamos los módulos necesarios
from modules.preprocessor import preprocess_image, pdf_to_images_parallel
from modules.text_extractor import extract_text_from_image
from modules.table_extractor import extract_tables_from_pdf
from modules.utils import create_directories
import os
import time
from concurrent.futures import ThreadPoolExecutor  # Para procesamiento paralelo

# Función para procesar una imagen y extraer texto de ella
def process_image_and_extract_text(image_path, output_dir, extracted_texts_dir, page_number):
    try:
        # Tiempo inicial del procesamiento de la imagen
        start_time = time.time()

        # Preprocesar la imagen (mejorar calidad, binarización, etc.)
        processed_image_path = os.path.join(output_dir, f"processed_page_{page_number}.png")
        preprocess_image(image_path, processed_image_path)
        # print(f"Página {page_number}: Imagen procesada.")

        # Extraer texto de la imagen procesada utilizando OCR
        text_from_image = extract_text_from_image(processed_image_path)
        # Guardar el texto extraído en un archivo
        with open(os.path.join(extracted_texts_dir, f"text_from_image_page_{page_number}.txt"), "w", encoding="utf-8") as f:
            f.write(text_from_image)
        # print(f"Página {page_number}: Texto extraído.")

        # Tiempo final del procesamiento y duración
        end_time = time.time()
        print(f"Página {page_number}: Procesada en {end_time - start_time:.2f} segundos.")
    except Exception as e:
        # Manejo de errores en caso de fallos durante el procesamiento
        print(f"Error procesando la página {page_number}: {e}")

# Función principal que gestiona el flujo del programa
def main():
    # Tiempo total de inicio para medir la duración completa
    total_start_time = time.time()
    
    # Crear y configurar los directorios necesarios para la salida
    config = create_directories()
    extracted_texts_dir = config["extracted_texts"]  # Directorio para los textos extraídos
    extracted_tables_dir = config["extracted_tables"]  # Directorio para las tablas extraídas
    output_dir = config["output_dir"]  # Directorio para imágenes procesadas

    # Ruta del archivo PDF a procesar
    pdf_path = "ruta/al/archivo.pdf"


    # Convertir el PDF a imágenes de forma paralela
    print("Convirtiendo PDF a imágenes...")
    start_conversion_time = time.time()
    image_paths = pdf_to_images_parallel(pdf_path, output_dir, max_workers=4)
    end_conversion_time = time.time()
    print(f"Conversión de PDF a imágenes completada en {end_conversion_time - start_conversion_time:.2f} segundos.")

    # Verificar si se generaron imágenes
    if not image_paths:
        print("No se pudieron convertir páginas del PDF a imágenes.")
        return

    # Procesar las imágenes y extraer texto de forma paralela
    print("\nProcesando imágenes y extrayendo texto...")
    start_processing_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i, image_path in enumerate(image_paths):
            # Cada imagen se procesa en paralelo
            executor.submit(process_image_and_extract_text, image_path, output_dir, extracted_texts_dir, i + 1)
    end_processing_time = time.time()
    print(f"Procesamiento de imágenes y extracción de texto completado en {end_processing_time - start_processing_time:.2f} segundos.")

    # Extraer tablas directamente del PDF
    print("\nExtrayendo tablas del PDF...")
    start_table_extraction_time = time.time()
    try:
        extract_tables_from_pdf(pdf_path, extracted_tables_dir)
    except Exception as e:
        # Manejo de errores durante la extracción de tablas
        print(f"Error al extraer tablas del PDF: {e}")
    end_table_extraction_time = time.time()
    print(f"Extracción de tablas completada en {end_table_extraction_time - start_table_extraction_time:.2f} segundos.")

    # Tiempo total de ejecución
    total_end_time = time.time()
    print(f"\nTiempo total de ejecución: {total_end_time - total_start_time:.2f} segundos.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
