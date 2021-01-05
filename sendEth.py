# Step 1
# Authors : Mélodie O, Delphine S.
# Date    : 13/12/2020

from scapy.all import *

def main():
    
    print ("Enter src MAC address : ")
    source = input()
    
    print("Enter dst MAC address : ")
    destination = input()
    
    print("Enter message to send : ")
    message = input()
    
    if len(destination) == 0:
        destination = "FF:FF:FF:FF:FF:FF"

    sendp(Ether(src = source, dst = destination)/message)
    
main()