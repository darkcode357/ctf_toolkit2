#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import libs_python
import sys
import cmd

#encodes(base)
from .modulos.base.encode.encode16 import encode16
from .modulos.base.encode.encode32 import encode32
from .modulos.base.encode.encode64 import encode64

#decode(base)
from .modulos.base.decode.decode64.decode64 import decode64
from .modulos.base.decode.decode16.decode16 import decode16
from .modulos.base.decode.decode32.decode32 import decode32

#database
#connect
#hex
#scanner
#kernel_exploit
#web
#donwload
from .modulos.donwloads.baixar import baixarU

#gera_payload
from .modulos.gera_payloads.gera_payloads import payloads

#encode(hash)
from .modulos.hash.hashs import sha3_256
from .modulos.hash.hashs import sha512
from .modulos.hash.hashs import sha256
from .modulos.hash.hashs import sha224
from .modulos.hash.hashs import sha3_224
from .modulos.hash.hashs import sha1
from .modulos.hash.hashs import sha3_384
from .modulos.hash.hashs import sha3_512
from .modulos.hash.hashs import sha384
from .modulos.hash.hashs import blake2s
from .modulos.hash.hashs import blake2b
from .modulos.hash.hashs import md5
#wordlist_gene
from .modulos.word_list_generate.especial.especial import especial
from .modulos.word_list_generate.int.int import _int
from .modulos.word_list_generate.int_especial.int_especial import int_especial
from .modulos.word_list_generate.str.str import _str
from .modulos.word_list_generate.str_especial.str_especial import str_especial
from .modulos.word_list_generate.str_int.str_int import str_especial
from .modulos.word_list_generate.str_int_especial.str_int_especial import str_int_especial
from .modulos.word_list_generate.str_int_up.str_int_up import str_int_up
from .modulos.word_list_generate.str_up.str_up import str_up
from .modulos.word_list_generate.str_up_especial.str_up_especial import str_up_especial




class cores:
    cyanClaro = "\033[1;36m"
    vermelho = '\033[31;1m'
    verde = '\033[32;1m'
    azul = '\033[34;1m'
    normal = '\033[0;0m'
    amarelo = '\033[1;33m'
    ciano = '\033[46m'
    magenta = '\033[45m'


