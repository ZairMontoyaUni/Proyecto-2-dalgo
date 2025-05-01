from collections import deque
import time

def resolver_caso(n, energia, robots, poderes):
    destino = n
    visitado = set()
    cola = deque()
    cola.append((0, energia, []))  # (posición actual, energía restante, lista de acciones)

    robots_set = set(robots)
    poderes_dict = dict(zip(poderes[::2], poderes[1::2]))

    while cola:
        posicion_actual, energia_restante, acciones = cola.popleft()

        if posicion_actual == destino:
            print(len(acciones), " ".join(acciones))
            return

        if (posicion_actual, energia_restante) in visitado:
            continue
        visitado.add((posicion_actual, energia_restante))

        # Movimiento C+
        if posicion_actual + 1 <= n and (posicion_actual + 1) not in robots_set:
            cola.append((posicion_actual + 1, energia_restante, acciones + ["C+"]))

        # Movimiento C-
        if posicion_actual - 1 >= 0 and (posicion_actual - 1) not in robots_set:
            cola.append((posicion_actual - 1, energia_restante, acciones + ["C-"]))

        # Movimiento S+ o S-
        if posicion_actual in poderes_dict:
            salto = poderes_dict[posicion_actual]
            if posicion_actual + salto <= n and (posicion_actual + salto) not in robots_set:
                cola.append((posicion_actual + salto, energia_restante, acciones + ["S+"]))
            if posicion_actual - salto >= 0 and (posicion_actual - salto) not in robots_set:
                cola.append((posicion_actual - salto, energia_restante, acciones + ["S-"]))

        # Movimiento T±k (teletransportaciones)
        for k in range(1, energia_restante + 1):
            for dir in [1, -1]:
                destino_tp = posicion_actual + dir * k
                if 0 <= destino_tp <= n and destino_tp not in robots_set and destino_tp != 0 and posicion_actual != 0:
                    accion = f"T{dir * k}"
                    cola.append((destino_tp, energia_restante - k, acciones + [accion]))

    print("NO SE PUEDE")

def main():
    start_time = time.perf_counter()
    casos = int(input())
    
    for _ in range(casos):
        n, energia = map(int, input().split())
        robots = list(map(int, input().split()))
        poderes = list(map(int, input().split()))
        resolver_caso(n, energia, robots, poderes)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The function took {execution_time:.4f} seconds to execute.")

if __name__ == "__main__":
    main()


