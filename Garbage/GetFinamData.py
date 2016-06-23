#------------------------------------------------------------------------------
#!/usr/bin/env python
import pycurl8
import StringIO
import datetime
import pygame

#===================================Глобальные переменные
glMArket = "200"

gl_File = open("DataFile.csv", "wb")

#===Дата начала
gl_D_S   = "20"
gl_M_S   = "0"   # месяц меньше на единичку (0 -  январь)
gl_Y_S   = "2012"

#===Дата конца
gl_D_F  = "20"
gl_M_F   = "0"
gl_Y_F   = "2012"



def PlayText(textForPlay):
  gl_Aud = open("Aud.mp3", "wb")
  url = "http://translate.google.com/translate_tts?ie=utf-8&q="+ textForPlay + "&tl=en"
  c = pycurl.Curl()
  c.setopt(pycurl.SSL_VERIFYPEER, 0)
  c.setopt(pycurl.SSL_VERIFYHOST, 0)
  c.setopt(pycurl.URL,url)
  c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3");
  c.setopt(pycurl.FOLLOWLOCATION, 1);
  c.setopt(pycurl.VERBOSE, 1);
  c.setopt(pycurl.AUTOREFERER, 1);
  c.setopt(pycurl.WRITEDATA, gl_Aud)
  c.perform()
  c.close()
  gl_Aud.close()

  # set up the mixer
  freq = 22050    # half-audio CD quality
  bitsize = -16    # unsigned 16 bit
  channels = 2     # 1 is mono, 2 is stereo
  buffer = 1024   # number of samples (experiment to get right sound)
  pygame.mixer.init(freq, bitsize, channels, buffer)
  pygame.mixer.music.load("Aud.mp3")
  pygame.mixer.music.play()


def GetFile(stockName, stockCode):
  sN = stockName
  sC = stockCode
  url = "http://195.128.78.52/" + sN + "_data.csv?market="\
          + glMarket+"&em=" + sC + "&code=" + sN\
          + "&df=" + gl_D_S + "&mf=" + gl_M_S + "&yf=" + gl_Y_S\
          + "&dt=" + gl_D_F + "&mt=" + gl_M_F + "&yt=" + gl_Y_F\
          + "&p=2&f=" + sN + "_data&e=.csv&cn=" + sN + "&dtf=1&tmf=1&MSOR=0&mstime=on&mstimever=1&sep=3&sep2=1&datf=1"

  c = pycurl.Curl()
  c.setopt(pycurl.SSL_VERIFYPEER, 0)
  c.setopt(pycurl.SSL_VERIFYHOST, 0)
  c.setopt(pycurl.URL,url)
  c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3");
  c.setopt(pycurl.FOLLOWLOCATION, 1);
  c.setopt(pycurl.VERBOSE, 1);
  c.setopt(pycurl.AUTOREFERER, 1);

  #=================================Аутентификация прокси==================
##  c.setopt(pycurl.PROXY, "10.46.51.125")
##  c.setopt(pycurl.PROXYPORT,3128)
##  c.setopt(pycurl.PROXYUSERPWD,'eagaletskiy:ukj,ec20')
##  #c.setopt(pycurl.PROXY,'eagaletskiy:ukj,ec20@10.46.51.125:3128')
##  c.setopt(pycurl.PROXYAUTH, pycurl.HTTPAUTH_ANY);
  #========================================================================

#  fName = sN + "_data.csv"
#  f = open(fName, "wb")
#  c.setopt(pycurl.WRITEDATA, f)
#  c.perform()

  c.setopt(pycurl.WRITEDATA, gl_File)
  c.perform()

  c.close()
  print sN," get.."
#  f.close()

def main():

  #=================== - определяем временные константы
  global gl_D_S
  global gl_M_S
  global gl_Y_S

  global gl_D_F
  global gl_M_F
  global gl_Y_F

  timeshift = -125 # по умолчанию
  timedelta = datetime.timedelta(days = timeshift)

  now  = datetime.datetime.now()
  year, month, day, hour, minutes, sec, wday, yday, isdst = now.timetuple()

  gl_D_F = str(day)
  gl_M_F = str(month - 1)
  gl_Y_F = str(year)

  past = now + timedelta
  year, month, day, hour, minutes, sec, wday, yday, isdst = past.timetuple()

  gl_D_S = str(day)
  gl_M_S = str(month - 1)
  gl_Y_S = str(year)


#===================


  global gl_File
  gl_File = open("DataFile.csv", "wb")

  # Получаем голубые фишки MICEX
  global glMarket
  #glMarket = "1"

  #GetFile("SBER","3")
 # GetFile("GAZP","16842")
 # GetFile("LKOH","8")
 # GetFile("ROSN","17273")
 # GetFile("VTBR","19043")
 # GetFile("GMKN","795")
 # GetFile("SNGS","4")
 # GetFile("SNGSP","13")
 # GetFile("SBERP","23")
 # GetFile("CHMF","16136")
 # GetFile("TRNFP","1012")
 # GetFile("URKA","19623")
 # GetFile("HYDR","20266")
 # GetFile("NLMK","17046")
 # GetFile("RTKM","7")








  # Получаем FORTS
  glMarket = "14"
  GetFile("SPFB.GAZP","17451")
  GetFile("SPFB.VTBR","19891")
 # GetFile("SPFB.SBRF","17456")

  gl_File.close()

  PlayText("download+complete")




if __name__ == '__main__':
    main()
