
document.addEventListener('DOMContentLoaded', function() {
    const sessions = [
        { id: 1, title: 'Morning Relaxation', duration: 10, style: 'Guided Meditation', theme: 'Relaxation', thumbnail: 'session1.jpg' },
        { id: 2, title: 'Stress Relief', duration: 20, style: 'Mindfulness', theme: 'Stress Relief', thumbnail: 'session2.jpg' },
        { id: 3, title: 'Focus Boost', duration: 5, style: 'Zen', theme: 'Focus', thumbnail: 'session3.jpg' }
    ];

    const searchBar = document.getElementById('search-bar');
    const styleFilter = document.getElementById('style-filter');
    const durationFilter = document.getElementById('duration-filter');
    const themeFilter = document.getElementById('theme-filter');
    const sessionsList = document.getElementById('sessions-list');
    const saveReminderButton = document.getElementById('save-reminder');
    const reminderTimeInput = document.getElementById('reminder-time');

    function displaySessions(filteredSessions) {
        sessionsList.innerHTML = '';
        filteredSessions.forEach(session => {
            const sessionCard = document.createElement('div');
            sessionCard.classList.add('session-card');
            sessionCard.innerHTML = `
                <img src="${session.thumbnail}" alt="${session.title}">
                <h3>${session.title}</h3>
                <p>${session.duration} mins</p>
                <p>${session.style}</p>
                <p>${session.theme}</p>
                <button>Start Session</button>
            `;
            sessionsList.appendChild(sessionCard);
        });
    }

    function filterSessions() {
        const searchText = searchBar.value.toLowerCase();
        const selectedStyle = styleFilter.value;
        const selectedDuration = durationFilter.value;
        const selectedTheme = themeFilter.value;

        const filteredSessions = sessions.filter(session => {
            return (
                (session.title.toLowerCase().includes(searchText) || searchText === '') &&
                (session.style === selectedStyle || selectedStyle === '') &&
                (session.duration === parseInt(selectedDuration) || selectedDuration === '') &&
                (session.theme === selectedTheme || selectedTheme === '')
            );
        });

        displaySessions(filteredSessions);
    }

    searchBar.addEventListener('input', filterSessions);
    styleFilter.addEventListener('change', filterSessions);
    durationFilter.addEventListener('change', filterSessions);
    themeFilter.addEventListener('change', filterSessions);

    saveReminderButton.addEventListener('click', () => {
        const reminderTime = reminderTimeInput.value;
        alert(`Reminder set for ${reminderTime}`);
    });

    displaySessions(sessions);
});
