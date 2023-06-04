import nmap

def scan_network():
    nm = nmap.PortScanner()
    target = input("Enter the target IP address or range to scan: ")
    print("Scanning:", target)
    results = nm.scan(hosts=target, arguments='-p 1-1000')
    
    for host in nm.all_hosts():
        print('-----------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
    
        for proto in nm[host].all_protocols():
            print('-----------------------------------------')
            print('Protocol : %s' % proto)
    
            lport = nm[host][proto].keys()
            for port in lport:
                print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))

scan_network()
