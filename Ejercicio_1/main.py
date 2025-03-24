from Estrella import Estrella

def main():
    estrella_A = Estrella(2, 3, 1)
    estrella_B = Estrella(4, 4, 4)
    estrella_C = Estrella(-3, -1, 0)
    origen = Estrella()

    print("Estrella A:", estrella_A)
    print("Estrella B:", estrella_B)
    print("Estrella C:", estrella_C)

    print("Galaxia de Estrella A:", estrella_A.galaxia())
    print("Galaxia de Estrella B:", estrella_B.galaxia())
    print("Galaxia de Estrella C:", estrella_C.galaxia())

    distancia_A_B = estrella_A.distancia(estrella_B)
    distancia_B_C = estrella_B.distancia(estrella_C)
    print("Distancia entre A y B:", distancia_A_B)
    print("Distancia entre B y C:", distancia_B_C)

    distancia_A_origen = estrella_A.distancia(origen)
    distancia_B_origen = estrella_B.distancia(origen)
    distancia_C_origen = estrella_C.distancia(origen)

    if distancia_A_origen > distancia_B_origen and distancia_A_origen > distancia_C_origen:
        print("La estrella más lejos del origen es A.")
    elif distancia_B_origen > distancia_C_origen:
        print("La estrella más lejos del origen es B.")
    else:
        print("La estrella más lejos del origen es C.")

if __name__ == "__main__":
    main()
