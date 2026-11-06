import json
import os
from pathlib import Path
import socket
import subprocess


def configured_servers():
    if os.name == "nt":
        command = ("$ErrorActionPreference='Stop'; "
                   "$active=@((Get-NetAdapter | Where-Object Status -eq 'Up').ifIndex); "
                   "@(Get-DnsClientServerAddress | "
                   "Where-Object { $_.InterfaceIndex -in $active } | "
                   "ForEach-Object { $_.ServerAddresses } | "
                   "Select-Object -Unique) | ConvertTo-Json -Compress")
        result = subprocess.run(["powershell.exe", "-NoProfile", "-Command", command],
                                capture_output=True, text=True, check=True, timeout=20)
        values = json.loads(result.stdout) if result.stdout.strip() else []
        return [values] if isinstance(values, str) else values
    servers = []
    for line in Path("/etc/resolv.conf").read_text().splitlines():
        fields = line.split()
        if len(fields) >= 2 and fields[0] == "nameserver":
            servers.append(fields[1])
    return list(dict.fromkeys(servers))


def main():
    try:
        servers = configured_servers()
        if not servers:
            print("No DNS resolver found on an active interface.")
        for address in servers:
            print("DNS server IP:", address)
            try:
                print("DNS server hostname:", socket.gethostbyaddr(address)[0])
            except OSError:
                print("DNS server hostname: reverse DNS unavailable")
    except (OSError, ValueError, subprocess.SubprocessError):
        print("Cannot read DNS configuration; check the operating-system resolver settings.")


if __name__ == "__main__":
    main()
