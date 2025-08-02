# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('211.48.136.64/255.255.255.224', False):
    bin_address = f'{address:b}'  # Python 3.9+
    #  bin_address = f'{int(address):b}' в ранних версиях
    count += bin_address[-2:] == '11'
print(count)
