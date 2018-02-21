import codecs


def hex_encode():
    h_e = input("encode[hex]=>")
    hexlify = codecs.getencoder('hex')
    print(str(bytes(hexlify(h_e)[0])[2:-1]))


hex_encode()
