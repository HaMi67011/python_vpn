import subprocess
import time
import random
import re

def generate_random_ip():
    # Generate a random private IP in the range 192.168.x.x
    ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip

def generate_random_mac():
    # Generate a random MAC address
    mac = [random.randint(0, 255) for _ in range(6)]
    mac[0] &= 0xFE  # Ensures it's a unicast address (even-numbered first byte)
    return ':'.join(['{:02x}'.format(x) for x in mac])

def change_ip(new_ip, interface):
    print(f"Changing IP address to {new_ip}...")
    result = subprocess.run(f"sudo ip addr add {new_ip}/24 dev {interface}", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error changing IP address: {result.stderr}")
    else:
        print(f"IP address changed to {new_ip}")

def change_mac(interface, time_to_wait):
    print(f"Waiting for {time_to_wait} seconds before changing MAC address...")
    time.sleep(time_to_wait)
    new_mac = generate_random_mac()
    print(f"Changing MAC address to {new_mac}...")
    
    result = subprocess.run(f"sudo ip link set {interface} down", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error bringing down interface: {result.stderr}")
        return

    result = subprocess.run(f"sudo ip link set {interface} address {new_mac}", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error changing MAC address: {result.stderr}")
        return

    result = subprocess.run(f"sudo ip link set {interface} up", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error bringing up interface: {result.stderr}")
        return

    print(f"MAC address changed to {new_mac}!")

def is_valid_interface(interface):
    result = subprocess.run(f"ip link show {interface}", shell=True, capture_output=True, text=True)
    return result.returncode == 0

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")

    # Validate interface
    if not is_valid_interface(interface):
        print(f"Error: Interface {interface} does not exist.")
    else:
        try:
            while True:
                # Generate random IP and MAC
                random_ip = generate_random_ip()
                random_mac = generate_random_mac()

                print(f"Generated Random IP Address: {random_ip}")
                print(f"Generated Random MAC Address: {random_mac}")
                
                # Change IP address immediately
                change_ip(random_ip, interface)

                # Wait and change MAC address
                change_mac(interface, time_to_wait=0.1)

                # Optionally, you can add a delay to prevent rapid changes
                time.sleep(2)  # Adjust this sleep time as needed

        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Stopping...")
