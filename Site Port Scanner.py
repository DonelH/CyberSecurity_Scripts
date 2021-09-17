# This script is a port scanner for a given domain name, taking in a domain
# name and 1 or more ports by the user.

from socket import  *

# This function contains the intro text block sent at the beginning of each
# instance.
def intro():
    print("Hello! Welcome to the Site Port Scanner (SPS)\n")
    print("\tSPS will require a domain name you would like to scan and")
    print("\tthe ports you would like to scan.\n")
    print("Please enter 1 for scanning a particular set of ports or 2")
    print("for a port range.\n")

# This function handles the input from the user and running the main functions
# for the script
def main_body():
    option = input("Option (1 or 2): ")
    valid_options = ['1', '2']
    while option not in valid_options:
        print("You typed something wrong! Please type 1 or 2!")
        option = input("Option (1 or 2): ")
    if (option == '1'):
        targetPorts = input("Enter desired ports to scan with a space in between: ")
        targetPorts = list(map(int, targetPorts.split()))
    else:
        firstPort = input("Enter the first port in the range for the scan: ")
        lastPort = input("Enter the last port in the range for the scan: ")
        targetPorts = list(range(int(firstPort), int(lastPort) + 1))
    target = input("Enter the target site to port scan: ")
    portScan(target, targetPorts)
    cont = input("Would you like to try another scan?(Y or N) ")
    if (cont == "Y"):
        main_body()
    else:
        print("GOODBYE! :)")
        exit 

# The conScan function has an input of a given target host and target port
# then checking if the targeted port for the targeted host is open or closed.
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)

# The portScan function is given a target host and one or more ports to process
# by calling the conScan function for each individual port.
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s '% tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s '% tgtName[0])
    except:
        print('\n[+] Scan result of: %s '% tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: %d'% tgtPort)
        conScan(tgtHost, int(tgtPort))

# The main function which calls the other functions that will be used
# throughout the script.
if __name__ == '__main__':
    intro()
    main_body()
