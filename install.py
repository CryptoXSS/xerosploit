#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

#---------------------------------------------------------------------------#
# Este archivo es parte de Xerosploit.                                      #
# Xerosploit es un software gratuito: puedes redistribuirlo y / o modificarlo #
# bajo los términos de la Licencia Pública General GNU publicada por        #
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o        #
# (a su elección) cualquier versión posterior.                              #
#                                                                           #
# Xerosploit se distribuye con la esperanza de que sea útil,                #
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de           # 
# COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. Ver el            #
# Licencia pública general GNU para más detalles.                           #
#                                                                           #
# Debería haber recibido una copia de la Licencia Pública General GNU       #
# junto con Xerosploit. Si no, vea <http://www.gnu.org/licenses/>.          #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2016 LionSec (www.lionsec.net)                         #
#                                                                           #
#---------------------------------------------------------------------------#

if not os.geteuid() == 0:
    sys.exit(
	    """\033[1;91m\n[!]El instalador de Xerosploit debe ejecutarse como root. ¯\_(ツ)_/¯\n\033[1;m""")

print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                  █████████████████████████████               █
█                  ██ Instalador de Xerosploit██               █ 
█                  █████████████████████████████               █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

def main():

   print("\033[1;34m\n[++] Elija su sistema operativo.\033[1;m")

   print("""
1) Ubuntu / Kali linux / Otros
2) Parrot OS
""")
	system0 = raw_input(">>> ")
	if system0 == "1":
		print("\033[1;34m\n[++] Instalación de Xerosploit ... \033[1;m")
		install = os.system(
			"apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables")

		
		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/xerosploit && cp -R tools/ /opt/xerosploit/ && cp xerosploit.py /opt/xerosploit/xerosploit.py && cp banner.py /opt/xerosploit/banner.py && cp run.sh /usr/bin/xerosploit && chmod +x /usr/bin/xerosploit && tput setaf 34; echo "Xerosploit has been sucessfuly instaled. Execute 'xerosploit' in your terminal." """)	
            elif system0 == "2":
		print("\033[1;34m\n[++] Installing Xerosploit ... \033[1;m")

		
		
		bet_un = os.system("apt-get remove bettercap") # Retire bettercap para evitar algunos problemas. Instalado por defecto con apt-get.
		
		bet_re_ins = os.system("gem install bettercap") # Reinstale bettercap con gema.

		install = os.system(
			"apt-get update && apt-get install -y nmap hping3 ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/xerosploit && cp -R tools/ /opt/xerosploit/ && cp xerosploit.py /opt/xerosploit/xerosploit.py && cp banner.py /opt/xerosploit/banner.py && cp run.sh /usr/bin/xerosploit && chmod +x /usr/bin/xerosploit && tput setaf 34; echo "Xerosploit has been sucessfuly instaled. Execute 'xerosploit' in your terminal." """)
		

	    else:
		print("
                        Seleccione la opción 1 o 2")
		main()
		
		
		
main()
