import pandas as pd
import numpy as np

class Tables_comparator:
    def __init__(self,geofences,landmarks):
        self.geofences=geofences
        self.landmarks=landmarks
             
    def comparator(geofences,landmarks):
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