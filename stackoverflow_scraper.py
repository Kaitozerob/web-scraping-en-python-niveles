"""
📌 OBJETIVO:
Scrapear preguntas recientes de la página principal de StackOverflow, extrayendo información clave como el título, descripción, etiquetas, autor, reputación y fecha de publicación.

🧾 DESCRIPCIÓN:
Este script utiliza la biblioteca `BeautifulSoup` para parsear el HTML de StackOverflow y recolectar información útil de cada publicación en la sección de preguntas.
El diseño está modularizado con funciones reutilizables, facilitando su mantenimiento y escalabilidad para futuras mejoras como paginación, exportación de datos o análisis más profundo.

🔍 DATOS EXTRAÍDOS:
- Título de la pregunta
- Enlace directo
- Descripción/resumen
- Etiquetas (tags)
- Autor
- Reputación del autor
- Fecha de publicación

👤 AUTOR:
Joan Talizo Balbin
"""


import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, features="lxml")

# Funciones limpias
def extraer_texto(tag):
    return tag.text.strip() if tag else 'Sin dato'

def extraer_href(tag):
    return 'https://stackoverflow.com' + tag.get('href') if tag else 'Sin enlace'

def extraer_descripcion(pregunta):
    descripcion_tag = pregunta.select_one('div.s-post-summary--content-excerpt')
    return descripcion_tag.get_text(strip=True, separator=' ') if descripcion_tag else 'Sin descripción'

def extraer_autor_y_fecha(pregunta):
    autor_tag = pregunta.select_one('div.s-user-card--info a')
    fecha_tag = pregunta.select_one('time.s-user-card--time')

    autor = autor_tag.text.strip() if autor_tag else 'Anónimo'
    fecha = fecha_tag.text.strip() if fecha_tag else 'Fecha no disponible'

    return autor, fecha

def reputacion(pregunta):
    reputacion_tag = pregunta.select_one('div.s-user-card--info span')
    return reputacion_tag.text.strip() if reputacion_tag else 'Sin reputación'

# Recorremos preguntas
lista_de_preguntas = soup.select('div.s-post-summary')

for pregunta in lista_de_preguntas:
    titulo_tag = pregunta.select_one('h3 a')
    tags = pregunta.select('a.post-tag')

    titulo = extraer_texto(titulo_tag)
    link = extraer_href(titulo_tag)
    descripcion = extraer_descripcion(pregunta)
    etiquetas = [tag.text.strip() for tag in tags]
    autor, fecha = extraer_autor_y_fecha(pregunta)
    reputacion_usuario = reputacion(pregunta)

    print(f'Título: {titulo}')
    print(f'Link: {link}')
    print(f'Descripción: {descripcion}')
    print(f'Tags: {", ".join(etiquetas)}')
    print(f'Autor: {autor}')
    print(f'Reputación: {reputacion_usuario}')
    print(f'Fecha: {fecha}\n')
