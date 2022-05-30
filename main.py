#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import ADS
from time import sleep
import requests
ads = ADS.ADS1115() #ads nesnesi çağırıldı

"""
MQTT nasıl çalıştığını anlamak için izle bunları
https://www.youtube.com/watch?v=hmPslaLRcHo&ab_channel=YigidOS
https://www.youtube.com/watch?v=kw-9wYDFxpg&ab_channel=YigidOS
"""

#Veri sınıflanır
def  map( x,  in_min,  in_max,  out_min,  out_max):
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


#Telegram kodları
api_id = '1446771393'
token = "1519506201:AAFDSIvFPHe-oMssGGsJROCo7E3dkpEobos"

#Telegrama mesaj atma fonksyonu
def mesaj_at(bot_message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + api_id + '&parse_mode=Markdown&text=' + bot_message
    #http request olarak bot a mesaj atma
    response = requests.get(send_text)

    return response.json()
# mqtt bağlantı mesaj paylaşma fonksyonları
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    
    client.subscribe("/btn")

def on_message(client, userdata, msg):
    pass
def on_publish(client,userdata,result):            
    print("data published \n")

    pass
# mqtt nesnesi ve bağlantı fonksyonu
client = mqtt.Client()
client.connect("192.168.1.25", 1883, 60)
client.on_publish = on_publish  
client.on_connect = on_connect
client.on_message = on_message
#while döngüsü
while True:
    """
    Bu kısımda ölçülen değerin mutlak değeri alınır 0-1000 olan değer 0-100
    Arasına ölçeklenir ve ilgili topic e "publish" edilir
    """
    """
    volt1 = ads.readADCSingleEnded(channel=0) #okuma
    mapped1 = map(abs(volt1),0,1000,0,100) #ölçekleme
    if mapped1 <= 10:                   #paraziti önlemek için if ile filtre
        mapped1 = 0
    client.publish("/on",mapped1)  # ilgili topic e publish

    """

    ###############

    volt1 = ads.readADCSingleEnded(channel=0)
    mapped1 = map(abs(volt1),0,1000,0,100)
    if mapped1 <= 10:
        mapped1 = 0
    client.publish("/on",mapped1)
    ###############

    ###############
    volt2 = ads.readADCSingleEnded(channel=1)
    mapped2 = map(abs(volt2),0,1000,0,100)
    if mapped2 <= 10:
        mapped2 = 0
    client.publish("/arka",mapped2)
    ###############

    ###############
    volt3 = ads.readADCSingleEnded(channel=2)
    mapped3 = map(abs(volt3),0,1000,0,100)
    if mapped3 <= 10:
        mapped3 = 0
    client.publish("/sol",mapped3)
    ###############

    ###############
    volt4 = ads.readADCSingleEnded(channel=3)
    mapped4 = map(abs(volt4),0,1000,0,100)
    if mapped4 <= 10:
        mapped4 = 0
    client.publish("/sag",mapped4) 
    ###############  

    """
    önümüze gelen değer gönderilmesin diye 
    70 üstü değerler paylaşılır ama 70 den büyük bir değer olursa 
    işlemci hızına bağlı olarak paylaşılır

    """

    if mapped1 >=70:
        mesaj_at("Aracınız önden ağır hasar aldı")     
    if mapped2 >=70:
        mesaj_at("Aracınız arkadan ağır hasar aldı")     
    if mapped3 >=70:
        mesaj_at("Aracınız soldan ağır hasar aldı")     
    if mapped4 >=70:
        mesaj_at("Aracınız sağdan ağır hasar aldı")  



    sleep(0.3) # 0.3 sn de bir döngü tekrarlanır böylece veri karmaşası önlenir

client.loop_forever() #bağlantının devamlılığı sağlanır










