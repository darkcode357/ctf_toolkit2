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
# prompt
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.key_binding.bindings.completion import display_completions_like_readline
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token

# donwload
from .modulos.donwloads.baixar import baixarU
# imports
# gera_payloads
from .modulos.gera_payloads.gera_payloads import payloads
from .modulos.hash.hashs import *
# reverse_shell
from .modulos.os.reverse_shell.servidor_tcp import main

#lelei anasp


registry = load_key_bindings()
registry.add_binding(Keys.ControlI)(display_completions_like_readline)

example_style = style_from_dict({
    # User input.
    Token: '#001EB6',

    # Prompt.
    Token.Username: '#0074FF',
    Token.At: '#FF0000',
    Token.Colon: '#FF0000',
    Token.Pound: '#FF0000',
    Token.Host: '#FF0000 bg:#aaaaff',
    Token.Path: '#FF0000 underline',
})

animal_completer = WordCompleter([

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
    'use encode64',
    'use encode32',
    'use encode16',
    'use decode64',
    'use decode16 ',
    'use decode32',
    'use ssh',
    'use ftp',
    'use gera_wordlist',
    'use reverse_tcp',
    'use baixar',
    'use gera_payload',
    'comandos'
], meta_dict={
    'use encode_sha3_256': "encode_sha3_256",
    'use encode_sha256': "encode_sha3_256",
    'use encode_blake2b': "encode_sha3_256",
    'use encode_sha384': "encode_sha3_256",
    'use encode_md5': "encode_sha3_256",
    'use encode_sha3_512': "encode_sha3_256",
    'use encode_sha512': "encode_sha3_256",
    'use encode_sha1': "encode_sha3_256",
    'use encode_sha3_224': "encode_sha3_256",
    'use encode_blake2s': "encode_sha3_256",
    'use encode_sha3_384': "encode_sha3_256",
    'use encode_sha224': "encode_sha3_256",
    'use encode64': "encode texto para base64",

    'use encode32': "encode texto para base32",

    'use encode16': "encode texto para base16",

    'use decode64': "decode base64 para texto",

    'use decode16': "decode base16 para texto",

    'use decode32': "decode base32 para texto",

    'use baixar': "baixa arquivos",

    'use ssh': "inicia sessao com ssh",

    'use ftp': "inicia sessao com ftp",

    'use gera_wordlist': "gera wordlist",

    'use reverse_tcp': "inicia reverse_shell",

    'use gera_payload': "gera payload",
    "comandos": "lista todos os comandos do ctf_toolkit"
}, ignore_case=True)




def menu():
    while True:
        menu = prompt('ctf@toolkit=>: ', completer=animal_completer,
                      key_bindings_registry=registry,

                      # Important: for this to work: `complete_while_typing` needs
                      #            to be False.
                      complete_while_typing=True, style=example_style)
        try:
            try:
                if menu == "help use":
                    print("%s[+]%s use comandos" % (amarelo, azul))
                elif menu == "list":
                    list()
                elif menu == "clean":
                    import os;

                    os.system("clear")
                    list()
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
                elif menu == "info base64":
                    help_base64()
                elif menu == "use reverse_tcp":
                    main()
                elif menu == "use baixar":
                    baixarU()
                elif menu == "use gera_payload":
                    payloads()
                elif menu == 'use encode_sha3_256':
                    sha3_256()
                elif menu == 'use encode_sha256':
                    sha256()
                elif menu == 'use encode_blake2b':
                    blake2b()
                elif menu == 'use encode_sha384':
                    sha384()
                elif menu == 'use encode_md5':
                    md5()
                elif menu == 'use encode_sha3_512':
                    sha3_512()
                elif menu == 'use encode_sha512':
                    sha512()
                elif menu == 'use encode_sha1':
                    sha1()
                elif menu == 'use encode_sha3_224':
                    sha3_224()
                elif menu == 'use encode_blake2s':
                    blake2s()
                elif menu == 'use encode_sha3_384':
                    sha3_384()
                elif menu == 'use encode_sha224':
                    sha224
                elif menu == "sair":
                    print("%s[+]%sobrigado por usar o ctf_toolkit" % (amarelo, azul))
                    print("%s[+]%scriador darkcode" % (amarelo, azul))
                    exit(1)
            except EOFError:
                print(amarelo + "digite help")

        except KeyboardInterrupt as e:
            print(amarelo + "digite help")
