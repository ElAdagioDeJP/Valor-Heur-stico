import heapq

# Grafo representado como un diccionario con las distancias entre ciudades
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

# Distancias aéreas estimadas hacia Barcelona
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

def a_star(grafo, inicio, objetivo, heuristica=None):
    """
    Implementación del algoritmo A* para encontrar el camino más corto.
    Parámetros:
    - grafo: Diccionario con el grafo (ciudades y distancias entre ellas).
    - inicio: Nodo de inicio.
    - objetivo: Nodo objetivo.
    - heuristica: Diccionario con los valores heurísticos (opcional).
    """
    # Inicialización de estructuras de datos
    heuristica = heuristica or {nodo: 0 for nodo in grafo}
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

# Parte A: Heurística nula
print("Parte A: Heurística nula")
camino, costo = a_star(grafo, "Palencia", "Barcelona", heuristica={nodo: 0 for nodo in grafo})
print(f"Camino más corto: {camino}")
print(f"Costo total: {costo} km\n")

# Parte B: Heurística basada en distancias aéreas
print("Parte B: Heurística con distancias aéreas")
camino, costo = a_star(grafo, "Palencia", "Barcelona", heuristica=heuristica)
print(f"Camino más corto: {camino}")
print(f"Costo total: {costo} km")