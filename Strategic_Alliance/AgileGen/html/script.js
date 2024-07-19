
const createAlliance = () => {
    const allianceName = document.getElementById('alliance-name').value;
    const description = document.getElementById('description').value;
    if (allianceName && description) {
        document.getElementById('current-alliance-name').textContent = allianceName;
        alert('Alliance created successfully');
    } else {
        alert('Please fill in all fields');
    }
};

const invitePlayer = () => {
    const playerName = document.getElementById('invite-player').value;
    if (playerName) {
        const membersList = document.getElementById('members-list');
        const listItem = document.createElement('li');
        listItem.textContent = playerName;
        membersList.appendChild(listItem);
        alert('Player invited successfully');
    } else {
        alert('Please enter a player name or ID');
    }
};

const disbandAlliance = () => {
    const confirmation = confirm('Are you sure you want to disband the alliance?');
    if (confirmation) {
        document.getElementById('current-alliance-name').textContent = 'None';
        document.getElementById('members-list').innerHTML = '';
        document.getElementById('alliance-resources').textContent = 'No resources';
        alert('Alliance disbanded successfully');
    }
};

const leaveAlliance = () => {
    const confirmation = confirm('Are you sure you want to leave the alliance?');
    if (confirmation) {
        document.getElementById('current-alliance-name').textContent = 'None';
        alert('You have left the alliance');
    }
};

const launchAttack = () => {
    const availableTroops = parseInt(document.getElementById('available-troops').textContent);
    const targetTerritory = document.getElementById('target-territory').value;
    if (availableTroops > 0 && targetTerritory) {
        const result = Math.random() > 0.5 ? 'won' : 'lost';
        document.getElementById('battle-result').textContent = `You have ${result} the battle for ${targetTerritory}`;
    } else {
        alert('You need to have troops and select a target territory');
    }
};

const defendTerritory = (territory) => {
    const result = Math.random() > 0.5 ? 'won' : 'lost';
    document.getElementById('defense-result').textContent = `You have ${result} the defense of ${territory}`;
};

// Dummy data for territories
const territories = ['Territory 1', 'Territory 2', 'Territory 3'];
const controlledTerritories = ['Territory 1'];
const incomingAttacks = ['Attack on Territory 1'];

window.onload = () => {
    const targetTerritorySelect = document.getElementById('target-territory');
    territories.forEach(territory => {
        const option = document.createElement('option');
        option.value = territory;
        option.textContent = territory;
        targetTerritorySelect.appendChild(option);
    });

    const controlledTerritoriesList = document.getElementById('controlled-territories');
    controlledTerritories.forEach(territory => {
        const listItem = document.createElement('li');
        listItem.textContent = territory;
        controlledTerritoriesList.appendChild(listItem);
    });

    const incomingAttacksList = document.getElementById('incoming-attacks');
    incomingAttacks.forEach(attack => {
        const listItem = document.createElement('li');
        listItem.textContent = attack;
        const defendButton = document.createElement('button');
        defendButton.textContent = 'Defend';
        defendButton.onclick = () => defendTerritory(attack);
        listItem.appendChild(defendButton);
        incomingAttacksList.appendChild(listItem);
    });
};
