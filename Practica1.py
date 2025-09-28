import random

productos=[
    {'nombre': 'Decoy Detonators', 'peso': 4, 'precio': 10},
    {'nombre': 'Fever Fudge', 'peso': 2, 'precio': 3},
    {'nombre': 'Love Potion', 'peso': 2, 'precio': 8},
    {'nombre': 'Puking Pastilles', 'peso': 1.5, 'precio': 2},
    {'nombre': 'Extendable Ears', 'peso': 5, 'precio': 12},
    {'nombre': 'Nosebleed Nougat', 'peso': 1, 'precio': 2},
    {'nombre': 'Skiving Snackbox', 'peso': 5, 'precio': 6},
]

capacidad_maxima = 30
tamano_poblacion = 10
posicion_love_potion = 2
posicion_skiving_snackbox = 6

def creacion_individuo():
    individuo = [0]*len(productos)
    peso_actual = 0

    individuo[posicion_love_potion] = 3
    peso_actual += productos[posicion_love_potion]['peso']*3

    individuo[posicion_skiving_snackbox] = 2
    peso_actual += productos[posicion_skiving_snackbox]['peso']*2

    posiciones_productos = list(range(len(productos)))
    random.shuffle(posiciones_productos)

    for i in posiciones_productos:
        if peso_actual + productos[i]['peso']<=capacidad_maxima:
            agregar_producto = int((capacidad_maxima - peso_actual) // productos[i]['peso'])
            productos_disponible = 10 - individuo[i]
            limitar_producto = min(agregar_producto, productos_disponible)

            if limitar_producto > 0:
                cantidad_azar = random.randint(1, limitar_producto)
                individuo[i] += cantidad_azar
                peso_actual += productos[i]['peso']*cantidad_azar

    return individuo

def generar_poblacion():
    poblacion = []
    for _ in range(tamano_poblacion):
        poblacion.append(creacion_individuo())
    
    return poblacion

poblacion_inicial = generar_poblacion()
print('Poblacion inicial')
for i, cromosoma in enumerate(poblacion_inicial):
    peso_total = sum(cromosoma[j]*productos[j]['peso'] for j in range(len(productos)))
    print(f'individuo {i+1}: {cromosoma} | peso total: {peso_total:.2f} libras')