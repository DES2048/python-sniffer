import struct
import socket
import textwrap


def get_mac_addr(mac_data):
    bytes_str = map('{:02x}'.format, macdata)
    return ':'.join(bytes_str).upper()


def ethernet_frame(data):
    dst_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[0:14])

    return get_mac_addr(dst_mac), get_mac_addr(src_mac), data[14:]
