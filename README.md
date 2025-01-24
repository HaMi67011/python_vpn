# python_vpn

Here's a simple `README.md` file for your script:

```markdown
# IP and MAC Address Changer Script

This Python script allows you to change the IP and MAC addresses of a network interface continuously, generating random IP and MAC addresses. The script will keep running until the user manually interrupts it by pressing `Ctrl+C`.

## Features:
- **Random IP Generation:** The script generates random IP addresses in the `192.168.x.x` range.
- **Random MAC Generation:** It generates random MAC addresses while ensuring they are unicast (even-numbered first byte).
- **Network Interface Support:** Supports any valid network interface like `eth0`, `wlan0`, etc.
- **Continuous Operation:** The script will continuously change the IP and MAC addresses until forcibly stopped by the user.

## Requirements:
- Python 3.x
- Linux-based OS (Ubuntu, Debian, etc.)
- `sudo` privileges for changing network configurations
- `ip` command available on the system (most modern Linux distributions)

## Installation:
1. Clone the repository or download the script.
2. Ensure that Python 3 and the necessary packages are installed.

```bash
sudo apt update
sudo apt install python3
```

3. Run the script with root (or sudo) privileges to allow network interface changes.

```bash
sudo python3 change_ip_mac.py
```

## Usage:
1. When you run the script, it will prompt you to enter the network interface (e.g., `eth0`, `wlan0`).
2. The script will then start generating random IP and MAC addresses and apply them to the selected interface.
3. The script will continue running and changing the IP and MAC addresses indefinitely, with a small delay between changes.
4. To stop the script, press `Ctrl+C` to interrupt and exit the process.

## Example:
```
Enter the network interface (e.g., eth0, wlan0): eth0
Generated Random IP Address: 192.168.45.67
Generated Random MAC Address: 12:34:56:78:9a:bc
Changing IP address to 192.168.45.67...
Changing MAC address to 12:34:56:78:9a:bc...
```

## Troubleshooting:
- **Interface Not Found:** If the script cannot find the network interface, ensure you have entered the correct interface name and that the interface is active. Use `ip link show` to list available interfaces.
- **Permission Denied:** Ensure you are running the script with `sudo` to allow changes to network configurations.

## Disclaimer:
Be cautious when running scripts that modify network settings, as changing the IP or MAC address may disrupt network connectivity temporarily. Use it in controlled environments or with administrative approval.
```

### Instructions for use:
1. **Cloning the repo (if applicable):** Replace the appropriate line with your actual repository URL if this is part of a repository.
2. **Adjusting installation steps:** If additional installation steps are required (for example, installing dependencies), you can modify the installation section accordingly.

This README provides instructions for users to understand the purpose of the script, how to use it, and how to troubleshoot common issues.
