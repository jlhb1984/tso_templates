import pandas as pd
import numpy as np

class Tables_comparator:
    def __init__(self,df_book_table01,df_book_table02):
        self.df_book_table01=df_book_table01
        self.df_book_table02=df_book_table02
             
    def comparator(df_book_table01,df_book_table02):
        print("df_book_table01: \n")
        print(df_book_table01.info())
        print("\n")
        print("df_book_table02: \n")
        print(df_book_table02.info())
        print("\n")
        print("df_book_table01.loc[0]: \n")
        print(df_book_table01.loc[0])
        print("df_book_table02.loc[0]: \n")
        print(df_book_table02.loc[0])        
        print(df_book_table02.head(5))
        df_book_table02=df_book_table02.drop(index=0)
        print(df_book_table02.head(5))
        print("df_book_table02.iloc[0,5] \n")
        print(df_book_table02.iloc[0,3])
        num_filas_table01=int(df_book_table01.shape[0])
        num_filas_table02=int(df_book_table02.shape[0])

        print("Trabajando...")
               
        for i in range(0,num_filas_table01):
            for j in range(0,num_filas_table02):
                #print(df_book_table02.iloc[j,3])
                #print("df_book_table01")
                #print(df_book_table01.iloc[i,0])
                #print("df_book_table02")
                #print(df_book_table02.iloc[j,5])
                if df_book_table01.iloc[i,0]==df_book_table02.iloc[j,5]:
                    print("* *I  g  u  a  l  e  s  * *")

        