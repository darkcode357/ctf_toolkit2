# -*- coding: utf-8 -*-
def ftp():
    from ftplib import FTP, error_perm
    from socket import gaierror
    import os

    def listar(ftp, caminho):
        """Lista os arquivos do diretório passado como parâmetro"""
        ftp.retrlines('LIST ' + caminho)

    def caminhar(ftp, caminho):
        ftp.cwd(caminho)

    def baixar(ftp, filename):
        print("Baixando arquivo...")
        file = open(filename, 'wb')
        ftp.retrbinary('RETR %s' % filename, file.write)
        file.close()
        print("Arquivo baixado com sucesso.")
        
    while True:
        while True:
            rhost = str(input('IP: ').strip(' '))
            try:
                porta = int(input('Porta: ').strip(' '))
            except ValueError:
                print('Verifique a porta e tente novamente.')
                continue
            else:
                break
                
        usuario = input('Usuário: ').strip(' ')
        senha = input('Senha: ').strip(' ')

        with FTP() as ftp:
            try:
                ftp.connect(rhost, porta)
            except (gaierror,ConnectionRefusedError):
                print("Servidor não encontrado.")
                break

            ftp.encoding = 'utf-8'
            try:        
                ftp.login(usuario, senha)
            except:
                print("Usuário ou senha incorretos.")
                break
            
            ##Comandos##
            print("Use 'help' para listar os comandos.")
            while True:
                current_dir = ftp.pwd()
                comando = input((usuario+'@'+rhost+'['+current_dir+']'+": ")).strip(' ').split(' ')

                if comando[0] == 'ls':
                    try:            
                        if len(comando) > 1:
                            caminho = ' '.join(map(str, comando[1:])) #Converte os diretórios com espacos que viraram 
                                                                      #elementos separados e junta-os novamente.
                            listar(ftp, caminho)
                        else:
                            listar(ftp, caminho='')
                    except error_perm:
                        print("Diretório não encontrado.")

                elif comando[0] == 'cd':
                    try:            
                        if len(comando) > 1:
                            caminho = ' '.join(map(str, comando[1:])) #Converte os diretórios com espacos que viraram 
                                                                      #elementos separados e junta-os novamente.
                            caminhar(ftp, caminho)
                        else:
                            caminhar(ftp, caminho='/')
                    except error_perm:
                        print("Diretório não encontrado.")
                
                elif comando[0] == 'baixar':
                    try:            
                        if len(comando) > 1:
                            caminho = ' '.join(map(str, comando[1:])) #Converte os diretórios com espacos que viraram 
                                                                      #elementos separados e junta-os novamente.
                            baixar(ftp, caminho)
                        else:
                            print('Indique o arquivo a ser baixado.')
                    except error_perm:
                        print("Arquivo não encontrado.")
                        os.remove(caminho)
                        
                elif comando[0] == 'sair':
                    return 0
                elif comando[0] == 'help':
                    #ls#
                    print('''\tls - lista os arquivos do diretório atual.\n\tExemplos: \n\t\tls\n\t\tls Área de Trabalho\n\t\tls Documentos''')
                    print()
                    #cd#
                    print('''\tcd - navega entre os diretórios.''')
                    #sair#
                    print('''\tsair - encerra o FTP.''')
