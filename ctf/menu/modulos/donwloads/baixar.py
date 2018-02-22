import wget


def baixarU():
    url = input("[+]set url=>")
    if url == None:
        pass
    else:
        print("[+]colocal onde o arquivo sera salvo")
        local = input("=>")
        wget.download(url=url, out=local)
        if local == None:
            local = "/tmp/"
            wget.download(url=url, out=local)
