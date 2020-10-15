from struct import *

packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'
LEN = len(packet) - (4 * 6)
#### Don't change the code until this line ####

def show_details()->None:
	sender_ID, receiver_ID, cont_size, session_ID, msg_ID, msg, checksum = unpack(f'iiiii{LEN}si', packet)
	print(sender_ID)
	print(msg_ID)
	print(msg.decode('utf8'))
	print(checksum)

show_details()
