while True:
    try:
        try:
            menu = input(azul + u'\u27a4' + vermelho)

            if menu == "help use":
                print("%s[+]%s use comandos" % (amarelo, azul))
            elif menu == "list":
                list()
            elif menu == "clean":
                import os;

                os.system("clear")
                list()
                del os
            elif menu == "use decode64":
                decode64()
            elif menu == "use encode64":
                encode64()
            elif menu == "use decode32":
                decode32()
            elif menu == "use encode32":
                encode32()
            elif menu == "use decode16":
                decode16()
            elif menu == "use encode16":
                encode16()
            elif menu == "use ssh":
                ssh()
            elif menu == "use ftp":
                ftp()
            elif menu == "use gera_wordlist":
                gera_wrdlist()
            elif menu == "comandos":
                list()
            elif menu == "info base64":
                help_base64()
            elif menu == "use reverse_tcp":
                main()
            elif menu == "use baixar":
                baixarU()
            elif menu == "use gera_payload":
                payloads()
            elif menu == "sair":
                print("%s[+]%sobrigado por usar o ctf_toolkit" % (amarelo, azul))
                print("%s[+]%scriador darkcode" % (amarelo, azul))
                exit(1)
        except EOFError:
            print(amarelo + "digite help")
    except KeyboardInterrupt as e:
        print(amarelo + "digite help")
