import os
target_ipaddress = input("Enter your target ip address: ")
os.system('nmap {0}'.format(target_ipaddress))