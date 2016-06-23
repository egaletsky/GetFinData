# -*- coding: utf-8 -*-
 # Импортировали библиотеку для работы с адресами и запросами Internet.
import urllib


url = "http://195.128.78.52/GBPUSD_141201_141201.csv?market=5&em=86&code=GBPUSD&df=1&mf=11&yf=2014&from=01.12.2014&dt=6&mt=11&yt=2014&to=06.12.2014&p=2&f=GBPUSD_141201_141206&e=.csv&cn=GBPUSD&dtf=1&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=5&at=1"
data= ""

with urllib.request.urlopen(url) as response:
   data = response.read()
   
print(data[:500]) # Первые 500 символов полученных данных.   


from pandas import DataFrame, read_csv  # Чтобы упаковать результат в стандартный DataFrame.
data = read_csv(url, header=0, index_col=0, parse_dates={'Date&Time': [0, 1]}, sep=';').sort_index()
data.columns = ['' + i for i in ['Open', 'High', 'Low', 'Close', 'Volume']] # Заголовки столбцов

from pandas import set_option
set_option('display.max_columns', 50) # Кол-во колонок
set_option('display.width', 500)      # и ширина поля вывода
                                      # (чтобы при выводе не переносило широкие таблицы).

print(data.head())  # Вывели первые строки набора данных.
print(data)

'''
urllib.request.
f = urlopen(url)   # Открыли соединение.
data1 = f.read()   # Прочитали данные.
f.close()          # Закрыли соединение.
'''