from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address()->None:
    packets = rdpcap(recording_path)
    print(packets[2].src)

show_mac_address()
