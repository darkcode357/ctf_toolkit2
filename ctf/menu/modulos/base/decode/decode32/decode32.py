def decode32():
    try:
        decode = input("decode(32)=>")
        import base64
        import binascii
        print(str(base64.b32decode(decode))[2:-1])
    except binascii.Error as e:
        print("nao e base32(%s)"%decode)