while True:
    try:
        try:
            class ctf_promt(cmd.Cmd):
                """
            ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗      ██████╗████████╗ ██████╗
            ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝     ██╔════╝╚══██╔══╝██╔════╝
            ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║        ██║        ██║   ██║  ███╗
            ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║        ██║        ██║   ██║   ██║
            ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║███████╗╚██████╗   ██║   ╚██████╔╝
            ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝

                """

                prompt = cores.azul+'ctf@toolkit=>: '+cores.vermelho
                intro = cores.amarelo+"""bem vindo ao custon_pront_ctf_toolkit """

                doc_header = cores.vermelho+'[+]lista de todos os comandos[+]'
                misc_header = 'misc_header'
                undoc_header = cores.azul+'[+]comando de saida/info[+]'

                ruler = '-'

                def do_prompt(self, line):
                    "Change the interactive prompt"
                    self.prompt = line + ': '
                comandos = ['clear',
                            'decode64',
                            'decode32',
                            'decode16',
                            'encode64',
                            'encode32',
                            'encode16',
                            'ssh',
                            'ftp',
                            'gera_wordlist',
                            'reverse_tcp',
                            'baixar',
                            'gera_payload',
                            'encode_sha3_256',
                            'encode_sha256',
                            'encode_blake2b',
                            'encode_sha384',
                            'encode_md5',
                            'encode_sha3_512',
                            'encode_sha512',
                            'encode_sha1',
                            'encode_sha3_224',
                            'encode_blake2s',
                            'encode_sha3_384',
                            'encode_sha224',
                            'sair',
                            'wordlist_especial',
                            'wordlist_int',
                            'wordlist_int_especial',
                            'wordlist_str',
                            'wordlist_str_especial',
                            'wordlist_str_int_especial',
                            'wordlist_str_int_up',
                            'wordlist_str_up',
                            'wordlist_str_up_especial',

                ]

                def do_banner(self,line):
                    print(cores.vermelho + """


                                      | |__|__|__|__|__|__|__|__|__|_|                         
                 __    __    __       |_|___|___|___|___|___|___|___||       __    __    __   
                |__|  |__|  |__|      |___|___|___|___|___|___|___|__|      |__|  |__|  |__|   
                |__|__|__|__|__|       \____________________________/       |__|__|__|__|__|   
                |_|___|___|___||        |_|___|___|___|___|___|___||        |_|___|___|___||
                |___|___|___|__|        |___|___|___|___|___|___|__|        |___|___|___|__|   
                 \_|__|__|___|/          \________________________/          \_|__|__|__|_/    
                  \__|____|__/            |___|___|___|___|___|__|            \__|__|__|_/     
                   |||_|_|_||             |_|___|___|___|___|__|_|             |_|_|_|_||      
                   ||_|_|||_|__    __    _| _  __ |_ __  _ __  _ |_    __    __||_|_|_|_|      
                   |_|_|_|_||__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|_|_|_|_||      
                   ||_|||_|||___|___|___|___|___|___|___|___|___|___|___|___|__||_|_|_|_|      
                   |_|_|_|_||_|___|___|___|___|___|___|___|___|___|___|___|___||_|_|_|_||      
                   ||_|_|_|_|___|___|___|___|___|___|___|___|___|___|___|___|__||_|_|_|_|      
                   |_|||_|_||_|___|___|___|___|___|___|___|___|___|___|___|___||_|_|_|_||      
                   ||_|_|_|_|___|___|___|___|___|_/| | | \__|___|___|___|___|__||_|_|_|_|      
                   |_|_|_|_||_|___|___|___|___|__/ | | | |\___|___|___|___|___||_|_|_|_||      
                   ||_|_|_|||___|___|___|___|___|| | | | | |____|___|___|___|__||_|_|_|_|      
                   |_|_|_|_||_|___|___|___|___|_|| | | | | |__|___|___|___|___||_|_|_|_||      
                  /___|___|__\__|___|___|___|___|| | | | | |____|___|___|___|_/_|___|__|_\     
                 |_|_|_|_|_|_||___|___|___|___|_|| | | | | |__|___|___|___|__|_|__|__|__|_|    
                 ||_|_|_|_|_|_|_|___|___|___|___||_|_|_|_|_|____|___|___|____|___|__|__|__|    
                %s
                 ██████╗████████╗███████╗       ██████╗ █████╗ ███████╗████████╗██╗     ███████╗
                ██╔════╝╚══██╔══╝██╔════╝      ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║     ██╔════╝
                ██║        ██║   █████╗  █████╗██║     ███████║███████╗   ██║   ██║     █████╗  
                ██║        ██║   ██╔══╝  ╚════╝██║     ██╔══██║╚════██║   ██║   ██║     ██╔══╝  
                ╚██████╗   ██║   ██║           ╚██████╗██║  ██║███████║   ██║   ███████╗███████╗
                 ╚═════╝   ╚═╝   ╚═╝            ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝
                criado darkcode0x00
                versao 0.4.4
                data 5/3/18
                    """ % cores.amarelo)
                def do_use(self, comando):
                    "comandos"
                    if comando and comando in self.comandos:
                        if comando == "encode16":
                            encode16()
                        elif comando =="encode32":
                            encode32()
                        elif comando =="encode64":
                            encode64()
                        elif comando =="decode16":
                            decode16()
                        elif comando =="decode32":
                            decode32()
                        elif comando =="decode64":
                            decode64()
                        elif comando =="baixar":
                            baixarU()
                        elif comando =="gera_payload":
                            payloads()
                        elif comando =="encode_sha3_256":
                            sha3_256()
                        elif comando =="encode_sha256":
                            sha256()
                        elif comando =="encode_blake2b":
                            blake2b()
                        elif comando =="encode_sha384":
                            sha384()
                        elif comando =="encode_md5":
                            md5()
                        elif comando =="encode_sha3_512":
                            sha3_512()
                        elif comando =="encode_sha512":
                            sha512()
                        elif comando =="encode_sha1":
                            sha1()
                        elif comando =="encode_sha3_224":
                            sha3_224()
                        elif comando =="encode_sha3_384":
                            sha3_384()
                        elif comando =="encode_sha224":
                            sha224()
                        elif comando =="wordlist_especial":
                            especial()
                        elif comando == "wordlist_int":
                            _int()
                        elif comando == "wordlist_int_especial":
                            int_especial()
                        elif comando == "wordlist_str":
                            _str()
                        elif comando == "wordlist_str_especial":
                            str_especial()
                        elif comando == "wordlist_str_int_especial":
                            str_int_especial()
                        elif comando == "wordlist_str_int_up":
                            str_int_up()
                        elif comando == "wordlist_str_up":
                            str_up()
                        elif comando == "wordlist_str_up_especial":
                            str_up_especial()
                        elif comando =="clear":
                            from os import system as sys
                            sys("clear")

                    elif comando:
                        saida = "[+]comando incompleto=> [%s]" % comando
                    elif comando:
                        saida = "[+]comando incompleto=> [%s]" % comando
                    else:
                        saida = '[+]comando errado...'

                def complete_use(self, text, line, begidx, endidx):
                    #completa os comandos
                    if not text:
                        completions = self.comandos[:]
                    else:
                        completions = [f
                                       for f in self.comandos
                                       if f.startswith(text)
                                       ]
                    return completions

                def help_use(self):
                    print('\n'.join([cores.amarelo+"[+]use $modulo"+cores.verde]))
                    comandos = ['clear',
                                'use decode64',
                                'use decode32',
                                'use decode16',
                                'use encode64',
                                'use encode32',
                                'use encode16',
                                'use ssh',
                                'use ftp',
                                'use gera_wordlist',
                                'use comandos',
                                'use reverse_tcp',
                                'use baixar',
                                'use gera_payload',
                                'use encode_sha3_256',
                                'use encode_sha256',
                                'use encode_blake2b',
                                'use encode_sha384',
                                'use encode_md5',
                                'use encode_sha3_512',
                                'use encode_sha512',
                                'use encode_sha1',
                                'use encode_sha3_224',
                                'use encode_blake2s',
                                'use encode_sha3_384',
                                'use encode_sha224',
                                'sair',
                                ]
                    for i in comandos:
                        print(i)


                def do_sair(self,line):
                    print("[+]obrigado por usar o ctf_toolkit")
                    exit(1)
                    return True




            ctf_promt().cmdloop()
        except EOFError:
            print("[+]digite sair")
    except KeyboardInterrupt:
        print("[+]digite sair......")