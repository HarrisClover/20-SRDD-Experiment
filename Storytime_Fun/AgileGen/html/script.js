
document.getElementById('preview-button').addEventListener('click', function() {
    const storyText = document.getElementById('story-text').value;
    const storyContent = document.getElementById('story-content');
    storyContent.innerHTML = `<p>${storyText}</p>`;
    alert('Preview your storybook in the "Read or Listen to Your Storybook" section.');
});

document.getElementById('record-button').addEventListener('click', function() {
    alert('Voice-over recording started.');
    // Implement voice-over recording functionality here
});

document.getElementById('playback-button').addEventListener('click', function() {
    const audio = document.getElementById('voice-over-playback');
    audio.src = 'your-voice-over-file-path.mp3'; // Replace with actual file path
    audio.play();
});

document.getElementById('add-puzzle').addEventListener('click', function() {
    const interactiveContent = document.getElementById('interactive-content');
    interactiveContent.innerHTML = '<p>Interactive Puzzle/Quiz Added!</p>';
    alert('Puzzle/Quiz added to the storybook.');
});

document.getElementById('preview-interactive').addEventListener('click', function() {
    alert('Preview your interactive elements in the "Read or Listen to Your Storybook" section.');
});
