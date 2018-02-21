import itertools
def gera_wrdlist():
    def intUP():
        min = input("minimo de caractere=>[" + "]")
        max = input("maximo de caractere=>[" + "]")
        chrs = 'abcdefghijklmnopqrstuvwxyz1234567890'.upper()

        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                print(''.join(xs))
    def strUp():
        min = input("minimo de caractere=>[" + "]")
        max = input("maximo de caractere=>[" + "]")
        chrs = 'abcdefghijklmnopqrstuvwxyz'.upper()

        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                print(''.join(xs))
    def str():
        min = input("minimo de caractere=>[" + "]")
        max = input("maximo de caractere=>[" + "]")
        chrs = 'abcdefghijklmnopqrstuvwxyz'

        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                print(''.join(xs))
    def str_int():
        min = input("minimo de caractere=>[" + "]")
        max = input("maximo de caractere=>[" + "]")
        chrs = 'abcdefghijklmnopqrstuvwxyz1234567890'

        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                print(''.join(xs))
    def full():
        min = input("minimo de caractere=>[" + "]")
        max = input("maximo de caractere=>[" + "]")
        chrs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=_+]}|/?.,><"'

        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                print(''.join(xs))


    check = input("voce gostaria \n"
                  "[+]full_generate[abcdefghijklmnopqrstuvwxyz1234567890-=_+]}|/?.,><']=[1]"
                  "\n[+]wordlistSTR[abcdefghijklmnopqrstuvwxyz]=[2]\n"
                  "[+]wordlist[str+int]=[abcdefghijklmnopqrstuvwxyz1234567890]=[3]\n"
                  "[+]wordlist[upper]=[4]\n"
                  "[+]wordlist[upper+int]=[5]\n"
                  "=>")
    if check =="1":
        print("[+]full_generate[abcdefghijklmnopqrstuvwxyz1234567890-=_+]}|/?.,><']")
        full()
    elif check =="2":
        print("[+]wordlistSTR[abcdefghijklmnopqrstuvwxyz]")
        str()
    elif check == "3":
        print("[+]wordlist[str+int]=[abcdefghijklmnopqrstuvwxyz1234567890]")
        str_int()
    elif check == "4":
        print("[+]wordlist[upper]=[4]")
        strUp()
    elif check == "5":
        print("[+]wordlist[upper+int]=[5]")
        intUP()
    else:
        print("[+]comando errado.....")
        pass
