import Adafruit_DHT as dht
import time as t
from datetime import datetime
from flask import Flask, request,jsonify
import requests
from bs4 import BeautifulSoup
import requests
import json

app = Flask("Sensor de Temperatura")

# Aqui eu envio pro meu backend qual o meu endereço atual do ngrok que está na porta 4040

def enviar():
    apiheroku = requests.get('https://example.herokuapp.com/') #Endereço do backend nodejs heroku
    if apiheroku.status_code==200:
        data = requests.get('http://127.0.0.1:4040/api/tunnels')
        if data.status_code==200:
            json = data.json()
            public_url = json['tunnels'][0]['public_url']
            payload={'url':public_url,'verify':'123456'} #trocar 123456 pela senha que a rota post do backend heroku espera para 'autenticar'
            r=requests.put('https://backend-sensor.herokuapp.com',json=payload) #Endereço do backend nodejs heroku
        
        
        
    
enviar()    



@app.route('/')
def temperatura():
    umid, temp = dht.read_retry(dht.DHT11, 4) # '4' É o pino da gpio que o DATA do dht11 está conectado
    return jsonify(dict(
                temperature=temp,
                humidity=umid,
                date=datetime.now().strftime("%d/%m/%y %H:%M:%S")
                ))


@app.route('/url')
def url():
    data = requests.get('http://127.0.0.1:4040/api/tunnels')
    json = data.json()
    public_url = json['tunnels'][0]['public_url']
    print(public_url)
    return jsonify(dict(
          url = public_url
        ))
        
  

app.run(host="0.0.0.0")