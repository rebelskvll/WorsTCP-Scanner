#!/usr/bin/python3

import socket
import threading
import argparse

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            if s.connect_ex((ip, port)) == 0:
                print(f'[+] Port {port} is open')
    except Exception as e:
        print(f'[-] Error scanning port {port}: {e}')

def main():

    parser = argparse.ArgumentParser(description='Threaded TCP Port Scanner')
    parser.add_argument('target', help='Target IP address or hostname')
    parser.add_argument('-s', '--start', type=int, help='Start port')
    parser.add_argument('-e', '--end', type=int, help='End port')
    args = parser.parse_args()
    
    target_ip = args.target
    start_port = args.start
    end_port = args.end

    threads = []

    print(f'[!] Scanning ports on {target_ip}')

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print('[*] Scan complete')

if __name__ == '__main__':
    main()