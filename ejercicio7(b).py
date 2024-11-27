import heapq
import turtle
import time

# Grafo con distancias basado en el mapa proporcionado
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

# Distancias aéreas estimadas hacia Barcelona (heurística actualizada)
heuristica = {
    "Barcelona": 0,
    "Bilbao": 502,
    "Cáceres": 850,
    "Madrid": 550,
    "Palencia": 580,
    "Santander": 605,
    "Valencia": 303,
    "Zaragoza": 275,
}

# Coordenadas ajustadas según el mapa proporcionado
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

def a_star(grafo, inicio, objetivo, heuristica):
    """
    Implementación del algoritmo A* para encontrar el camino más corto.
    """
    abierta = []
    heapq.heappush(abierta, (0, inicio))  # (f(n), nodo)
    costos = {inicio: 0}
    padres = {inicio: None}
    
    while abierta:
        _, nodo_actual = heapq.heappop(abierta)
        
        # Si llegamos al objetivo, reconstruimos el camino
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1], costos[objetivo]
        
        # Expandimos los vecinos del nodo actual
        for vecino, costo in grafo[nodo_actual].items():
            nuevo_costo = costos[nodo_actual] + costo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino]
                heapq.heappush(abierta, (prioridad, vecino))
                padres[vecino] = nodo_actual
    
    return None, float("inf")  # No se encontró un camino

def dibujar_grafo(camino):
    """
    Visualiza el grafo y el camino encontrado usando Turtle.
    """
    pantalla = turtle.Screen()
    pantalla.title("Visualización del mapa de carreteras")
    pantalla.bgcolor("white")
    
    tortuga = turtle.Turtle()
    tortuga.speed(0)
    tortuga.penup()
    tortuga.hideturtle()

    # Dibujar las ciudades
    for ciudad, pos in coordenadas.items():
        tortuga.goto(pos)
        tortuga.dot(20, "blue")
        tortuga.write(ciudad, align="center", font=("Arial", 12, "bold"))

    # Dibujar las conexiones del grafo
    for ciudad, vecinos in grafo.items():
        for vecino in vecinos:
            tortuga.goto(coordenadas[ciudad])
            tortuga.pendown()
            tortuga.goto(coordenadas[vecino])
            tortuga.penup()

    # Dibujar el camino encontrado
    tortuga.pencolor("red")
    tortuga.pensize(3)
    tortuga.goto(coordenadas[camino[0]])
    tortuga.pendown()
    for ciudad in camino[1:]:
        tortuga.goto(coordenadas[ciudad])
        time.sleep(0.5)  # Retardo para visualizar el camino paso a paso
    tortuga.penup()

    pantalla.mainloop()

# Ejecutar el algoritmo A* y mostrar los resultados
inicio = "Palencia"
objetivo = "Barcelona"
camino, costo = a_star(grafo, inicio, objetivo, heuristica)

if camino:
    print(f"Camino más corto considerando heurística (A*): {camino}")
    print(f"Costo total: {costo} km")
    dibujar_grafo(camino)
else:
    print("No se encontró un camino entre las ciudades.")