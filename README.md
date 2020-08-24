# SMART EYE - Raspberry Pi 3 + dht 11

*Flask + sensor de temperatura e umidade*

<br>

 Por [Wagner Sobreira](https://www.linkedin.com/in/wagner-sobreira-395b66167/)

<br>


💻 **Acesse a [API-Heroku](https://github.com/wagnersk/smart-eye-api-heroku)** | 
🖥  Você está em *Projeto Raspberry* |
📱 **Acesse o [Mobile](https://github.com/wagnersk/smart-eye-mobile)** |

<br>

### ⚠️  Requisitos Extras :

- *Sensor DHT11 de 4 pinos*
- *Protoboard*
- *4 cabos flats*
- *Resistor de 10k*
- *Modem Dwm 221*
- *Sistema operacional:  Raspberry Pi OS (32-bit) with desktop and recommended software*
<br>
  
  
<img src="/image/dht11circuit.png" >


                                             fonte: www.circuitbasics.com
                                             
<br>
                                  

*No final do README tem um *link de um curso sobre raspberry básico**

<br>



## 📑 Índice

- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Sobre o Projeto](#-sobre-o-projeto)
- [Executar esse projeto no seu computador raspberry Pi 3](#-como-executar-esse-projeto-no-seu-raspberry-pi-3)
- [Como incluir o ngrok em seu projeto para gerar um dns fixo](#EF%B8%8F-como-incluir-o-ngrok-em-seu-projeto-para-gerar-um-dns-fixo)
- [Configurações automáticas](#EF%B8%8F-configurações-automáticas)
- [Sequência de execução dos scripts](#EF%B8%8F-sequ%C3%AAncia-de-execu%C3%A7%C3%A3o-dos-scripts)
- [Referências](#-referências)
- [Autor](#%EF%B8%8F-autor)


<br><br>


## 🚀 Tecnologias utilizadas

- Python
- Flask
- Ngrok


<br><br>


## 💡 Sobre o Projeto

<br>

**SMART EYE  _making your life easier._**

<br>

> É um projeto para monitoramento prático de ambientes com temperatura controlada.<br>

> Este repositório não tem fins lucrativos , apenas refere-se a parte back-end do raspberry com um sensor DHT-11 para medição de temperatura e umidade.

<br><br>


## 📥 Como executar esse projeto no seu raspberry Pi 3


`sudo apt-get update `

`sudo apt-get install ppp usb-modeswitch wvdial`

`sudo pip3 install Adafruit_DHT`  

<br>

## ✅️ Como incluir o ngrok em seu projeto para gerar um dns fixo

1. [Clique Aqui](https://ngrok.com/) para criar uma conta no site do ngrok

2. *Baixe o ngrok para o seu raspberry*

3. `sudo ./ngrok authtoken 1231eddasfdgwwhrwef`

> O `1231eddasfdgwwhrwef` é um exemplo de um token pessoal que será gerado em sua conta pelo site , dessa forma o dns gerado não terá um tempo de expiração*

<br><br>

## 🤔️ Configurações automáticas

`mkdir $HOME/www/`

`cd $HOME/www/`

`git clone https://github.com/wagnersk/flask-raspberry-sensor-archives-example/`

`cd flask-raspberry-sensor-archives-example/`

`sudo mv **wvdial.conf** /etc/`

`sudo mv **usb_modeswitch.conf** /etc/`

*OBS: Em `usb_modeswitch` , voce irá alterar de acordo com as informações desse [TUTORIAL](https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial)*

<br>

## ✅️ Sequência de execução dos scripts

**1-`ligarmoden`** 

**2-`addmodemdefault`** 

**3-`ligarngrok`**

**4-`hello.py`**

*O Script hello.py tem comentários explicando o que você deverá alterar para adaptar a sua realidade*

OBS: O script **`hello.py`** precisa ser o ultimo a rodar pois ele vai enviar o endereço que o ngrok criou para o servidor no mongo db 
<br>

*Caso **não** tenha dado sudo reboot com o modem plugado, use o comando a seguir para ativar o modem*

`sudo usb_modeswitch -c /etc/usb_modeswitch.conf `
<br><br>

## 📕 Referências

[https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial](https://www.thefanclub.co.za/how-to/how-setup-usb-3g-modem-raspberry-pi-using-usbmodeswitch-and-wvdial)

[https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/](https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)

Curso raspberry Pi:

[https://www.youtube.com/watch?v=X7WMSfEfZGg&list=PLHz_AreHm4dnGZ_nudmN4rvyLk2fHFRzy](https://www.youtube.com/watch?v=X7WMSfEfZGg&list=PLHz_AreHm4dnGZ_nudmN4rvyLk2fHFRzy)

<br>

## 😎️ Autor

[Wagner Sobreira](https://www.linkedin.com/in/wagner-sobreira-395b66167/)
