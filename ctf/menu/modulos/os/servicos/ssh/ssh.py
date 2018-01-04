cyanClaro = "\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
amarelo = '\033[1;33m'
ciano = '\033[46m'
magenta = '\033[45m'
normal = '\033[0;0m'
#comandos ctf_shell
ctf_comandos = {"find_suid":"find / -user root -perm -4000 2>/dev/null",
                "list_users":"awk -F: '{ print $1 }' /etc/passwd",
                "info_os":"cat /etc/*release",
                "kernel":"uname -r",
                }


def ssh():
    from os import system as sys
    from pexpect import pxssh
    import getpass
    try:
        s = pxssh.pxssh()
        hostname = input('hostname: ')
        username = input('username: ')
        password = getpass.getpass('password: ')
        s.login(hostname, username, password)
        while True:
            try:
                print("use a ctf_shell para ajudar vc no sua exploracao")
                print("use ctf_shell")
                dsa = input(amarelo+"darkcode=>"+vermelho)  # print everything before the prompt.
                s.sendline(dsa)
                s.prompt()
                print(verde+s.before.decode("utf-8"))
                if dsa == "sair":
                    s.logout()
                    break
                if dsa =="use ctf_shell":
                    while True:
                        ctf_shell = input(amarelo+"ctf#=>"+azul)
                        if ctf_shell =="sair":
                            break

                        elif ctf_shell == "ctf_comandos":
                            for key,value in ctf_comandos.items():
                                print(vermelho+"ctf_comandos => "+key)
                                print(azul+"linux_comandos=>"+value)

                        elif ctf_shell =="list_users":
                            s.sendline(ctf_comandos["list_users"])
                            s.prompt()
                            print(verde + s.before.decode("utf-8"))

                        elif ctf_shell =="info_os":
                            s.sendline(ctf_comandos["info_os"])
                            s.prompt()
                            print(verde + s.before.decode("utf-8"))

                        elif ctf_shell =="kernel":
                            from menu.modulos.os.servicos.ssh.kernel import kernel
                            s.sendline(kernel)
                            s.prompt()
                            print(verde + s.before)

                        elif ctf_shell =="find_suid":
                            s.sendline(ctf_comandos["find_suid"])
                            s.prompt()
                            print(verde + s.before.decode("utf-8"))




            except KeyboardInterrupt:
                print("digite=> sair")

    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)
