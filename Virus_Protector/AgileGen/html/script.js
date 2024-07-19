
document.addEventListener('DOMContentLoaded', () => {
    // Dummy data for demonstration
    const activityLog = [
        'Malicious file detected and quarantined.',
        'System scan completed. No threats found.',
        'Real-time protection activated.'
    ];

    const notifications = [
        'New virus definitions available.',
        'Scheduled scan completed. No threats found.',
        'Real-time protection detected a potential threat.'
    ];

    // Populate activity log
    const activityLogList = document.getElementById('activity-log-list');
    activityLogList.innerHTML = activityLog.map(activity => `<li>${activity}</li>`).join('');

    // Populate notifications
    const notificationPanelList = document.getElementById('notification-panel-list');
    notificationPanelList.innerHTML = notifications.map(notification => `<li>${notification}</li>`).join('');

    // Event listeners for buttons
    document.getElementById('quick-scan').addEventListener('click', () => {
        alert('Quick Scan initiated.');
        document.getElementById('scan-status').innerText = 'Scanning...';
        setTimeout(() => {
            document.getElementById('scan-status').innerText = 'Completed';
            document.getElementById('detected-threats').innerText = '2';
        }, 2000);
    });

    document.getElementById('full-scan').addEventListener('click', () => {
        alert('Full Scan initiated.');
        document.getElementById('scan-status').innerText = 'Scanning...';
        setTimeout(() => {
            document.getElementById('scan-status').innerText = 'Completed';
            document.getElementById('detected-threats').innerText = '0';
        }, 5000);
    });

    document.getElementById('custom-scan').addEventListener('click', () => {
        alert('Custom Scan initiated.');
        document.getElementById('scan-status').innerText = 'Scanning...';
        setTimeout(() => {
            document.getElementById('scan-status').innerText = 'Completed';
            document.getElementById('detected-threats').innerText = '1';
        }, 3000);
    });

    document.getElementById('quarantine').addEventListener('click', () => {
        alert('Files quarantined.');
    });

    document.getElementById('delete').addEventListener('click', () => {
        alert('Files deleted.');
    });

    document.getElementById('ignore').addEventListener('click', () => {
        alert('Threats ignored.');
    });
});
