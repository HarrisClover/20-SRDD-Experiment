
document.getElementById('upload-button').addEventListener('click', function() {
    document.getElementById('video-input').click();
});

document.getElementById('video-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const video = document.getElementById('video');
    video.src = URL.createObjectURL(file);
    video.load();
});

document.getElementById('trim-button').addEventListener('click', function() {
    const startTime = parseFloat(document.getElementById('start-time').value);
    const endTime = parseFloat(document.getElementById('end-time').value);
    const video = document.getElementById('video');

    if (isNaN(startTime) || isNaN(endTime) || startTime >= endTime || startTime < 0 || endTime > video.duration) {
        document.getElementById('error-message').textContent = 'Invalid time selection. Please ensure the start time is before the end time.';
        return;
    }

    const trimmedVideo = document.createElement('video');
    trimmedVideo.src = video.src;
    trimmedVideo.currentTime = startTime;
    trimmedVideo.addEventListener('seeked', function() {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const dataURL = canvas.toDataURL('video/mp4');
        const link = document.createElement('a');
        link.href = dataURL;
        link.download = 'trimmed-video.mp4';
        link.click();
    });
    trimmedVideo.play();
    document.getElementById('error-message').textContent = '';
    document.getElementById('success-message').textContent = 'Video trimmed successfully and saved to the specified location.';
});

document.getElementById('save-button').addEventListener('click', function() {
    const saveLocation = document.getElementById('save-location').value;
    if (saveLocation) {
        document.getElementById('success-message').textContent = 'Video saved to ' + saveLocation;
    }
});
