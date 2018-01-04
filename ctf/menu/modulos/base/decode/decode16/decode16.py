def decode16():
    try:
        decode = input("decode(16)=>")
        import base64
        import binascii
        print(base64.b16decode(decode))
    except binascii.Error as e:
        print("nao e base16(%s)"%decode)