from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ip_address()->None:
    packets = rdpcap(recording_path)
    print(packets[3][IP].src)
    print(packets[5][IP].dst)

show_source_destination_ip_address()
