def decode32():
    try:
        decode = input("decode(32)=>")
        import base64
        import binascii
        print(base64.b32decode(decode))
    except binascii.Error as e:
        print("nao e base32(%s)"%decode)
