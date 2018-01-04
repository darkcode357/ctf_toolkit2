def ftp():

    try:
        import ftplib
    except ImportError:
        print("install ftplib")
        from os import system as sys
        sys("pip3 install ftplib")
    try:
        from ftplib import  FTP
        host = input("host=>")
        FTP(host)
        FTP.login[])
        print("shell ftp")
        while True:
            ftp = input("ftp=>")
            if ftp == "LIST":
                FTP.dir("LIST")
    except ftplib.all_errors as e :
        print(e)
ftp()
