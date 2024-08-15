numbers = {1:"uno", 2:"dos", 3:"tres"} #en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre" : "Camilo",
               "apellidos" : "Zuniga",
               "estatura" : 1.73,
               "esta feliz" : True}
print(information)
# del information ["apellidos"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Camilo": {"Apellido": "Zuniga",
                        "Altura": 1.73,
                        "Edad": 24,
                        "Telefono": 3243594845,
                        "Signo zodiacal": "Tauro",
                        "Serie favorita": "Billy the kid",
                        "Cancion favorita": "Money trees - Kendrick lamar",
                        "Comida favorita": "Frijoles, sancocho",
                        "Lugar soñado vaciones": "Mexico",
                        "Habilidad secreta": "Entrenar hasta superarse",
                        "Pasatiempo":"Jugar futbol",
                        "Heroe o persona que admiras": "Endrick Moreira",
                        "Libro que mas me ha impactado": "Hagakure",
                        "Cenar con alguien": "Leicy Santos",
                        "Superpoder": "Visualizar el futuro",
                        "Que logro personal te enorgullese": "Mi habilidad",},
            "Javier":  {"Apellido": "Zuniga",
                        "Altura": 1.72,
                        "Edad": 46}}   
print(contacts)