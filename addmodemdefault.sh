#!/bin/bash

# Esse script irá matar seu default gateway e 
# Adicionar o modem como default gateway ppp0 primário

sudo route del default
sudo route add default ppp0
