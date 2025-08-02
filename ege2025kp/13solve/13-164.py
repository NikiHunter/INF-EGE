# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('202.75.38.152/255.255.255.248', False):
    bin_address = f'{address:b}'  # Python 3.9+
    #  bin_address = f'{int(address):b}' в ранних версиях
    count += '111' in bin_address
print(count)
