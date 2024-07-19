'''
This is the updated main file for the support ticket system. It contains the Ticket, Agent, and TicketSystem classes.
Now, it includes the method to update the status of the ticket in the Ticket class.
Also, in the TicketSystem class, after assigning a ticket to an agent, the status of the ticket is updated to 'In Progress'.
The auto_escalate method has been added to handle automated ticket escalation.
'''
import datetime
MAX_OPEN_TIME = datetime.timedelta(hours=1)
MAX_IN_PROGRESS_TIME = datetime.timedelta(hours=2)
class Ticket:
    def __init__(self, ticket_id, customer_name, issue_description):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.assigned_agent = None
        self.priority_level = None
        self.status = 'Open'
        self.comments = []
        self.time_open = datetime.datetime.now()
        self.time_in_progress = None
    def assign_agent(self, agent):
        self.assigned_agent = agent
        self.time_in_progress = datetime.datetime.now()
    def set_priority_level(self, level):
        self.priority_level = level
    def add_comment(self, comment):
        self.comments.append(comment)
    def update_status(self, status):
        self.status = status
    def auto_escalate(self):
        if self.status == 'Open' and datetime.datetime.now() - self.time_open > MAX_OPEN_TIME:
            self.priority_level = 'High'
        elif self.status == 'In Progress' and datetime.datetime.now() - self.time_in_progress > MAX_IN_PROGRESS_TIME:
            self.priority_level = 'High'
class Agent:
    def __init__(self, agent_id, agent_name):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.assigned_tickets = []
    def assign_ticket(self, ticket):
        self.assigned_tickets.append(ticket)
        ticket.assign_agent(self)
class TicketSystem:
    def __init__(self):
        self.tickets = []
        self.agents = []
    def create_ticket(self, customer_name, issue_description):
        ticket_id = len(self.tickets) + 1
        ticket = Ticket(ticket_id, customer_name, issue_description)
        self.tickets.append(ticket)
        return ticket
    def add_agent(self, agent_name):
        agent_id = len(self.agents) + 1
        agent = Agent(agent_id, agent_name)
        self.agents.append(agent)
        return agent
    def assign_ticket_to_agent(self, ticket, agent):
        agent.assign_ticket(ticket)
        ticket.set_priority_level('Medium')
        ticket.update_status('In Progress')
    def track_ticket_status(self, ticket):
        return ticket.status
    def communicate_with_customer(self, ticket, comment):
        ticket.add_comment(comment)
    def escalate_tickets(self):
        for ticket in self.tickets:
            ticket.auto_escalate()