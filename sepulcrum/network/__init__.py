import socket


def sort_ips(ip_list):
    return sorted(ip_list, key=socket.inet_aton)
