#!/bin/bash

# Esse script irá monitorar o wvdial e tentar executar ele dnv
# a cada 10 segundos para manter o modem sempre ativo

{
	while : ; do
		sudo wvdial
		sleep 10
	done
	
}

