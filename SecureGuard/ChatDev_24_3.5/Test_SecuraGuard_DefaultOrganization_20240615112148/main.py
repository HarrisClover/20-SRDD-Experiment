'''
SecureGuard - Security Software Application
This is the main file of the SecureGuard application. It provides real-time monitoring and protection for personal computers, constantly scanning for malware, viruses, and unauthorized access attempts. It alerts the user and takes measures to neutralize threats. It includes a firewall and password manager to ensure data privacy and security.
Author: Programmer
'''
from gui import SecureGuardGUI
from scanner import Scanner
from firewall import Firewall
from password_manager import PasswordManager
def main():
    # Initialize the scanner, firewall, and password manager
    scanner = Scanner()
    firewall = Firewall()
    password_manager = PasswordManager()
    # Create the GUI and pass the scanner, firewall, and password manager objects
    gui = SecureGuardGUI(scanner, firewall, password_manager)
    gui.run()
if __name__ == "__main__":
    main()