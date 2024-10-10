import pandas as pd
import numpy as np
from tables_comparator import Tables_comparator
from data_analyzer import Data_analyzer
from date import Date

print("data_analyzer01.")
option=input("1. Data_analyzer01.\n2. Tables comparator. \n3. Str_date_order. \n4. Salir. \n")

while option!=4:
    
    if option=='1':
        number_plate=input("Digite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)

    elif option=='2':
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

        Tables_comparator.comparator(landmarks,geofences)

    elif option=='3':
        table02=input("Digita el nombre de la tabla: ")
        Date.order_date(table02)       

    elif option=='4':
        print("Saliendo")
        break
    
    option=input("1. Data_analyzer01.\n2. Tables comparator. \n3. Str_date_order. \n4. Salir. \n")
