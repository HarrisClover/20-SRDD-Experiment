
document.getElementById('upload-button').addEventListener('click', function() {
    const fileInput = document.getElementById('video-file');
    const statusIndicator = document.getElementById('status-indicator');
    
    if (fileInput.files.length === 0) {
        statusIndicator.textContent = 'No file chosen';
        statusIndicator.style.color = 'red';
        return;
    }

    const file = fileInput.files[0];
    statusIndicator.textContent = 'Processing...';
    statusIndicator.style.color = 'orange';

    setTimeout(() => {
        const videoName = file.name;
        const format = file.type.split('/')[1].toUpperCase();
        const sceneChanges = Math.floor(Math.random() * 10) + 1;
        const timestamps = Array.from({ length: sceneChanges }, () => Math.floor(Math.random() * 600));

        statusIndicator.textContent = 'Completed';
        statusIndicator.style.color = 'green';

        const processedVideosTable = document.getElementById('processed-videos-table');
        const newRow = processedVideosTable.insertRow();
        newRow.insertCell(0).textContent = videoName;
        newRow.insertCell(1).textContent = format;
        newRow.insertCell(2).textContent = 'Completed';
        newRow.insertCell(3).textContent = sceneChanges;
        newRow.insertCell(4).textContent = timestamps.join(', ');

        document.getElementById('result-video-name').textContent = videoName;
        document.getElementById('result-video-format').textContent = format;
        document.getElementById('result-total-scenes').textContent = sceneChanges;
        
        const timestampsList = document.getElementById('result-timestamps-list');
        timestampsList.innerHTML = '';
        timestamps.forEach(timestamp => {
            const listItem = document.createElement('li');
            listItem.textContent = timestamp;
            timestampsList.appendChild(listItem);
        });
    }, 3000);
});
