# # Funciones auxiliares.
import os

def create_directories():
    # os.makedirs("../PDF_Data_Extraction/outputs/extracted_texts", exist_ok=True)
    # os.makedirs("../PDF_Data_Extraction/outputs/extracted_tables", exist_ok=True)


    extracted_texts = "C:/Users/MANUEL GALVIS/OneDrive/Escritorio/TechProject/PDF_Data_Extraction/extracted_texts"
    extracted_tables = "C:/Users/MANUEL GALVIS/OneDrive/Escritorio/TechProject/PDF_Data_Extraction/extracted_tables"
    output_dir = "C:/Users/MANUEL GALVIS/OneDrive/Escritorio/TechProject/PDF_Data_Extraction/extracted_images"

    # Crear directorios
    os.makedirs(extracted_texts, exist_ok=True)
    os.makedirs(extracted_tables, exist_ok=True)

    return {
        "extracted_texts": extracted_texts,
        "extracted_tables": extracted_tables,
        "output_dir": output_dir
    }
