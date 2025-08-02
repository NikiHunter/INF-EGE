import ipaddress


def calculate_max_addresses(ip_str, network_str):
    # Преобразуем строки в IPv4-адреса
    ip = ipaddress.IPv4Address(ip_str)
    network_address = ipaddress.IPv4Address(network_str)

    # Находим минимальную маску, при которой IP & mask = network_address
    # Перебираем возможные длины маски (от 0 до 32)
    for prefix_len in range(33):
        mask = ipaddress.IPv4Network(f"0.0.0.0/{prefix_len}").netmask
        if (int(ip) & int(mask)) == int(network_address):
            break

    # Создаём объект сети
    print(prefix_len)  # понять
    network = ipaddress.IPv4Network(f"{network_str}/{prefix_len}", strict=False)

    # Количество адресов в сети (включая network и broadcast)
    return network.num_addresses


# Пример использования
ip = "98.162.71.94"
network = "98.162.71.64"
max_addresses = calculate_max_addresses(ip, network)
print(f"Наибольшее количество возможных адресов в сети: {max_addresses}")