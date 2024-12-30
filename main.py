import json

def obtener_seguidores(archivo: str) -> list:
    with open(archivo, 'r') as archivo:
        seguidores = json.load(archivo)

    lista_seguidores = []

    for seguidor in seguidores:
        lista_seguidores.append(seguidor["string_list_data"][0]["value"])

    return lista_seguidores

def obtener_seguidos(archivo: str) -> list:
    with open(archivo, 'r') as archivo:
        seguidos = json.load(archivo)

    lista_seguidos = []

    for seguido in seguidos['relationships_following']:
        lista_seguidos.append(seguido["string_list_data"][0]["value"])

    return lista_seguidos

def main():

    print('Listado de gente que seguis pero no te sigue!')

    seguidores = obtener_seguidores(input('Archivo json con la gente que te sigue > '))
    seguidos = obtener_seguidos(input('Archivo json con la gente que seguis > '))

    generar_archivo = False
    if input('¿Generar archivo con la salida? [S/n] ').upper() == 'S':
        generar_archivo = True

    seguidos_no_siguen = []
    for seguido in seguidos:
        if seguido not in seguidores:
            seguidos_no_siguen.append(seguido)

    print('\nResultados:')
    print("Numero de seguidores:", len(seguidores))
    print("Numero de seguidos:", len(seguidos))
    print(f'Los seguidos que no te siguen son:\n {seguidos_no_siguen}, \nTotal: {len(seguidos_no_siguen)}')

    if generar_archivo:
        with open("seguidos_que_no_siguen.txt", "w") as archivo:
            for elemento in seguidos_no_siguen:
                archivo.write(elemento + "\n")

if __name__ == "__main__":
    main()