
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('shared-canvas');
    const ctx = canvas.getContext('2d');
    const userList = document.getElementById('user-list');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const notificationArea = document.getElementById('notification-area');
    const saveModal = document.getElementById('save-modal');
    const closeSaveModal = document.getElementById('close-save-modal');
    const permissionsModal = document.getElementById('permissions-modal');
    const closePermissionsModal = document.getElementById('close-permissions-modal');

    // Setup canvas dimensions
    canvas.width = window.innerWidth * 0.7;
    canvas.height = window.innerHeight * 0.8;

    // Tool state
    let currentTool = 'brush';
    let currentColor = '#000000';
    let drawing = false;

    // Event listeners for tools
    document.getElementById('brush-tool').addEventListener('click', () => currentTool = 'brush');
    document.getElementById('eraser-tool').addEventListener('click', () => currentTool = 'eraser');
    document.getElementById('color-picker').addEventListener('change', (e) => currentColor = e.target.value);

    // Drawing logic
    canvas.addEventListener('mousedown', (e) => {
        drawing = true;
        ctx.beginPath();
        ctx.moveTo(e.offsetX, e.offsetY);
    });

    canvas.addEventListener('mousemove', (e) => {
        if (drawing) {
            ctx.lineTo(e.offsetX, e.offsetY);
            ctx.strokeStyle = currentTool === 'brush' ? currentColor : '#ffffff';
            ctx.lineWidth = currentTool === 'brush' ? 2 : 10;
            ctx.stroke();
        }
    });

    canvas.addEventListener('mouseup', () => {
        drawing = false;
        ctx.closePath();
    });

    // Chat functionality
    document.getElementById('send-chat').addEventListener('click', () => {
        const message = chatInput.value;
        if (message) {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            chatMessages.appendChild(messageElement);
            chatInput.value = '';
        }
    });

    // Save functionality
    document.getElementById('save-btn').addEventListener('click', () => {
        notificationArea.textContent = 'Sketch Saved!';
        saveModal.style.display = 'flex';
    });

    closeSaveModal.addEventListener('click', () => {
        saveModal.style.display = 'none';
    });

    // Undo/Redo functionality (basic implementation)
    let history = [];
    let historyIndex = -1;

    function saveState() {
        history = history.slice(0, historyIndex + 1);
        history.push(canvas.toDataURL());
        historyIndex++;
    }

    canvas.addEventListener('mouseup', saveState);

    document.getElementById('undo-btn').addEventListener('click', () => {
        if (historyIndex > 0) {
            historyIndex--;
            const img = new Image();
            img.src = history[historyIndex];
            img.onload = () => ctx.drawImage(img, 0, 0);
        }
    });

    document.getElementById('redo-btn').addEventListener('click', () => {
        if (historyIndex < history.length - 1) {
            historyIndex++;
            const img = new Image();
            img.src = history[historyIndex];
            img.onload = () => ctx.drawImage(img, 0, 0);
        }
    });

    // Permissions functionality
    document.getElementById('permissions-modal').style.display = 'none'; // Initially hide the modal
    document.getElementById('close-permissions-modal').addEventListener('click', () => {
        permissionsModal.style.display = 'none';
    });

    // Example of adding users to user list
    const users = ['User1', 'User2', 'User3'];
    users.forEach(user => {
        const userElement = document.createElement('li');
        userElement.textContent = user;
        userList.appendChild(userElement);
    });

    // Example of setting permissions
    const permissionsList = document.getElementById('permissions-list');
    users.forEach(user => {
        const permissionElement = document.createElement('div');
        permissionElement.textContent = `${user}: Can Draw`;
        permissionsList.appendChild(permissionElement);
    });
});
