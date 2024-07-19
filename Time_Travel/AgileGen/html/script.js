
document.getElementById('load-period').addEventListener('click', function() {
    const timePeriod = document.getElementById('time-period').value;
    loadTimePeriod(timePeriod);
});

function loadTimePeriod(period) {
    const introduction = document.getElementById('introduction');
    introduction.style.display = 'block';
    const overview = introduction.querySelector('.overview');
    const keyEvents = introduction.querySelector('.key-events');

    switch (period) {
        case 'ancient-egypt':
            overview.textContent = 'Ancient Egypt was a civilization of ancient North Africa, concentrated along the lower reaches of the Nile River.';
            keyEvents.innerHTML = '<ul><li>3100 BC: Unification of Egypt</li><li>1279 BC: Reign of Ramses II</li></ul>';
            break;
        case 'medieval-europe':
            overview.textContent = 'Medieval Europe refers to the period of European history from the 5th to the late 15th century.';
            keyEvents.innerHTML = '<ul><li>476 AD: Fall of the Western Roman Empire</li><li>1066 AD: Norman Conquest of England</li></ul>';
            break;
        case 'renaissance':
            overview.textContent = 'The Renaissance was a fervent period of European cultural, artistic, political and economic ¡°rebirth¡± following the Middle Ages.';
            keyEvents.innerHTML = '<ul><li>1450: Gutenberg invents the printing press</li><li>1492: Columbus discovers America</li></ul>';
            break;
        case 'industrial-age':
            overview.textContent = 'The Industrial Age is a period of history that encompasses the changes in economic and social organization that began around 1760.';
            keyEvents.innerHTML = '<ul><li>1760: Start of the Industrial Revolution</li><li>1879: Edison invents the light bulb</li></ul>';
            break;
    }
}

function openTab(evt, tabName) {
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => content.classList.remove('active'));

    const tabLinks = document.querySelectorAll('.tab-link');
    tabLinks.forEach(link => link.classList.remove('active'));

    document.getElementById(tabName).classList.add('active');
    evt.currentTarget.classList.add('active');
}

document.querySelectorAll('.start-game').forEach(button => {
    button.addEventListener('click', function() {
        document.getElementById('game-interface').style.display = 'block';
    });
});

document.getElementById('submit-game').addEventListener('click', function() {
    const score = Math.floor(Math.random() * 100);
    document.querySelector('.user-score').textContent = `Score: ${score}`;
    document.querySelector('.progress-bar').style.width = `${score}%`;
    document.querySelector('.badge-reward').textContent = 'You earned a badge!';
});
