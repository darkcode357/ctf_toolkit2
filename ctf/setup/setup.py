import os
import os.path
from os import system as sys

from modulos.check_net import check


def install_local():
    print("")

def install_web():
    print("check[+]=[internet]")
    check()
    sys("clear")
    print("[+]iniciando a instalacao =>[web]<=")
    if os.path.exists("../arquivos") == False:
        os.makedirs("../arquivos")
    else:
        print("[pass]=[arquivos[ok]]")
    if os.path.exists("../arquivos/wordlist") ==False:
        print("add=> arquivos/wordlist[+]")
        os.makedirs("../arquivos/wordlist")
    else:
        print("[pass]=[arquivos/wordlist[ok]]")
    if os.path.exists("../arquivos/wordlist/metasploit") == False:
        print("add=>/arquivos/wordlist/metasploit[+]")
        os.makedirs("../arquivos/wordlist/metasploit")
    else:
        print("[pass]=[arquivos/wordlist/metasploit[ok]]")
    if os.path.exists("../arquivos/wordlist/sec_wordlist") == False:
        print("add=>/arquivos/wordlist/sec_wordlist[+]")
        os.makedirs("../arquivos/wordlist/sec_wordlist")
    else:
        print("[pass]=[arquivos/wordlist/sec_word_list[ok]]")


    print("inicinado verificacao de diretorios para  o donwloads dos arquivos....[+]")

    if os.path.isdir("../arquivos") == True:
        print("check 1-de-4[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()

    if os.path.isdir("../arquivos") == True:
        print("check 2-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("../arquivos/wordlist") == True:
        print("check 3-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("../arquivos/wordlist/metasploit") == True:
        print("check 4-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    if os.path.isdir("../arquivos/wordlist/sec_wordlist") == True:
        print("check 5-de-5[ok]")
    else:
        print("erro[criacao de diretorios]")
        exit()
    urlsMetas = ['https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/adobe_top100_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/av-update-urls.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/av_hips_executables.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/burnett_top_1024.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/burnett_top_500.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/cms400net_default_userpass.txt	',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/common_roots.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dangerzone_a.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dangerzone_b.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_user.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/db2_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_pass_for_services_unhash.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_userpass_for_services_unhash.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/default_users_for_services_unhash.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/dlink_telnet_backdoor_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/hci_oracle_passwords.csv',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_default_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/http_owa_common.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/idrac_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/idrac_default_user.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/ipmi_passwords.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/ipmi_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/joomla.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/keyboard-patternss.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/malicious_urls.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_user.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/mirai_user_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/multi_vendor_cctv_dvr_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/multi_vendor_cctv_dvr_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/namelist.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_hashes.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_passwords.csv',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/oracle_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/password.lst',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/piata_ssh_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_user.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/postgres_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/root_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/routers_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/rpc_names.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/rservices_from_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_common.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_default.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sap_icm_paths.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/scada_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sensitive_files.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sensitive_files_win.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/sid.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/snmp_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tftp.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_pass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/tomcat_mgr_default_userpass.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/unix_passwords.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/unix_users.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vnc_passwords.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vxworks_collide_20.txt',
                 'https://raw.githubusercontent.com/rapid7/metasploit-framework/master/data/wordlists/vxworks_common_20.txt',
                 ]




install_web()























'''


def cria_urls_txt():
    with open("urls.txt","w") as fl:
        print("[+]iniciando...")
        try:
            if os.path.exists("../arquivos") == False:
                print("[+]criando pasta => [arquivos]")
                os.makedirs("../arquivos")
            else:
                print("[+]diretorio ja existente.....[pass]")
        except D:
            print("[+]diretorio ja existente.....[pass]")
            #if os.path.file
        urls = ["http://scrapmaker.com/data/wordlists/dictionaries/rockyou.txt"] #url
        names_url = ["rockyou"] #nome referente a url
        for u in urls :
            for n in names_url:
                if u == urls:
                    pass
            else:
                print("[+]add=[%s]"%n)
                fl.write("\n"+u)
cria_urls_txt()
'''
