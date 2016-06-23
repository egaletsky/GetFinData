# -*- coding: utf-8 -*-
import urllib
#from urllib import urllib.parse.urlencode
from datetime import datetime
from pandas import DataFrame, read_csv  # Чтобы упаковать результат в стандартный DataFrame.


 
#Заполнение датафрейма по списку инструментов
def GetDataFrame(symbols,timeParam):
    dataframe = DataFrame() 
    for symbol in symbols:
        dataframe = dataframe.append(DownloadFinamData(symbol,timeParam))
    return dataframe    
    
    
#Получение данных с сайта по единичному инструменту
def DownloadFinamData(symbol,timeParam):
     # Определяем параметры инструмента из списка активных инструментов:
    symbol_code = symboldict[symbol]['symbol_code']
    market      = symboldict[symbol]['market']
    
    # Определяем временные параметры из дат и числового обозначения таймфрейма финама:
    start_date_str = timeParam['start_date_str']
    end_date_str   = timeParam['end_date_str']
    period         = perioddict[timeParam['period']]
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
    end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()      
        
    # Формируем строку с параметрами запроса:
    params = urllib.parse.urlencode([('market', market), ('em', symbol_code), ('code', symbol),
                       ('df', start_date.day), ('mf', start_date.month - 1), ('yf', start_date.year),
                       ('from', start_date_str),
                       ('dt', end_date.day), ('mt', end_date.month - 1), ('yt', end_date.year),
                       ('to', end_date_str),
                       ('p', period), ('f', "table"), ('e', ".csv"), ('cn', symbol),
                       ('dtf', 1), ('tmf', 3), ('MSOR', 1), ('mstime', "on"), ('mstimever', 1),
                       ('sep', 3), ('sep2', 1), ('datf', 1), ('at', 1)])
    
    # Полная строка адреса со всеми параметрами.
    FINAM_URL = "http://195.128.78.52/table.csv?"
    url = FINAM_URL + params 
    
    # Соединяемся с сервером, получаем данные и выполняем их разбор:
    data = read_csv(url, header=0, index_col=0, parse_dates={'Date&Time': [2, 3]}, sep=';').sort_index()
    data.columns = ['' + i for i in ['TIKER','PER','OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']] # Заголовки столбцов
    
    return data

#Словарь список активных инструментов
def GetSymbolDictionary():
    symboldict =   {'GBPUSD':{'symbol_code':'86','market':'5'},
                    'AUDCAD':{'symbol_code':'181410','market':'5'},
                    'SPFB.GAZP':{'symbol_code':'17451','market':'14'},
                    'SPFB.VTBR':{'symbol_code':'19891','market':'14'},
                    'SPFB.SBRF':{'symbol_code':'17456','market':'14'}} 
    return symboldict

#Словарь список доступных таймфреймов в числовых обозначениях финама  
def GetPeriodDictionary():
    perioddict =   {'tick': 1, 'min': 2, '5min': 3, '10min': 4, '15min': 5, '30min': 6, 'hour': 7, 'daily': 8, 'week': 9, 'month': 10} 
    return perioddict


symboldict = GetSymbolDictionary()
perioddict = GetPeriodDictionary()
