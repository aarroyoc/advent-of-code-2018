from dataclasses import dataclass
from collections import defaultdict
import math

@dataclass
class Punto:
    x: int
    y: int
    owner: int

def distancia(p1,p2):
    return abs(p1.x-p2.x)+abs(p1.y-p2.y)

def day6(file):
    with open(file) as f:
        lines = f.readlines()
    puntosControl = list()
    xlist = list()
    ylist = list()
    for i,line in enumerate(lines):
        l = line.split(",")
        xlist.append(int(l[0]))
        ylist.append(int(l[1]))
        puntosControl.append(Punto(x=int(l[0]),y=int(l[1]),owner=i))
    esquinaSuperiorIzquierda = Punto(x=min(xlist),y=min(ylist),owner=-1)
    esquinaInferiorDerecha = Punto(x=max(xlist),y=max(ylist),owner=-1)

    # Los que están fuera del rango esquinaSuperiorIzquierdaxesquinaInferiorDerecha se excluyen automáticamente
    excluidos = set()
    world = defaultdict(lambda: -1)
    #world_total = set()
    world_total = 0
    for i in range(esquinaSuperiorIzquierda.x-1,esquinaInferiorDerecha.x+2):
        for j in range(esquinaSuperiorIzquierda.y-1,esquinaInferiorDerecha.y+2):
            punto = Punto(x=i,y=j,owner=-1)
            distanciaMin = math.inf
            total = 0
            for p in puntosControl:
                if distancia(punto,p) == distanciaMin:
                    punto.owner = -1
                if distancia(punto,p) < distanciaMin:
                    distanciaMin = distancia(punto,p)
                    punto.owner = p.owner
                total += distancia(punto,p)
            if total < 10000:
                world_total += 1
                #world_total.add((i,j)) 
                
            if i == esquinaSuperiorIzquierda.x-1 or i == esquinaInferiorDerecha.x+1 or j == esquinaSuperiorIzquierda.y-1 or j == esquinaInferiorDerecha.y+1:
                excluidos.add(punto.owner)
            if punto.owner > -1:
                world[(i,j)] = punto.owner
    conteo = defaultdict(lambda: 0)
    for p in world:
        if not world[p] in excluidos:
            conteo[world[p]] += 1
    max_finite_area = max(conteo.values())
    region_size = world_total

    return max_finite_area,region_size
        





            
