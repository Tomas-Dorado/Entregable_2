def arreglar_texto(texto):
    '''Recibe un texto y lo formatea para que tenga el primer caracter 
    en mayúscula y añade puntos y saltos de línea.'''

    partes = texto.split('#')
    
    texto_formateado = partes[0].capitalize() + "..."
    
    for parte in partes[1:]:
        texto_formateado += "\n" + parte.capitalize() + "."
    
    return texto_formateado


def main():
    texto_original = ("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#"
                      "lo que se mueve es el viento -respondió otro monje#"
                      "ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")

    texto_arreglado = arreglar_texto(texto_original)
    print(texto_arreglado)


if __name__ == "__main__":
    main()