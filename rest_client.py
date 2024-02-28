import requests

url = "http://localhost:8000/"


ruta_post_agrega_estudiante = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_agrega_estudiante_response = requests.post(
    ruta_post_agrega_estudiante, json=nuevo_estudiante
)
print("POST /agrega_estudiante:", post_agrega_estudiante_response.json())

ruta_get_lista_estudiantes = url + "lista_estudiantes"
get_lista_estudiantes_response = requests.get(ruta_get_lista_estudiantes)
print("GET /lista_estudiantes:", get_lista_estudiantes_response.json())


ruta_get_buscar_nombre = url + "buscar_nombre"
get_buscar_nombre_response = requests.get(ruta_get_buscar_nombre)
print("GET /buscar_nombre:", get_buscar_nombre_response.json())


ruta_get_contar_carreras = url + "contar_carreras"
get_contar_carreras_response = requests.get(ruta_get_contar_carreras)
print("GET /contar_carreras:", get_contar_carreras_response.json())


ruta_get_total_estudiantes = url + "total_estudiantes"
get_total_estudiantes_response = requests.get(ruta_get_total_estudiantes)
print("GET /total_estudiantes:", get_total_estudiantes_response.json())

