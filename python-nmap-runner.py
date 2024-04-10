## Author: Aditya Kamarusu
## Topic: nmap: Network Mapper

import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sV -O -p 1-20')

    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print("----------")
            print(f"Protocol : {proto}")
            print("----------")

            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                extrainfo = nm[host][proto][port]['extrainfo']
                
                print(f"Port : {port}\tState : {state}")
                print(f"Service : {name}\tProduct : {product}\tVersion : {version}\tExtra Info : {extrainfo}")

def userAsk():
    target = input("Enter the target(s) to scan: ") #(comma-separated if multiple)
    scan_network(target)

if __name__ == "__main__":
    userAsk()
