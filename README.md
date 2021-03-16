# IP-Check

IP check is a simple python 3 script that gets json data and checks if a given IP is in the Ipv4 CIDR Ranges

## Installation
Clone the repo and then install the dependencies
```bash
pip install -r requirements.txt
```
## Usage

```bash
./ip_check <ip address>
```

### Output
```bash
$ python ip_check.py 192.168.004.001
Fail: 192.168.4.1 is not found in the ipv4 CIDR ranges
```
```bash
$ python ip_check.py 69.208.0.1
Pass: 69.208.0.1 is found in the ipv4 CIDR range
```