def encode16():
    try:
        encode = input("encode(16)=>")
        import base64,binascii
        dsa = base64.b16encode(bytes(encode, 'utf-8'))
        print(dsa)
    except binascii.Error as e:
        print("nao e base16(%s)"%encode)