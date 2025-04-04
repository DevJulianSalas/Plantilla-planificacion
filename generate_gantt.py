from lxml import etree
from datetime import datetime, timedelta
import zipfile
import os

# Crear estructura base del archivo .gan (archivo XML comprimido tipo zip)
project_name = "Proyecto BCI"
start_date = datetime(2025, 4, 5)

# Definición de tareas con nombre, duración en días y dependencias
tareas = [
    # Etapa 1 - Formación técnica
    {"id": 1, "name": "1.1 Estudio del estado del arte", "duration": 5, "dependencies": []},
    {"id": 2, "name": "1.2 Capacitación en señales EEG", "duration": 5, "dependencies": []},
    {"id": 3, "name": "1.3 Capacitación en BCI", "duration": 5, "dependencies": []},
    {"id": 4, "name": "1.4 Capacitación en AWS", "duration": 3, "dependencies": [1, 2, 3]},

    # Etapa 2 - Preparación de los datos
    {"id": 5, "name": "2.1 Búsqueda de fuentes", "duration": 1, "dependencies": [4]},
    {"id": 6, "name": "2.2 Implementación descarga de datos", "duration": 1, "dependencies": [5]},
    {"id": 7, "name": "2.3 Preparación de datos", "duration": 2, "dependencies": [6]},

    # Etapa 3 - Implementación de modelos
    {"id": 8, "name": "3.1 Bibliografía modelo 1", "duration": 2, "dependencies": [7]},
    {"id": 9, "name": "3.2 Implementación modelo 1", "duration": 5, "dependencies": [8]},
    {"id": 10, "name": "3.3 Bibliografía modelo 2", "duration": 2, "dependencies": [7]},
    {"id": 11, "name": "3.4 Implementación modelo 2", "duration": 5, "dependencies": [10]},
    {"id": 12, "name": "3.5 Bibliografía modelo 3", "duration": 2, "dependencies": [7]},
    {"id": 13, "name": "3.6 Implementación modelo 3", "duration": 5, "dependencies": [12]},
    {"id": 14, "name": "3.7 Análisis de modelos", "duration": 2, "dependencies": [9, 11, 13]},
    {"id": 15, "name": "3.8 Selección del mejor modelo", "duration": 1, "dependencies": [14]},
]

# Crear estructura XML
project = etree.Element("project")
tasks_elem = etree.SubElement(project, "tasks")

for tarea in tareas:
    task_elem = etree.SubElement(tasks_elem, "task", 
                                 id=str(tarea["id"]), 
                                 name=tarea["name"], 
                                 start=start_date.strftime("%Y-%m-%d"),
                                 duration=str(tarea["duration"]))

    for dep_id in tarea["dependencies"]:
        etree.SubElement(task_elem, "depend", id=str(dep_id))

# Guardar XML temporal
xml_path = "./project.xml"
with open(xml_path, "wb") as f:
    f.write(etree.tostring(project, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

# Convertir a formato .gan (zip con contenido XML)
gan_path = "./Proyecto_BCI.gan"
with zipfile.ZipFile(gan_path, "w") as zipf:
    zipf.write(xml_path, arcname="project.xml")