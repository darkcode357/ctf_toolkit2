#!/usr/bin/env python
# -*- coding: utf-8 -*-
cyanClaro = "\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
amarelo = '\033[1;33m'
ciano = '\033[46m'
magenta = '\033[45m'
# sair
# reverse_shell
# wordlist
# decode
# encode
# ssh
# ftp
# documentacao do s modulos
# documentacao do s modulos
# decode
# encode
# imports
# wordlist
# ftp
# ssh
# imports
# sair
from sys import exit

# wordlist
# decode
# encode
# ssh
# ftp
# documentacao do s modulos
# documentacao do s modulos
from menu.documentacao.info import help_base64
from menu.documentacao.info import list
from menu.modulos.base.decode.decode16.decode16 import decode16
from menu.modulos.base.decode.decode32.decode32 import decode32
# decode
from menu.modulos.base.decode.decode64.decode64 import decode64
from menu.modulos.base.encode.encode16 import encode16
from menu.modulos.base.encode.encode32 import encode32
# encode
from menu.modulos.base.encode.encode64 import encode64
# imports
# wordlist
from menu.modulos.brute_force.gera_wordlist import gera_wrdlist
# ftp
from menu.modulos.os.servicos.ftp.ftp import ftp
# ssh
from menu.modulos.os.servicos.ssh.ssh import ssh

# donwload
from .modulos.donwloads.baixar import baixarU
# imports
# gera_payloads
from .modulos.gera_payloads.gera_payloads import payloads
# reverse_shell
from .modulos.os.reverse_shell.servidor_tcp import main


#lelei anasp

def menu():
    while True:
        try:
            menu = input(azul+u'\u27a4'+vermelho)

            if menu == "help use":
                use()
            elif menu == "list":
                list()
            elif menu =="clean":
                import os;os.system("clear")
                list()
                use()
                del os
            elif menu == "use decode64":
                decode64()
            elif menu == "use encode64":
                encode64()
            elif menu == "use decode32":
                decode32()
            elif menu == "use encode32":
                encode32()
            elif menu == "use decode16":
                decode16()
            elif menu == "use encode16":
                encode16()
            elif menu == "use ssh":
                ssh()
            elif menu == "use ftp":
                ftp()
            elif menu == "use gera_wordlist":
                gera_wrdlist()
            elif menu == "comandos":
                list()
            elif menu =="info base64":
                help_base64()
            elif menu == "use reverse_tcp":
                main()
            elif menu == "use baixar":
                baixarU()
            elif menu == "use gera_payload":
                payloads()
            elif menu =="sair":
                exit(1)
        except KeyboardInterrupt as e:
            print(amarelo+"digite help")
