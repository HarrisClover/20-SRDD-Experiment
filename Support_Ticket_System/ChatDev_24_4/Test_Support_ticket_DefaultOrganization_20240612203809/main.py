'''
This is the main execution file for the support ticket system. 
It creates an instance of the TicketSystem class and periodically calls the escalate_tickets method.
'''
import time
from ticket_system import TicketSystem
ticket_system = TicketSystem()
while True:
    ticket_system.escalate_tickets()
    time.sleep(60)  # wait for 60 seconds