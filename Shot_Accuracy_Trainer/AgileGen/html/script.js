
document.getElementById('confirm-sport').addEventListener('click', function() {
    const sport = document.getElementById('sport').value;
    document.getElementById('training-display').innerText = `Selected Sport: ${sport}`;
});

document.getElementById('save-settings').addEventListener('click', function() {
    const distance = document.getElementById('distance').value;
    const targetSize = document.getElementById('target-size').value;
    document.getElementById('training-display').innerText += `, Distance: ${distance}, Target Size: ${targetSize}`;
});

document.getElementById('start-training').addEventListener('click', function() {
    document.getElementById('virtual-interface').innerText = 'Training session in progress...';
    // Simulate real-time feedback
    setTimeout(() => {
        document.getElementById('shot-accuracy').innerText = 'Shot Accuracy: 85%';
        document.getElementById('technique-feedback').innerText = 'Technique Feedback: Keep your elbow up';
    }, 2000);
});

document.getElementById('end-training').addEventListener('click', function() {
    document.getElementById('virtual-interface').innerText = 'Training session ended.';
    document.getElementById('shot-accuracy').innerText = 'Shot Accuracy: N/A';
    document.getElementById('technique-feedback').innerText = 'Technique Feedback: N/A';
});

document.getElementById('generate-report').addEventListener('click', function() {
    document.getElementById('generated-report').innerText = 'Generated Report: \nShot Accuracy: 85%\nTechnique Feedback: Keep your elbow up\nAreas for Improvement: Focus on follow-through';
});
