#!/usr/bin/env python3
import requests
import sys
import json 
import pytest
from netaddr import * 

def test_find_ip():
    #API call to JSON Data
    ip = IPAddress('192.208.0.0')
    r = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")
    #Grab ipv4 address blocks into a set
    ipv4_set = set(r.json()['data']['resources']['ipv4'])
    count = 0
    # Compare ip address with the set and add 1 to count for match
    for x in ipv4_set:
        if ip in IPNetwork(x): count+=1
    if count >= 1: 
        print(f"Pass: {ip} is found in the ipv4 CIDR ranges")
    else:
        print(f"Fail: {ip} is not found in the ipv4 CIDR ranges")
    