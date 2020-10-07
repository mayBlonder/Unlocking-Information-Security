from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment
import re

#### Don't change the code until this line ####

def show_username_password()-None:
    packets = rdpcap(recording_path)
    for packet in packets:
        p = re.findall(".*password(.*)", packet.load.decode("utf8"))
        u = re.findall(".*username(.*)", packet.load.decode("utf8"))
        if(p and u):
            print(packet)

show_username_password()
