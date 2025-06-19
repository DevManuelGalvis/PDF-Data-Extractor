import os

def create_directories(base_dir="outputs"):
    extracted_texts = os.path.join(base_dir, "extracted_texts")
    extracted_tables = os.path.join(base_dir, "extracted_tables")
    output_dir = os.path.join(base_dir, "extracted_images")

    # Crear directorios
    os.makedirs(extracted_texts, exist_ok=True)
    os.makedirs(extracted_tables, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    return {
        "extracted_texts": extracted_texts,
        "extracted_tables": extracted_tables,
        "output_dir": output_dir
    }