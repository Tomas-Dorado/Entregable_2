import os
import subprocess

def mostrar_menu():
    print("Menú de Ejercicios:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Salir")

def ejecutar_main_de_carpeta(carpeta):
    try:
        ruta_carpeta = os.path.join(os.getcwd(), carpeta)
        if not os.path.exists(ruta_carpeta):
            print(f"La carpeta '{carpeta}' no existe.")
            return
        
        ruta_main = os.path.join(ruta_carpeta, "main.py")
        if os.path.exists(ruta_main):
            print(f"Ejecutando {carpeta}/main.py...\n")
            subprocess.run(["python", ruta_main], check=True)
        else:
            print(f"No se encontró 'main.py' en la carpeta '{carpeta}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar '{carpeta}/main.py': {e}")
    except Exception as e:
        print(f"Error al procesar la carpeta '{carpeta}': {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ejecutar_main_de_carpeta("Ejercicio_1")
        elif opcion == "2":
            ejecutar_main_de_carpeta("Ejercicio_2")
        elif opcion == "3":
            ejecutar_main_de_carpeta("Ejercicio_3")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()