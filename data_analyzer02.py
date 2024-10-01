import pandas as pd
import numpy as np

#Carga de la tabla 1.
df_book_landmarks=pd.read_csv('/home/jose/git/tso/Colab/Landmarks InOut.csv')
df_book_landmarks.info()

#Carga de la tabla 2.
df_book_geofences=pd.read_csv('/home/jose/git/tso/Colab/Geofences InOut Report.csv')
df_book_geofences.info()

landmarks=df_book_landmarks.loc[:,'ContactName']
landmarks.info()
print(landmarks)

geofences=df_book_geofences.loc[:,'GeofenceName']
geofences.info()
print(geofences)

landmarks.drop_duplicates(inplace=True)
geofences.drop_duplicates(inplace=True)

total_geofences=geofences.count()
total_landmarks=landmarks.count()
print("Total geofences: ",total_geofences)
print("Total landmarks: ",total_landmarks)

for i in range(0,total_geofences):
    for j in range(0,total_landmarks):
        if geofences.iloc[i]==landmarks.iloc[j]:
            print("Se encontró geofence con igual nombre de landmark")
            print("Geofence número: ",i,"con nombre: ",geofences.iloc[i],". ","Landmark número: ",j,"con nombre: ",landmarks.iloc[j],".")