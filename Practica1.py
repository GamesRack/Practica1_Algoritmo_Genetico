import random  # Importamos random para la generacion aleatoria

# Definimos la lista de productos, cada uno siendo un diccionario con los
# datos de nombre, peso y precio y se cuentan desde la posicion 0 hasta el 6

productos=[
    {'nombre': 'Decoy Detonators', 'peso': 4, 'precio': 10},
    {'nombre': 'Fever Fudge', 'peso': 2, 'precio': 3},
    {'nombre': 'Love Potion', 'peso': 2, 'precio': 8},
    {'nombre': 'Puking Pastilles', 'peso': 1.5, 'precio': 2},
    {'nombre': 'Extendable Ears', 'peso': 5, 'precio': 12},
    {'nombre': 'Nosebleed Nougat', 'peso': 1, 'precio': 2},
    {'nombre': 'Skiving Snackbox', 'peso': 5, 'precio': 6},
]

# Definimos parametros
capacidad_maxima = 30   # Peso maximo
tamano_poblacion = 10   # Individuos en la poblacion inicial

# Guardamos las posiciones de los productos con restriccion para
# llevar un mejor control en caso de cambios en la lista y para facilitar
# la legibilidad del codigo
posicion_love_potion = 2
posicion_skiving_snackbox = 6

# Crea un individuo de 7 numeros que representan la cantidad de x producto en la mochila
# Este individuo representa una posible solucion
def creacion_individuo():
    # Iniciamos al individuo como una lista de ceros, con una posicion por producto
    # Tambien empezamos con un peso en mochila de 0
    individuo = [0]*len(productos)
    peso_actual = 0

    # Nos hacemos cargo de las restricciones y actualizamos el peso de la mochila
    # agregando la suma de las restricciones
    individuo[posicion_love_potion] = 3
    peso_actual += productos[posicion_love_potion]['peso']*3

    individuo[posicion_skiving_snackbox] = 2
    peso_actual += productos[posicion_skiving_snackbox]['peso']*2

    # Despues llenamos el resto de la mochila al azar, creando una lista con las
    # posiciones del resto de productos
    posiciones_productos = list(range(len(productos)))
    random.shuffle(posiciones_productos)    # El orden de adicion de los productos tambien se hara de forma aleatoria

    # Cuando ya se haya asignado su posicion, empezamos a agregar productos
    for i in posiciones_productos:
        # Revisamos si al menos uno del producto actual entra en la mochila
        if peso_actual + productos[i]['peso']<=capacidad_maxima:
            # Calculamos el maximo de este producto que aun puede caber en el espacio que queda
            agregar_producto = int((capacidad_maxima - peso_actual) // productos[i]['peso'])
            # Revisamos cuantos de ese producto tenemos disponible
            productos_disponible = 10 - individuo[i]
            # Calculamos el limite real, que sera el valor mas pequeno entre lo que cabe y lo que hay disponible
            limitar_producto = min(agregar_producto, productos_disponible)

            # si al menos podemos meter uno del producto:
            if limitar_producto > 0:
                # Se elegira una cantidad del producto al azar de entre 1 y el limite real
                cantidad_azar = random.randint(1, limitar_producto)
                # Sumaremos esta cantidad a nuestro individuo
                individuo[i] += cantidad_azar
                # Y actualizaremos el peso de la mochila
                peso_actual += productos[i]['peso']*cantidad_azar

    return individuo

# Genera nuestra poblacion incial de 10 individuos
def generar_poblacion():
    poblacion = [] # Empezamos con una lista vacia donde ira nuestra poblacion
    for _ in range(tamano_poblacion): # La creacion de individuos se repetira tantas veces como lo hayamos indicado (10 veces)
        poblacion.append(creacion_individuo()) # Y en cada repeticion un nuevo individuo se agrega a la lista de poblacion
    
    return poblacion

# Se calcula la ganancia de cada individuo sumando el precio total de sus productos
def calcular_aptitud(individuo):
    aptitud_total = 0       # Empezamos con una aptitud de 0
    for i in range(len(individuo)):
        # Se multiplica la cantidad de cada producto por su precio y se suma al total
        cantidad = individuo[i]
        precio = productos[i]['precio']
        aptitud_total += cantidad*precio
    
    return aptitud_total

poblacion_inicial = generar_poblacion() # Guardamos nuestra poblacion en otra variable
print('Poblacion inicial')
for i, cromosoma in enumerate(poblacion_inicial):
    # Para cada individuo se calcula el peso total, multiplicando la cantidad de producto
    # por su peso y sumando estas cantidades, y asi comprobamos que se cumpla la restriccion de peso
    peso_total = sum(cromosoma[j]*productos[j]['peso'] for j in range(len(productos)))
    aptitud = calcular_aptitud(cromosoma)
    print(f'individuo {i+1}: {cromosoma} | peso total: {peso_total:.2f} libras | aptitud: {aptitud} galeones')