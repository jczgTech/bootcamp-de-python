ingreso_mensual = 12000
ahorro_mensual = 6000

if ingreso_mensual > 10000:
    if ahorro_mensual < 7000:
        print("Ahora si estas bien")
    else:
        print("estas gastando mucho, ahorra mas")
    
elif ingreso_mensual > 1000:
    print("estas bien en cualquier parte del mundo")

elif ingreso_mensual > 500:
    print("estas bien en colombia")
    
elif ingreso_mensual > 200:
    print("estas bien en peru")
    
else:
    print("estas en la pobreza")