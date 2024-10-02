from scapy.all import *
from scapy.layers.inet import IP,TCP
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse
from datetime import datetime
import os
import csv

iPkt=0

def process_pkt(pkt):
    global iPkt
    iPkt +=1
    with open("./connection.csv", "a+") as myfile:
        if os.stat("./connection.csv").st_size == 0:
            csv.writer(myfile).writerow(["Numero pacchetto","Lunghezza","Data/ora","IP sorgente","IP destinazione","Porta sorgente","Porta destinazione","Host"])
        if pkt[TCP].dport ==80 or pkt[TCP].dport ==443: 
            if pkt.haslayer(HTTPRequest):
                csv.writer(myfile).writerow([iPkt,pkt[IP].len,datetime.now(),pkt[IP].src,pkt[IP].dst,pkt[TCP].sport,pkt[TCP].dport,pkt[HTTPRequest].Host])
            else:
                csv.writer(myfile).writerow([iPkt,pkt[IP].len,datetime.now(),pkt[IP].src,pkt[IP].dst,pkt[TCP].sport,pkt[TCP].dport])
        elif pkt[TCP].sport==80 or pkt[TCP].sport==443:
            if pkt.haslayer(HTTPRequest):
                csv.writer(myfile).writerow([iPkt,pkt[IP].len,datetime.now(),pkt[IP].src,pkt[IP].dst,pkt[TCP].sport,pkt[TCP].dport,pkt[HTTPRequest].Host])
            else:
                csv.writer(myfile).writerow([iPkt,pkt[IP].len,datetime.now(),pkt[IP].src,pkt[IP].dst,pkt[TCP].sport,pkt[TCP].dport])

sniff(iface="eth0",filter="tcp",prn=process_pkt)

