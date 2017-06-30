from scapy.all import *
import subprocess
import requests
import time
from time import localtime, strftime, sleep
lastdetection = 0
import urllib
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import locale
import json

#Das ist die Übergeordnete Methode (Mainmethode)
def arp_display(pkt):
  global lastdetection
  if pkt.haslayer(DHCP):
    #Hier muss die MAC-Adresse vom 1ten DashButton Helfer eingetragen werden
    if pkt[Ether].src == '44:65:0d:f5:78:7b':
      if(time.time() - lastdetection > 10):
          print
          print "Helfer"
          ifttt_postB('Helfer eingetroffen')
          2google('Helfer eingetroffen')
    #Hier muss die MAC-Adresse vom 2ten DashButton  Patient eingetragen werden
    elif pkt[Ether].src == 'ac:63:be:3d:ab:bd':
      if(time.time() -lastdetection > 10):
          print
          print "Patient"
          ifttt_post('Raum 225')
          2google("Patient A")
          lastdetection = time.time()
    else:
      #Falls keine Bekannte MAC-Adresse erkannt wird, erfolgt die Ausgabe aller gefundenen MAC-Adressen
      print pkt[Ether].src

# Methode zum IFTTT E-MAIL vom Patienten
def ifttt_post(value):
    url = 'https://maker.ifttt.com/trigger/Patient/with/key/1ZtlOAudE_eoCRCU0UVsa'
    query = {'value1': value}
    res = requests.post(url, data=query)
    print(res.text)

# Methode zum IFTT E-MAIL vom Helfer, alles OK
def ifttt_postB(value):
    url = 'https://maker.ifttt.com/trigger/Helfer/with/key/1ZtlOAudE_eoCRCU0UVsa'
    query = {'value1': value}
    res = requests.post(url, data=query)
    print(res.text)

# Methode zum IFTTT Schreiben in GoogleDocs
def 2google(name):
    url = 'https://maker.ifttt.com/trigger/2google/with/key/1ZtlOAudE_eoCRCU0UVsa'
    lt = localtime()
    tag = strftime("%-d. %B", lt)
    uhrzeit = strftime("%-H:%M",lt)
    wochentag = strftime("%A",lt)
    print wochentag
    value = wochentag
    #Hier werden zwei Parameter an IFTTT übergeben zum einen der Wochentag und zum anderen der Name
    query = {'value1': value , 'value2' : name}
    res = requests.post(url, data=query)
    print(res.text)
    
#2google("Script startet")  
print sniff(prn=arp_display, filter="(udp and (port 67 or 68))", store=0)
 
