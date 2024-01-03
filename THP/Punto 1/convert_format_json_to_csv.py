#Importo librerias a utilizar
import pandas as pd
import json

#Leo archivo de formato json 
#(en este caso no se indica ruta de acceso asumiendo que se encuentra en el mismo directorio)
with open('taylor_swift_spotify.json', 'r') as file:
    data = json.load(file)

# Normalizo los datos para manejar las listas anidadas

df = pd.json_normalize(data = data,
                       record_path = ['albums', 'tracks'], 
                       meta = ['artist_id', 'artist_name', 'artist_popularity',
                       ['albums', 'album_id'], ['albums', 'album_name'], 
                       ['albums', 'album_release_date'], ['albums', 'album_total_tracks']])

# Elimino el prefijo 'albums.' de los nombres de las columnas para dejar en el formato solicitado
df.columns = df.columns.str.replace('albums.', '')

# Guardo el dataset en un archivo de formato csv
df.to_csv('dataset.csv', index=False)