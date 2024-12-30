import json

def json_a_lista(archivo: str, es_json_seguidos: bool) -> list:
    with open(archivo, 'r') as archivo:
        archivo_json = json.load(archivo)
    
    lista = []

    if es_json_seguidos:
        archivo_json = archivo_json['relationships_following']

    for elemento in archivo_json:
        lista.append(elemento["string_list_data"][0]["value"])

    return lista


def main():

    print('Listado de gente que seguis pero no te sigue!')

    seguidores = json_a_lista(input('Archivo json con la gente que te sigue > '), False)
    seguidos = json_a_lista(input('Archivo json con la gente que seguis > '), True)

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
