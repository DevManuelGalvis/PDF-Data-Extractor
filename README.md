# Herramienta de procesamiento de PDF y extracción de datos

Este proyecto es una herramienta para procesar archivos PDF y extraer contenido útil, como:

- Texto de las imágenes dentro de un PDF utilizando técnicas OCR.
- Tablas estructuradas y convertirlas a archivos CSV para análisis posterior.
- Imágenes procesadas para mejorar su calidad y realizar extracciones más precisas.

Es ideal para procesar documentos escaneados, reportes financieros, documentos técnicos y cualquier PDF con datos tabulares o imágenes.

## Estado del proyecto

Actualmente, la herramienta funciona desde la consola. Se está trabajando en el desarrollo de un sitio web para que cualquiera la pueda usar fácilmente desde su navegador.

## Tecnologías Utilizadas

Este proyecto utiliza las siguientes tecnologías y bibliotecas:

- **Python**: Lenguaje de programación principal.
- **OpenCV**: Para el preprocesamiento de imágenes (escalas de grises, binarización, etc.).
- **Pillow (PIL)**: Para manipular y abrir imágenes.
- **pytesseract**: Motor OCR basado en Tesseract para la extracción de texto.
- **pdfplumber**: Para extraer tablas y texto directamente desde PDFs.
- **pandas**: Para manejar datos tabulares y exportarlos como CSV.

## Requisitos Previos

- Python 3.8 o superior instalado en tu sistema.
- Instalar las dependencias necesarias desde requirements.txt:

```bash
pip install -r requirements.txt
```

- Tesseract OCR instalado y configurado en tu sistema.

## Cómo Usar

- Coloca el archivo PDF que deseas procesar en la raíz del proyecto.
- Modifica la ruta del PDF en el archivo **main.py**:

```python
pdf_path = "ruta/al/archivo.pdf"
```

- Ejecuta el script principal:
```bash
python main.py
```
