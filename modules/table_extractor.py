#  Extrae tablas de los PDFs.

# Importamos las bibliotecas necesarias
import pdfplumber  # Biblioteca para trabajar con PDFs y extraer contenido estructurado
import pandas as pd  # Biblioteca para manipulación y exportación de datos en formato tabular

# Función para extraer tablas de un archivo PDF
def extract_tables_from_pdf(pdf_path, output_dir):
    """
    Extrae tablas de un archivo PDF y las guarda como archivos CSV.

    Args:
        pdf_path (str): Ruta del archivo PDF desde el cual se extraerán las tablas.
        output_dir (str): Directorio donde se guardarán los archivos CSV generados.

    Returns:
        list: Lista de rutas de los archivos CSV generados.
    """
    # Lista para almacenar las rutas de las tablas exportadas
    tables = []
    
    # Abre el archivo PDF usando pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Itera a través de cada página del PDF
        for page_number, page in enumerate(pdf.pages):
            # Extrae todas las tablas presentes en la página actual
            page_tables = page.extract_tables()
            
            # Procesa cada tabla extraída
            for idx, table in enumerate(page_tables):
                # Convierte la tabla en un DataFrame de pandas
                df = pd.DataFrame(table)
                
                # Define la ruta de salida para el archivo CSV de la tabla
                output_path = f"{output_dir}/table_page_{page_number + 1}_{idx + 1}.csv"
                
                # Guarda el DataFrame como un archivo CSV
                df.to_csv(output_path, index=False)
                
                # Agrega la ruta del archivo CSV generado a la lista
                tables.append(output_path)
    
    # Devuelve la lista de rutas de las tablas exportadas
    return tables
