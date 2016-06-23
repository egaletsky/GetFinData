# -*- coding: utf-8 -*-
import FinamDownload


#Параметры времени
#period = 'tick', 'min', '5min', '10min', '15min', '30min', 'hour', 'daily', 'week', 'month'
timeParam = {'start_date_str': '01.06.2016',
             'end_date_str'  : '23.06.2016',
             'period'        : 'hour'} 

#Список инструментов
symbols = ["SPFB.GAZP","GBPUSD","AUDCAD"]



 
d = FinamDownload.GetDataFrame(symbols,timeParam)  
d.to_csv("data.csv")  
print(d)
