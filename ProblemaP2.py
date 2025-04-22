#Victoria González Ch - 202320852
#Zair Montoya - 202321067
#Andrea Davila -

from collections import defaultdict
import sys
from collections import deque

def bfs(grafo, n, energia):
    visitado = set()
    cola = deque([(0, energia, [])])
    
    while cola:
        plataforma_actual, energia_restante, camino_corrido = cola.popleft()
        
        if plataforma_actual == n-1:
            return camino_corrido
        
        if (plataforma_actual, energia_restante) in visitado:
            continue
        visitado.add((plataforma_actual, energia_restante))
        
        for plataforma_vecina, accion in grafo[plataforma_actual]:
                nueva_energia = energia_restante
                
                if accion.startswith("T"):
                    nueva_energia = energia_restante - abs(int(accion[1:]))
                    if nueva_energia < 0:
                        continue
                
                if plataforma_vecina not in visitado:   
                    cola.append((plataforma_vecina, nueva_energia, camino_corrido + [accion]))
                    
                
    return "NO SE PUEDE"  


def leer_entrada():
    input_lines = sys.stdin.read().splitlines()
    casos = int(input_lines[0])
    
    idx = 1
    entradas = []
    
    for _ in range(casos):
        n, energia = map(int, input_lines[idx].split())
        idx += 1
        
        robots = list(map(int, input_lines[idx].split()))
        idx += 1
        
        saltos = list(map(int, input_lines[idx].split()))
        idx += 1
        
        poderes = {}
        for i in range(0, len(saltos), 2):
            plataforma = saltos[i]
            salto = saltos[i+1]
            poderes[plataforma] = salto
        
        entradas.append((n+1, energia, set(robots), poderes))
    
    return entradas
            
        

def construccion_grafo(n, energia, robots, powers):
    grafo = defaultdict(list)
    
    for i in range(n):
        if i in robots:
            continue
            
        if i + 1 < n and (i + 1) not in robots:
            grafo[i].append((i+1, "C+"))
        if i - 1 < n and (i - 1) not in robots:
            grafo[i].append((i-1, "C-"))
        
        for j in range(n):
            if j != i and j not in robots:
                saltos = (j - i)
                if abs(saltos) <= energia:
                    grafo[i].append((j, "T"+str(saltos)))
        
    for i, salto in powers.items():
        if i in robots:
            continue
        if i + salto < n and (i + salto) not in robots:
            grafo[i].append((i + salto, "S+"))
        if i - salto < n and (i - salto) not in robots:
            grafo[i].append((i - salto, "S-"))
    
    return grafo   


def main():
    casos = leer_entrada()
    
    for n, energia, robots, powers in casos:
        grafo = construccion_grafo(n, energia, robots, powers)
        solucion = bfs(grafo, n, energia)
        
        if solucion == "NO SE PUEDE":
            print(solucion)
        else:
            print(len(solucion) , " ".join(solucion))



if __name__ == "__main__":
    main()