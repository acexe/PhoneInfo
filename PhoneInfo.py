#simbolos {} +
autor = '@alexis.z40'

import requests
import json
import os
import platform
import time
from colorama import *

sistema = platform.system()

if sistema == 'Windows':
    os.system("cls")
else:
    os.system("clear")

while True:
        print("╭━━━┳╮╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╱╭━╮")
        print("┃╭━╮┃┃╱╱╱╱╱╱╱╱╱╱╱╰┫┣╯╱╱┃╭╯")
        print("┃╰━╯┃╰━┳━━┳━╮╭━━╮╱┃┃╭━┳╯╰┳━━╮")
        print("┃╭━━┫╭╮┃╭╮┃╭╮┫┃━┫╱┃┃┃╭╋╮╭┫╭╮┃")
        print("┃┃╱╱┃┃┃┃╰╯┃┃┃┃┃━┫╭┫┣┫┃┃┃┃┃╰╯┃")
        print("╰╯╱╱╰╯╰┻━━┻╯╰┻━━╯╰━━┻╯╰┻╯╰━━╯")
        print(Fore.RED + "                                         code by @alexis.z40" + Fore.RESET)
        print("\n")
        print(Fore.RED + "Solo poner el numero, ningun otro caracter que no sea un numero" + Fore.RESET)
        numero = int(input("Introduce numero: "))

        def num(apikey,country,numero):
            agent = {'User-Agent':'Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
            print(Fore.GREEN + "Escaneando...." + Fore.RESET)
            pe = requests.get(
                'http://apilayer.net/api/validate?access_key={}&number={}&country_code={}&format=1'.format(apikey,numero,country),
                headers=agent
                )
            data = json.loads(pe.text)
            for d in data:
                print('[+] {}: {}'.format(d, data[d]))
        num(apikey='3f50fee2695691f9e473629818026355',country='MX', numero=numero)

        print("\n")
        print("1 Repetir proceso")
        print("2 Salir")

        op = int(input("Opcion: "))

        if op ==1:
            print(Fore.GREEN + "Repitiendo proceso." + Fore.RESET)
            time.sleep(1)
            if sistema == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
        elif op ==2:
            if sistema == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
            print(Fore.RED + "Saliendo" + Fore.RESET)
            time.sleep(2)
            break
        else:
            print("OPCION NO DISPONIBLE")
