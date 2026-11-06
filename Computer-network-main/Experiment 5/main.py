addresses = {"192.0.2.10": "02:00:00:00:00:01", "192.0.2.11": "02:00:00:00:00:02"}

ip = input("ARP - enter IP address: ").strip()
print("MAC address:", addresses.get(ip, "Address not found"))

mac = input("RARP - enter MAC address: ").strip().lower()
reverse = {value: key for key, value in addresses.items()}
print("IP address:", reverse.get(mac, "Address not found"))
