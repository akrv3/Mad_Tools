import requests
import json
import pyfiglet

print(pyfiglet.figlet_format("MAD TOOLS"))

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_ip_info(ip_address):
    ip_info = get_ip_info(ip_address)
    if ip_info:
        print(f"IP Address: {ip_address}")
        print(f"Country: {ip_info['country']}")
        print(f"City: {ip_info['city']}")
        print(f"Latitude: {ip_info['loc'].split(',')[0]}")
        print(f"Longitude: {ip_info['loc'].split(',')[1]}")
        print(f"ISP: {ip_info['org']}")
        print(f"Hostname: {ip_info['hostname']}")
        print(f"Organization: {ip_info['org']}")
        if 'company' in ip_info:
            print(f"Company: {ip_info['company']['name']}")
            if 'address' in ip_info['company']:
                print(f"Address: {ip_info['company']['address']}")
            if 'phone' in ip_info['company']:
                print(f"Phone: {ip_info['company']['phone']}")
            if 'email' in ip_info['company']:
                print(f"Email: {ip_info['company']['email']}")
    else:
        print("IP INVALIDE")

def main():
    while True:
        ip_address = input("Entre une adress IP( ou Q pour quitter ) ")
        if ip_address.lower() == 'q':
            break
        print_ip_info(ip_address)
        print()

if __name__ == "__main__":
    main()