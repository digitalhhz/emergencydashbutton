from scapy.all import *
import subprocess
import requests
import time
import gspread
import locale
from time import *
from oauth2client.service_account import *

def 2google(message = ''):
  scope = ['https://spreadsheets.google.com/feeds']
  #Die Credentials sollten als erstes angelget werden und der Pfad angepasst
  credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/credentials.json', scope)
  gspeadcreds = gspread.authorize(credentials)
  # Der Schlüssel sollte von der GoogleTabelle übernommen werden
  wkeys = gc.open_by_key("1Y34234pudshjalhJHDKAHLdhjknsaSADAioe").sheet1
  lotime = localtime()
  uhrzeit = strftime("%-H:%M",lt)
  wochentag = strftime("%A",lt)
  print wochentag
  print uhrzeit
  wkeys.append_row([wochentag,uhrzeit,message])
  
2google("DK")  
