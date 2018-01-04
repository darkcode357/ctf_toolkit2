def encode32():
    try:
        encode = input("encode(32)=>")
        import base64,binascii
        dsa = base64.b32encode(bytes(encode, 'utf-8'))
        print(dsa)
    except binascii.Error as e:
        print("nao e base32(%s)"%encode)