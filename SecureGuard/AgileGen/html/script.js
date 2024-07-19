
function toggleRealTimeProtection() {
    const status = document.getElementById('real-time-status');
    status.textContent = status.textContent === 'Running' ? 'Stopped' : 'Running';
}

function runImmediateVirusScan() {
    const status = document.getElementById('scan-status');
    const alert = document.getElementById('scan-alert');
    const action = document.getElementById('scan-action');
    
    status.textContent = 'Running';
    alert.textContent = 'Virus Detected in Downloaded File';
    action.textContent = 'File Quarantined';
}

function toggleFirewall() {
    const status = document.getElementById('firewall-status');
    status.textContent = status.textContent === 'Enabled' ? 'Disabled' : 'Enabled';
}

function openPasswordManager() {
    const status = document.getElementById('password-status');
    const save = document.getElementById('password-save');
    const autofill = document.getElementById('password-autofill');

    status.textContent = 'Enabled';
    save.textContent = 'Password Saved Securely';
    autofill.textContent = 'Password Autofilled';
}

function viewAllAlerts() {
    alert('Viewing all alerts...');
}
