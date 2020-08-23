# Raspberry PI 3 + DHT11


### Requisitos Extras :

- Sensor DHT11 de 4 pinos
- Protoboard
- 4 cabos flats
- Resistor de 10k
- Modem Dwm 221  
- Sistema operacional:  Raspberry Pi OS (32-bit) with desktop and recommended software  
  
  
<img src="/image/dht11circuit.png">


                                             fonte: www.circuitbasics.com
                                  

*No final do README tem um *link de um curso sobre raspberry básico**




# Configurações iniciais

`sudo apt-get update `

`sudo apt-get install ppp usb-modeswitch wvdial`

`sudo pip3 install Adafruit_DHT`  

### Criar uma conta no site do [NGROK](https://ngrok.com/)

1. *Baixar o ngrok para o seu raspberry*

2. `sudo ./ngrok authtoken 1231eddasfdgwwhrwef`

> O `1231eddasfdgwwhrwef` é um exemplo de um token pessoal que será gerado em sua conta pelo site , dessa forma o dns gerado não terá um tempo de expiração*


### Use os comandos

`mkdir $HOME/www/`

`cd $HOME/www/`

`git clone https://github.com/wagnersk/flask-raspberry-sensor-archives-example/`

`cd flask-raspberry-sensor-archives-example/`

`sudo mv **wvdial.conf** /etc/`

`sudo mv **usb_modeswitch.conf** /etc/`

*OBS: Em `usb_modeswitch` , voce irá alterar de acordo com as informações desse [TUTORIAL](https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial)*



## Sequelncia de execução do scripts

**1-`ligarmoden`** 

**2-`addmodemdefault`** 

**3-`ligarngrok`**

**4-`hello.py`**

*O Script hello.py tem comentários explicando o que você deverá alterar para adaptar a sua realidade*

OBS: O script **`hello.py`** precisa ser o ultimo a rodar pois ele vai enviar o endereço que o ngrok criou para o servidor no mongo db 


*Caso **não** tenha dado sudo reboot com o modem plugado, use o comando a seguir para ativar o modem*

`sudo usb_modeswitch -c /etc/usb_modeswitch.conf `


# Referências :

[https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial](https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial)

[https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/](https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)

Curso raspberry Pi:

[https://www.youtube.com/watch?v=X7WMSfEfZGg&list=PLHz_AreHm4dnGZ_nudmN4rvyLk2fHFRzy](https://www.youtube.com/watch?v=X7WMSfEfZGg&list=PLHz_AreHm4dnGZ_nudmN4rvyLk2fHFRzy)


## 📕 Autor

[Wagner Sobreira](https://www.linkedin.com/in/wagner-sobreira-395b66167/)
