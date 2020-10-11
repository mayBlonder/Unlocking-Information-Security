from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_domain_ip_address():
    packets = rdpcap(recording_path)
    for pkt in packets:
        if (DNS in pkt):
            for x in range(pkt[DNS].ancount):
                print(pkt[DNSRR][x].rdata)

show_domain_ip_address()
