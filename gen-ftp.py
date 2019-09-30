#!/usr/bin/python 
# -*- coding: utf-8 -*-
#Copyright 2019 gen-ftp
#Written by: Adrian Guillermo
#Facebook: Adrian Guillero
#Github: https://www.github.com/AdrMXR

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

import urllib
import os 
import time
from time import sleep
from sys import stdout, argv, exit
from getch import pause
import webbrowser

def check(host='https://www.google.com'):
	print("{}Verificando su conexion a internet...").format(GREEN)
	time.sleep(0.5)
	try:
		urllib.urlopen(host)
		print("{}Conexion a internet exitosa").format(GREEN)
		time.sleep(0.5)
		banner()
	except:
		print("{}Verifique su conexion a internet para utilizar GEN-FTP").format(RED)
		exit(0)

def banner():
	os.system('clear')
	print ('''
	
	 ██████╗ ███████╗███╗   ██╗    ███████╗████████╗██████╗ 
	██╔════╝ ██╔════╝████╗  ██║    ██╔════╝╚══██╔══╝██╔══██╗
	██║  ███╗█████╗  ██╔██╗ ██║    █████╗     ██║   ██████╔╝	
	██║   ██║██╔══╝  ██║╚██╗██║    ██╔══╝     ██║   ██╔═══╝ 
	╚██████╔╝███████╗██║ ╚████║    ██║        ██║   ██║     
	 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝        ╚═╝   ╚═╝     ''').format(GREEN)
	print '{}------------------------------------------------------'.format(WHITE).center(77)
	print '{}GENERADOR DE SERVIDORES FTP'.format(RED).center(76)
	print '{0}Creado por: {3}Adrian Guillermo {2}({1}AdrMXR{2}) {0}Version: {3}1.0{2}{3}'.format(YELLOW, RED, YELLOW, BLUE).center(117)
	print '{}------------------------------------------------------'.format(WHITE).center(77)

def private(): #Servidor FTP local
	print("Instalando requerimientos...")
	time.sleep(3)
	os.system('sudo apt-get install vsftpd')
	time.sleep(2)
	os.system('systemctl stop vsftpd')
	user = raw_input('Ingrese un nombre de usuario: ')
	os.system('adduser {0} --force-badname'.format(user))
	carpet = raw_input("Ingrese un nombre para su carpeta de archivos ftp: ")
	time.sleep(2)
	print("Realizando configuraciones FTP...")
	time.sleep(4)
	os.system('sudo chown root:root /home/{0} && sudo mkdir /home/{0}/{1} && sudo chown {0}:{0} /home/{0}/{1}'.format(user, carpet))
	directory = os.getcwd()
	os.system('sudo cp {0}/archftp /bin/archftp && sudo echo /bin/archftp >> /etc/shells && sudo usermod {1} -s /bin/archftp && sudo cp {0}/vsftpd.conf /etc/vsftpd.conf && systemctl restart vsftpd'.format(directory, user))

	if raw_input("¿Desea acceder a su servidor FTP? (y/n)\n{0}GenFTP >>{1} ".format(RED, WHITE)).upper() != "Y":
		print("GRACIAS POR UTILIZAR GEN-FTP")
		exit(0)
	os.system('ftp localhost')


def public(): #Servidor FTP publico
	if raw_input("¿Ya cuenta con un servidor FTP local? (y/n)\n{0}GenFTP >>{1} ".format(RED, WHITE)).upper() != "Y":
		print("Creando servidor local FTP...")
		time.sleep(2)
		private()
	servidor = raw_input("Introduzca su gateway (puerta de enlace de su router): ")
	time.sleep(2)
	print("A continuacion se abrira la puerta de enlace de su router, configure los puertos correspondientes.")
	time.sleep(3)
	webbrowser.open("http://{0}".format(servidor))
	time.sleep(3)
	pause("Una vez terminado, presione una tecla para continuar...")
	os.system('systemctl restart vsftpd')
	print("Tu servidor FTP publico deberia estar listo.")
	time.sleep(3)
	print("GRACIAS POR UTILIZAR GEN-FTP")
	exit(0)

def menu():
	option = input("¿Que tipo de servidor FTP desea?\n\n[1] --- Local\n\n[2] --- Publico\n\n{0}GenFTP >>{1} ".format(RED, WHITE))
	if option == 1:
		private()
	elif option == 2:
		public()
	else:
		return menu()

#Ejecucion de funciones
check()
banner()
menu()

	
	










