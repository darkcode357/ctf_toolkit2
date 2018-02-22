cyanClaro = "\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
amarelo = '\033[1;33m'
ciano = '\033[46m'
magenta = '\033[45m' 

def list():
    print("##########################################")
    print("################comandos##################")

    print("##########################################")
    print("%s[info]%s=base64-encode%s   =>   %s[comando]%s=use encode64" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base64-decode%s   =>   %s[comando]%s=use decode64" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base64-info%s     =>   %s[comando]%s=use info base64" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=base32-encode%s   =>   %s[comando]%s=use encode32" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base32-decode%s   =>   %s[comando]%s=use decode32" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base32-info%s     =>   %s[comando]%s=use info base32[=]" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=base16-encode%s   =>   %s[comando]%s=use encode16" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base16-decode%s   =>   %s[comando]%s=use decode16" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=base16-info%s     =>   %s[comando]%s=use info base16[=]" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=wordlist_gera%s   =>   %s[comando]%s=use gera_wordlist" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=wordlist_info%s   =>   %s[comando]%s=use info wordlist[=]" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=ftp-cli      %s   =>   %s[comando]%s=use ftp[=]" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=ftp-info     %s   =>   %s[comando]%s=use info ftp[=]" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=ssh+ctf_shell%s   =>   %s[comando]%s=use ssh => use ctf_shell" % (
    azul, verde, amarelo, azul, verde))

    print("%s[info]%s=reverse_shell%s   =>   %s[comando]%s=use reverse_tcp" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=reverse_shell-info%s=> %s[comando]%s=use info reverse_tcp" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=sair         %s   =>   %s[comando]%s=sair" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=wget-baixar  %s   =>   %s[comando]%s=use baixar" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=wget-info    %s   =>   %s[comando]%s=use info baixar" % (azul, verde, amarelo, azul, verde))

    print("%s[info]%s=gera_payload %s   =>   %s[comando]%s=use gera_payload" % (azul, verde, amarelo, azul, verde))
    print("%s[info]%s=%s[comando]%s=" % (azul, verde, azul, verde))
    print("%s[info]%s=%s[comando]%s=" % (azul, verde, azul, verde))


def help_base64():
    print (verde+"""
            ================doc_base64================
The particular set of 64 characters chosen to represent the 64 place-values for
the base varies between implementations. The general strategy is to choose 64 
characters that are both members of a subset common to most encodings, and also 
printable. This combination leaves the data unlikely to be modified in transit
through information systems, such as email, that were traditionally not 8-bit clean.
For example, MIME's Base64 implementation uses A–Z, a–z, and 0–9 for the first 62 
values. Other variations share this property but differ in the symbols chosen for the last
two values; an example is UTF-7.

The earliest instances of this type of encoding were created for dialup communication 
between systems running the same OS — e.g., uuencode for UNIX, BinHex for the TRS-80 
(later adapted for the Macintosh) — and could therefore make more assumptions about
what characters were safe to use. For instance, uuencode uses uppercase letters, 
digits, and many punctuation characters, but no lowercas

================Base64 table================

Base64 table

Value	Char	 	
0=>A	16=>Q	32=>g	48=>w
1=>B	17=>R	33=>h	49=>x
2=>C	18=>S	34=>i	50=>y
3=>D	19=>T	35=>j	51=>z
4=>E	20=>U	36=>k	52=>0
5=>F	21=>V	37=>l	53=>1
6=>G	22=>W	38=>m	54=>2
7=>H	23=>X	39=>n	55=>3
8=>I	24=>Y	40=>o	56=>4
9=>J	25=>Z	41=>p	57=>5
10=>K	26=>a	42=>q	58=>6
11=>L	27=>b	43=>r	59=>7
12=>M	28=>c	44=>s	60=>8
13=>N	29=>d	45=>t	61=>9
14=>O	30=>e	46=>u	62=>+
15=>P	31=>f	47=>v	63=>/

    """)    

