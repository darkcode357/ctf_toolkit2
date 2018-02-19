def decode16():
    try:
        decode = input("decode(16)=>")
        import base64
        import binascii
        print(str(base64.b16decode(decode))[2:-1])
    except binascii.Error as e:
        print("nao e base16(%s)"%decode)
