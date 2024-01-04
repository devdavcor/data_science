import os
import multiprocessing

def obtener_numero_hilos():
    return os.cpu_count()

if __name__ == "__main__":
    numero_hilos = obtener_numero_hilos()
    print(f"Tu PC tiene {numero_hilos} hilos disponibles para trabajar.")
