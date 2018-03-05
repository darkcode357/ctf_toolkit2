#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import libs_python
import cmd

from .modulos.base.decode.decode16.decode16 import decode16
from .modulos.base.decode.decode32.decode32 import decode32
# decode(base)
from .modulos.base.decode.decode64.decode64 import decode64
# encodes(base)
from .modulos.base.encode.encode16 import encode16
from .modulos.base.encode.encode32 import encode32
from .modulos.base.encode.encode64 import encode64
# database
# connect
# hex
# scanner
# kernel_exploit
# web
# donwload
from .modulos.donwloads.baixar import baixarU
# gera_payload
from .modulos.gera_payloads.gera_payloads import payloads
from .modulos.hash.hashs import blake2b
from .modulos.hash.hashs import md5
from .modulos.hash.hashs import sha1
from .modulos.hash.hashs import sha224
from .modulos.hash.hashs import sha256
from .modulos.hash.hashs import sha384
from .modulos.hash.hashs import sha3_224
# encode(hash)
from .modulos.hash.hashs import sha3_256
from .modulos.hash.hashs import sha3_384
from .modulos.hash.hashs import sha3_512
from .modulos.hash.hashs import sha512


# wordlist_gene


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

                prompt = cores.azul + 'ctf@toolkit=>: ' + cores.vermelho
                intro = cores.amarelo + """bem vindo ao custon_pront_ctf_toolkit """

                doc_header = cores.vermelho + '[+]lista de todos os comandos[+]'
                misc_header = 'misc_header'
                undoc_header = cores.azul + '[+]comando de saida[+]'

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
                            ]

                def do_use(self, comando):
                    "comandos"
                    if comando and comando in self.comandos:
                        if comando == "encode16":
                            encode16()
                        elif comando == "encode32":
                            encode32()
                        elif comando == "encode64":
                            encode64()
                        elif comando == "decode16":
                            decode16()
                        elif comando == "decode32":
                            decode32()
                        elif comando == "decode64":
                            decode64()
                        elif comando == "baixar":
                            baixarU()
                        elif comando == "gera_payload":
                            payloads()
                        elif comando == "encode_sha3_256":
                            sha3_256()
                        elif comando == "encode_sha256":
                            sha256()
                        elif comando == "encode_blake2b":
                            blake2b()
                        elif comando == "encode_sha384":
                            sha384()
                        elif comando == "encode_md5":
                            md5()
                        elif comando == "encode_sha3_512":
                            sha3_512()
                        elif comando == "encode_sha512":
                            sha512()
                        elif comando == "encode_sha1":
                            sha1()
                        elif comando == "encode_sha3_224":
                            sha3_224()
                        elif comando == "encode_sha3_384":
                            sha3_384()
                        elif comando == "encode_sha224":
                            sha224()
                        elif comando == "clear":
                            from os import system as sys
                            sys("clear")

                    elif comando:
                        saida = "[+]comando incompleto=> [%s]" % comando
                    elif comando:
                        saida = "[+]comando incompleto=> [%s]" % comando
                    else:
                        saida = '[+]comando errado...'

                def complete_use(self, text, line, begidx, endidx):
                    # completa os comandos
                    if not text:
                        completions = self.comandos[:]
                    else:
                        completions = [f
                                       for f in self.comandos
                                       if f.startswith(text)
                                       ]
                    return completions

                def help_use(self):
                    print('\n'.join([cores.amarelo + "[+]use $modulo" + cores.verde]))
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

                def do_sair(self, line):
                    print("[+]obrigado por usar o ctf_toolkit")
                    exit(1)
                    return True


            ctf_promt().cmdloop()
        except EOFError:
            print("[+]digite sair")
    except KeyboardInterrupt:
        print("[+]digite sair......")
