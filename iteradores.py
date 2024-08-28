#Ejemplo de como funcionan los iteradores
#Crear una lista con algunos numeros
my_list = [1, 2, 3, 4]
#Obtener el iterador de la lista
#Un iterador se un objeto que nos permite recorrer una coleccion (como una lista uno por uno)
my_iter = iter(my_list)
#Usar el iterador para acceder a los elementos de la lista
#La funcion next() nos da el siguiente elemento en la coleccion cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))
#Iterar cadenas de texto usando un iterador
#Crear la cadena de texto
text = "Hola mundo"
#Crear un iterador para la cadena
#Un iterador nos permite recorrer cada caracter de una cadena uno por uno
iter_text = iter(text)
#Iterar sobre cada caracter de la cadena usando un bucle for
for char in iter_text:
    print(char)
#Crear un iterador que genere numeros impares desde 1 hasta el limite
#range(1, limit+1, 2) genera numeros comenzando en 1, con saltos de 2, hasta llegar a 9 (el limite no se incluye)
odd_iter = iter(range(1, 10, 2))
#usar el iterador para recorrer y mostrar cada numero impar generado
for num in odd_iter:
    print(num)
#Definir una funcion generadora
def my_generator():
    #La palabra clave yield nos permite retornar un valor y pausar la funcion en ese punto
    yield 1 #primer valor que se devuelve cuando se llama la funcion
    yield 2 #segundo valor que se devuelve cuando se llama la funcion
    yield 3 #tercer valor que se devuelve cuando se llama la funcion
#usar un bucle for para iterar sobre los valores generados
for value in my_generator():
    print(value)
#Fibonacci
#La serie de fibonacci hace referencia a que vamos a obtener un valor sumando los dos anteriores [0 1 1 2 3 5 8 13 ...]
def fibonacci(limit):
    #inicializar los dos primeros numeros de la secuencia de fibonacci
    a, b = 0, 1.
    #Continuar generando numeros mientras "a" sea menor que el limite
    while a < limit:
        yield a #Devolver el valor actual de "a" y pausar la ejecucion de la funcion
        a, b = b, a + b
    for num in fibonacci(10):
        print(num)