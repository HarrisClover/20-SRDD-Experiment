'''
Firewall - Network Firewall
This file contains the Firewall class, which is responsible for monitoring and blocking unauthorized access attempts.
Author: Programmer
'''
class Firewall:
    def __init__(self):
        self.blocked_ips = []
    def block(self, ip_address):
        # Perform the blocking logic here
        self.blocked_ips.append(ip_address)
    def is_blocked(self, ip_address):
        # Check if the given IP address is blocked
        return ip_address in self.blocked_ips