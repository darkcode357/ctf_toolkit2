def packs():
    from os import system as sys
    modoff = "modulo nao instalado =>"
    modon =  "modulo instalado =>"
    libs = ['python-nmap','dsa']
    try:
        import nmap
    except ImportError as e:
        print(modoff+e)
    try:
        import base64
    except ImportError as e:
        print(e)
    try:
        import prompt_toolkit
    except ImportError as e:
        sys("pip3 install prompt_toolkit")
