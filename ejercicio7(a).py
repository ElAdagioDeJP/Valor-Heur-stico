import heapq
import turtle

# Grafo con las distancias entre las ciudades (costes)
grafo = {
    "Palencia": {"Madrid": 239, "Santander": 203, "Cáceres":368},
    "Madrid": {"Zaragoza": 322, "Cáceres": 299, "Valencia": 350, "Palencia": 239},
    "Zaragoza": {"Barcelona": 299, "Madrid": 322, "Bilbao": 323},
    "Cáceres": {"Madrid": 299, "Palencia": 368},
    "Valencia": {"Madrid": 350, "Barcelona": 352},
    "Santander": {"Palencia": 203, "Bilbao": 111},
    "Bilbao": {"Santander": 111, "Zaragoza": 323},
    "Barcelona": {"Zaragoza": 299, "Valencia": 352},
}

# Implementación del algoritmo A* (sin heurística)
def a_star_sin_heuristica(grafo, inicio, fin):
    cola = [(0, inicio)]  # (coste acumulado, nodo)
    costes = {inicio: 0}
    padres = {inicio: None}
    
    while cola:
        coste_actual, nodo = heapq.heappop(cola)
        
        if nodo == fin:
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]
            return camino[::-1], coste_actual  # Camino y coste total
        
        for vecino, coste_vecino in grafo.get(nodo, {}).items():
            nuevo_coste = coste_actual + coste_vecino
            if vecino not in costes or nuevo_coste < costes[vecino]:
                costes[vecino] = nuevo_coste
                padres[vecino] = nodo
                heapq.heappush(cola, (nuevo_coste, vecino))
    
    return None, float('inf')  # Si no hay camino

# Coordenadas de las ciudades para la visualización con Turtle
coordenadas = {
    "Palencia": (-250, 100),
    "Madrid": (-100, 0),
    "Santander": (-300, 200),
    "Zaragoza": (150, 50),
    "Cáceres": (-350, 10),
    "Valencia": (200, -50),
    "Bilbao": (150, 200),
    "Barcelona": (300, 100),
}

# Función para dibujar las ciudades y las conexiones entre ellas
def graficar_camino(grafo, camino):
    screen = turtle.Screen()
    screen.setworldcoordinates(-400, -200, 400, 200)
    
    t = turtle.Turtle()
    t.speed(0)  # Velocidad máxima
    
    # Dibujar las ciudades
    for ciudad, (x, y) in coordenadas.items():
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(10, "blue")  # Dibujar ciudad
        t.penup()
        t.goto(x, y - 10)
        t.write(ciudad, align="center")
    
    # Dibujar las rutas entre las ciudades
    for ciudad in grafo:
        x1, y1 = coordenadas[ciudad]
        for vecino, coste in grafo[ciudad].items():
            x2, y2 = coordenadas[vecino]
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)
    
    # Resaltar el camino más corto
    t.color("red")
    for i in range(len(camino) - 1):
        ciudad1 = camino[i]
        ciudad2 = camino[i + 1]
        x1, y1 = coordenadas[ciudad1]
        x2, y2 = coordenadas[ciudad2]
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    
    turtle.done()

# Ejecutamos el algoritmo A* sin heurística
inicio = "Palencia"
fin = "Barcelona"
camino, coste = a_star_sin_heuristica(grafo, inicio, fin)

print(f"Camino más corto desde {inicio} hasta {fin}: {camino}")
print(f"Coste total: {coste} km")

# Graficar el camino
graficar_camino(grafo, camino)