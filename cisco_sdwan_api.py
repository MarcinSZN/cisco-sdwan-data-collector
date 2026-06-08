import requests
import sys
from getpass import getpass
from urllib3.exceptions import InsecureRequestWarning
from requests.exceptions import ConnectionError, InvalidURL, RequestException
from rich.console import Console
from rich.table import Table

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

VMANAGE_URL = "https://192.168.115.20:8443"
TIMEOUT=10


def get_vamange_token(vmanage_url, username, password):
    AUTH_URL = "/j_security_check"
    URL = vmanage_url + AUTH_URL

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'j_username': username,
        'j_password': password
    }

    try:
        output = requests.post(url=URL, headers=headers, data=payload, verify=False, timeout=TIMEOUT)

        if "Wrong username" in output.text:
            print("Invalid username/password.")
            sys.exit(1)
        
        if output.status_code != 200:
            print(f"Authentication failed with status {output.status_code}.")
            sys.exit(1)
        
        cookie = output.headers['set-cookie']
        token = cookie.split(';')[0]

        return token
    
    except (ConnectionError, InvalidURL) as e:
        print(f"Unable to connect to vManage at '{URL}'")
        sys.exit(1)

    
def get_device_certs(vmanage_url, token):
    certs_url = "/dataservice/certificate/record"
    url = vmanage_url + certs_url
    headers_certs = {
        'Content-Type': 'application/json',
        'Cookie': token
    }
    try:
        output = requests.get(url=url, headers=headers_certs, verify=False, timeout=TIMEOUT)
        return output.json()
    except RequestException as e:
        print(f"Failed to retrieve certificates: {e}")

def get_device_info(vmanage_url, token):
    devinfo_url = "/dataservice/device"
    url = vmanage_url + devinfo_url
    headers_devinfo = {
        'Content-Type': 'application/json',
        'Cookie': token
    }

    try:
        output = requests.get(url=url, headers=headers_devinfo, verify=False, timeout=TIMEOUT)
        return output.json()
    except RequestException as e:
        print(f"Failed to retrieve device inventory: {e}")


def main():
    username = input("Please provide username: ").strip()
    password = getpass("Please provide password: ")
    console = Console(record=True)

    token = get_vamange_token(VMANAGE_URL, username, password)

    # Gathering data
    certs = get_device_certs(VMANAGE_URL, token)
    devinfo = get_device_info(VMANAGE_URL, token)

    # Rendering table for SD-WAN Control Plane Certificates
    certs_table = Table(title="SDWAN Devices Certificates")
    columns = ['Device Type', 'Expiration Date']

    for column in columns:
        certs_table.add_column(column)

    for device in certs.get('data', []):
        certs_table.add_row(
            f"{device.get('deviceType', 'Unknown')}", 
            f"{device.get('expirationDate', 'N/A')}"
        )
    console.print(certs_table)


    # Rendering table for SD-WAN devices inventory
    table = Table(title="SDWAN Devices")

    columns = ['Hostname', 'Device-Model', 'UUID', 'System-IP', 'Site-ID']
    for column in columns:
        table.add_column(column)

    for device in devinfo.get('data', []):
        table.add_row(
            f"{device.get('host-name', 'N/A')}", 
            f"{device.get('device-model', 'N/A')}", 
            f"{device.get('uuid', 'N/A')}", 
            f"{device.get('system-ip', 'N/A')}", 
            f"{device.get('site-id', 'N/A')}"
        )
    console.print(table)


if __name__ == '__main__':
    main()
