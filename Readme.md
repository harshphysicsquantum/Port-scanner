# Port Scanner

A command-line port scanner written in Python. Uses multithreading to scan a range of TCP ports on a target host, identifies open ports, and resolves service names where possible.

## Features

- Threaded scanning for fast results
- Service name resolution for open ports
- Input validation with clear error messages
- Scan duration reporting
- Clean, minimal output

## Requirements

- Python 3.x
- No external dependencies — standard library only

## Installation

```bash
git clone https://github.com/yourusername/port-scanner
cd port-scanner
```

## Usage

```bash
python scanner.py
```

You will be prompted to enter:
- Target IP address
- Starting port number
- Ending port number

## Example

```
Port Scanner Project V-1.0
Enter the IP: 192.168.1.1
Enter the starting port number: 1
Enter the last port number: 1000
The IP to be scanned is: 192.168.1.1 and the ports to be scanned are: 1 1000

Open Ports:
  22/tcp   →  ssh
  80/tcp   →  http
  443/tcp  →  https

Scan completed in: 3.42 seconds
```

## Limitations

- TCP only — UDP scanning is not supported
- No banner grabbing — service names are resolved from the system's service registry, not from live service responses
- No subnet or multi-host support — scans a single IP per run
- No output to file

## Planned Improvements

- argparse support for command-line arguments
- Banner grabbing for open ports
- Output to file
- Subnet scanning support

## Legal Notice

This tool is intended for use on systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your jurisdiction.
