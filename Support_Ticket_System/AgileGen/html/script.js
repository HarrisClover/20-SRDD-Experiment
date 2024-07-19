
document.addEventListener('DOMContentLoaded', function () {
    const createTicketLink = document.getElementById('create-ticket');
    const viewOpenTicketsLink = document.getElementById('view-open-tickets');
    const viewEscalatedTicketsLink = document.getElementById('view-escalated-tickets');
    const generateReportLink = document.getElementById('generate-report');
    const createTicketForm = document.getElementById('create-ticket-form');
    const ticketListSection = document.getElementById('ticket-list');
    const cancelBtn = document.getElementById('cancel');
    const ticketForm = document.getElementById('ticket-form');
    const ticketTableBody = ticketListSection.querySelector('tbody');

    let tickets = [];
    let ticketIdCounter = 1;

    createTicketLink.addEventListener('click', function () {
        createTicketForm.classList.remove('hidden');
        ticketListSection.classList.add('hidden');
    });

    viewOpenTicketsLink.addEventListener('click', function () {
        createTicketForm.classList.add('hidden');
        ticketListSection.classList.remove('hidden');
        displayTickets('Open');
    });

    viewEscalatedTicketsLink.addEventListener('click', function () {
        createTicketForm.classList.add('hidden');
        ticketListSection.classList.remove('hidden');
        displayTickets('Escalated');
    });

    cancelBtn.addEventListener('click', function () {
        createTicketForm.classList.add('hidden');
    });

    ticketForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const ticket = {
            id: ticketIdCounter++,
            customerName: ticketForm['customer-name'].value,
            customerEmail: ticketForm['customer-email'].value,
            issueDescription: ticketForm['issue-description'].value,
            priorityLevel: ticketForm['priority-level'].value,
            assignedAgent: ticketForm['assign-to'].value,
            status: 'Open',
        };
        tickets.push(ticket);
        ticketForm.reset();
        createTicketForm.classList.add('hidden');
        alert('Ticket created successfully');
    });

    function displayTickets(status) {
        ticketTableBody.innerHTML = '';
        tickets.filter(ticket => ticket.status === status).forEach(ticket => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${ticket.id}</td>
                <td>${ticket.customerName}</td>
                <td>${ticket.issueDescription}</td>
                <td>${ticket.priorityLevel}</td>
                <td>${ticket.assignedAgent}</td>
                <td>${ticket.status}</td>
                <td>
                    <button onclick="viewTicket(${ticket.id})">View</button>
                    <button onclick="editTicket(${ticket.id})">Edit</button>
                    <button onclick="reassignTicket(${ticket.id})">Reassign</button>
                    <button onclick="updateStatus(${ticket.id})">Update Status</button>
                </td>
            `;
            ticketTableBody.appendChild(row);
        });
    }

    window.viewTicket = function (id) {
        const ticket = tickets.find(ticket => ticket.id === id);
        alert(`Ticket Details:\nID: ${ticket.id}\nCustomer: ${ticket.customerName}\nIssue: ${ticket.issueDescription}\nPriority: ${ticket.priorityLevel}\nAgent: ${ticket.assignedAgent}\nStatus: ${ticket.status}`);
    };

    window.editTicket = function (id) {
        const ticket = tickets.find(ticket => ticket.id === id);
        ticketForm['customer-name'].value = ticket.customerName;
        ticketForm['customer-email'].value = ticket.customerEmail;
        ticketForm['issue-description'].value = ticket.issueDescription;
        ticketForm['priority-level'].value = ticket.priorityLevel;
        ticketForm['assign-to'].value = ticket.assignedAgent;
        createTicketForm.classList.remove('hidden');
    };

    window.reassignTicket = function (id) {
        const newAgent = prompt('Enter new agent name:');
        const ticket = tickets.find(ticket => ticket.id === id);
        ticket.assignedAgent = newAgent;
        alert('Ticket reassigned successfully');
    };

    window.updateStatus = function (id) {
        const newStatus = prompt('Enter new status (Open, In Progress, Resolved, Escalated):');
        const ticket = tickets.find(ticket => ticket.id === id);
        ticket.status = newStatus;
        alert('Ticket status updated successfully');
    };
});
