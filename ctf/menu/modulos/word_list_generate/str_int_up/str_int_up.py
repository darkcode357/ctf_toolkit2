import errno
import itertools
import os


def str_int_up():
    try:
        os.makedirs("../../files/wordlist/str_int_up/")
        print("[criando pasta wordlist/str_int_up][OK]")
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    word_list_name = input("[+]nome da wordlist=>")
    min = input("minimo de caractere=>[" + "]")
    max = input("maximo de caractere=>[" + "]")
    chrs = 'abcdefghijklmnopqrstuvwxyz1234567890'.upper()
    with open("../../files/wordlist/str_int_up/" + word_list_name, "w") as fl:
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                dsa = fl.write(''.join(xs) + "\n")
