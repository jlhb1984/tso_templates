import pandas as pd

class Date():
    def __init__(self,table02):
        self.table02=table02
    
    def order_date(table02):
        path=table02
        df=pd.read_csv(path)
        df_filter=df[['Unit','Events','Date','Landmark']]
        print(df_filter.info())
        df_filter['Date']=pd.to_datetime(df['Date'])
        print(df_filter.info())        
        df.sort_values(by='Date', ascending=True)
        print(df_filter)
        df_filter_date=df_filter[(df_filter['Date'].dt.month>8)&(df_filter['Date'].dt.day>26)]
        print(df_filter_date)
        print("\n")