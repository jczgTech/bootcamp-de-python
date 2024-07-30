# Esta es la estructura de un condicional:
#if condicion: # si esto es True
# Accion #la accion se ejecuta

#if false: #si esto es false
# Accion #la accion no se ejecuta

edad = 17
if edad >= 18: #los dos puntos los puedes leer como "le vamos a decir"
    print("Puedes pasar")
    
else:
    print("Eres menor de edad, no puedes pasar")
    
contrasena_almacenada = "JheysonGalvis"
contrasena_escrita = "JheysonGalvis"

if contrasena_almacenada == contrasena_escrita:
    print("hay coincidencia")
else:
    print("No hay coincidencia")