import turtle
import heapq
import time  # Para la pausa entre dibujos

# Datos del problema
roads = {
    1: {2: 200},
    2: {1: 200, 3: 150, 4: 350, 5: 450},
    3: {2: 150, 6: 225},
    4: {2: 350, 5: 300},
    5: {2: 450, 4: 300, 6: 400, 7: 250},
    6: {3: 225, 5: 400},
    7: {5: 250, 8: 125},
    8: {7: 125}
}

heuristics = {  # Heurística: distancia en línea recta a la ciudad 8
    1: 800,
    2: 650,
    3: 500,
    4: 650,
    5: 325,
    6: 375,
    7: 125,
    8: 0
}

# Implementación del algoritmo A*
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))  # La cola de prioridad
    came_from = {}  # Para seguir el camino
    g_score = {node: float('inf') for node in roads}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Devuelve el camino en orden correcto

        for neighbor, distance in roads[current].items():
            tentative_g_score = g_score[current] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # No se encontró camino

# Visualización con Turtle
def draw_path(path):
    # Configuración de Turtle
    screen = turtle.Screen()
    screen.title("A* Pathfinding Visualization")
    screen.bgcolor("white")
    
    # Coordenadas ficticias para representar las ciudades
    positions = {
        1: (-300, 200),
        2: (-200, 100),
        3: (-100, 200),
        4: (0, 0),
        5: (100, -100),
        6: (0, 200),
        7: (200, -150),
        8: (300, -200)
    }

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()

    # Dibuja las ciudades
    for city, pos in positions.items():
        t.goto(pos)
        t.dot(20, "blue")
        t.write(f"City {city}", align="center", font=("Arial", 12, "bold"))

    # Dibuja las conexiones de carretera con retardo
    for city, neighbors in roads.items():
        time.sleep(0.2) 
        for neighbor in neighbors:
            t.goto(positions[city])
            t.pendown()
            t.goto(positions[neighbor])
            t.penup()
            time.sleep(0.5)  # Retardo entre cada conexión

    # Dibuja el camino encontrado con retardo
    t.pencolor("red")
    t.pensize(3)
    t.goto(positions[path[0]])
    t.pendown()
    for city in path[1:]:
        t.goto(positions[city])
        time.sleep(0.2)  # Retardo entre cada paso del camino
    t.penup()

    # Mantener ventana abierta
    screen.mainloop()

# Resolviendo el problema
path = a_star(1, 8)
if path:
    print(f"El camino más corto de la ciudad 1 a la 8 es: {path}")
    draw_path(path)
else:
    print("No se encontró un camino de la ciudad 1 a la ciudad 8.")
