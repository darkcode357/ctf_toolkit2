'''
md5
sha1
sha224
sha256
sha384
sha512
'''
import hashlib


def sha3_256():
    encde = input("[sha3_256]=>")
    hash = hashlib.sha3_256()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha256():
    encde = input("[sha256]=>")
    hash = hashlib.sha256()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def blake2b():
    encde = input("[blake2b]=>")
    hash = hashlib.blake2b()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha384():
    encde = input("[sha384]=>")
    hash = hashlib.sha384()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def md5():
    encde = input("[md5]=>")
    hash = hashlib.md5()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha3_512():
    encde = input("[sha3_512]=>")
    hash = hashlib.sha3_512()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha512():
    encde = input("[sha512]=>")
    hash = hashlib.sha512()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha1():
    encde = input("[sha1]=>")
    hash = hashlib.sha1()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha3_224():
    encde = input("[sha3_224]=>")
    hash = hashlib.sha3_224()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def blake2s():
    encde = input("[blake2s]=>")
    hash = hashlib.blake2s()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha3_384():
    encde = input("[sha3_384]=>")
    hash = hashlib.sha3_384()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())


def sha224():
    encde = input("[sha224]=>")
    hash = hashlib.sha224()
    hash.update(encde.encode('utf-8'))
    print(hash.hexdigest())
