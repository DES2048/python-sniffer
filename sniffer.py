import struct
import socket
import textwrap


def get_mac_addr(mac_data):
    bytes_str = map('{:02x}'.format, macdata)
    return ':'.join(bytes_str).upper()


def ethernet_frame(data):
    dst_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[0:14])

    return get_mac_addr(dst_mac), get_mac_addr(src_mac), proto, data[14:]


def main():
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))

    while True:
        raw_data, addr = sock.recvfrom(65536)
        dst_mac, src_mac, proto, data = ethernet_frame(raw_data)
        print('src:{}, dst:{}, proto:{}'.format(dst_mac, src_mac, proto))


if __name__ == '__main__':
    main()


