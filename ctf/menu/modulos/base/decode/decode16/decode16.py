cyanClaro = "\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
amarelo = '\033[1;33m'
ciano = '\033[46m'
magenta = '\033[45m'
def decode16():
    try:
        decode = input("decode(16)=>")
        import base64
        import binascii
        print(str(base64.b16decode(decode))[2:-1])
    except binascii.Error as e:
        print("nao e base16(%s)"%decode)
