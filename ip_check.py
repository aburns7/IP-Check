#!/usr/bin/env python3
import requests
import sys
import json 
import time
from netaddr import *

def find_ip(ip):
    #API call to JSON Data
    try:
        r = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")
    except Exception as e: print(f"Exception Raised API Request: {e}")
    count = 0
    #Grab ipv4 address blocks into a set
    ipv4_set = set(r.json()['data']['resources']['ipv4'])

    # Compare ip address with the set and add 1 to count for match
    for x in ipv4_set:
        if ip in IPNetwork(x): count+=1
    if count >= 1: 
        return (f"Pass: {ip} is found in the ipv4 CIDR ranges")
    else:
        return (f"Fail: {ip} is not found in the ipv4 CIDR ranges")
        


if __name__ == '__main__':
    #Validate IP address
    try:
        # Take in given IP Address from command line argument
        # Edge case: stop program if more than one ip is given
        ip = IPAddress(sys.argv[1])
        if len(sys.argv) > 2:
            raise SystemExit(f"Usage: {sys.argv[0]} <IPv4 Address>")

        # Edge case: check if IP is a valid IPv4 address
        # Now call function to determine if the IP is located in the CIDR ranges
        if ip.version == 4:
            print(find_ip(ip))
        else: raise SystemExit(f"Usage: {sys.argv[0]} <IPv4 Address>")

    except AddrFormatError as e: print(str(e) + '. Please input the IP address correctly')
    except IndexError: raise SystemExit(f"Usage: {sys.argv[0]} <IPv4 Address>")