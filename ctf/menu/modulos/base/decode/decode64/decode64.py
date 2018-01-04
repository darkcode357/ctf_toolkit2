def decode64():
    try:
        import base64
        import binascii
        decode = input("decode(64)=>")
        d = base64.b64decode(decode)
        print("base64(%s)"%d)
    except binascii.Error as e:
        print("erro nao e uma base64=>(%s)"%decode)
