def encode64():
    try:
        encode = input("encode(64)=>")
        import base64,binascii
        dsa = base64.b64encode(bytes(encode, 'utf-8'))
        print(dsa)
    except binascii.Error as e:
        print("nao e base64(%s)"%encode)