import nmap
def scan(ip="127.0.0.1",r1=1,r2=1000):
    #ip = "202.162.214.254"
    #r1 = 1
    #r2 = 9900
    nm = nmap.PortScanner()
    nm.scan(ip, '%s-%s'%(r1,r2))
    print("#"*30)
    print("metodo => "+nm.scaninfo()['tcp']['method'])                       # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
    print("portas => "+nm.scaninfo()['tcp']['services'])                       # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
    print("status => "+nm[ip].state())

    for port in nm[ip]['tcp']:
        thisDict = nm[ip]['tcp'][port]
        print ('Port ' + str(port) + ': ' + thisDict['product'] + ', v' + thisDict['version'])
        print("\tprotocolo => "+nm[ip]['tcp'][port]['product'])
        print("\tstatus => "+nm[ip]['tcp'][port]['state'])
        print("\tversao => "+nm[ip]['tcp'][port]['version'])
        print("\tnome => "+nm[ip]['tcp'][port]['name'])
        print("\tconf => "+nm[ip]['tcp'][port]['conf'])
        print("\textrainfo => "+nm[ip]['tcp'][port]['extrainfo'])
        print("\treason =>"+nm[ip]['tcp'][port]['reason'])
        print("\tcpe => "+nm[ip]['tcp'][port]['cpe'])
        #print(nm[ip]['tcp'][port])          # get infos about port 22 in tcp on host 127.0.0.1
        #print(nm[ip].tcp(port))             # get infos about port 22 in tcp on host 127.0.0.1
    #{'product': 'Apache httpd', 'state': 'open', 'version': '2.4.29', 'name': 'http', 'conf': '10', 'extrainfo': '(Debian)', 'reason': 'syn-ack', 'cpe': 'cpe:/a:apache:http_server:2.4.29'}
scan()
