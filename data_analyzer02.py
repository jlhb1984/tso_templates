import pandas as pd
import numpy as np

print("Tables comparator.")
option=input("1. Comparar.\n2. Salir. \n")

while option!=2:
    if option=='1':
        #Carga de la tabla 1. Landmarks InOut.csv
        table01=input("Digita el nombre de la tabla 1: ")
        df_book_landmarks=pd.read_csv(table01)
        df_book_landmarks.info()

        #Carga de la tabla 2. Geofences InOut Report.csv
        table02=input("Digita el nombre de la tabla 2: ")
        df_book_geofences=pd.read_csv(table02)
        df_book_geofences.info()

        #Carga de la columna de la tabla 1. ContactName
        table01_column=input("Digita el nombre de la columna de la tabla 1: ")
        landmarks=df_book_landmarks.loc[:,table01_column]
        landmarks.info()
        print(landmarks)

        #Carga de la columna de la tabla 1. GeofenceName
        table02_column=input("Digita el nombre de la columna de la tabla 2: ")
        geofences=df_book_geofences.loc[:,table02_column]
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
                    print("\ncdz")
                    print("Se encontró geofence con igual nombre de landmark")
                    print("Geofence número: ",i,"con nombre: ",geofences.iloc[i],". ","Landmark número: ",j,"con nombre: ",landmarks.iloc[j],".")
    
    elif option=='2':
        print("Saliendo!")
        break

    print("Tables comparator.")
    option=input("1. Comparar.\n2. Salir. \n")