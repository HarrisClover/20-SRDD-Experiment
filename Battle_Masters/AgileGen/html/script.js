
document.addEventListener('DOMContentLoaded', () => {
    const warriors = [
        { name: 'Warrior A', stats: 'Strength: 100, Agility: 50', abilities: ['Fireball', 'Shield Bash'] },
        { name: 'Warrior B', stats: 'Strength: 80, Agility: 70', abilities: ['Heal', 'Quick Strike'] },
        { name: 'Warrior C', stats: 'Strength: 90, Agility: 60', abilities: ['Stun', 'Power Attack'] }
    ];

    const scenarios = [
        { name: 'Scenario 1', description: 'Easy battle against weak opponents.', difficulty: 'Easy' },
        { name: 'Scenario 2', description: 'Moderate battle with balanced opponents.', difficulty: 'Medium' },
        { name: 'Scenario 3', description: 'Hard battle against strong opponents.', difficulty: 'Hard' }
    ];

    const warriorList = document.getElementById('warrior-list');
    const selectedWarriors = document.getElementById('selected-warriors');
    const teamSize = document.getElementById('team-size');
    const battleScenarios = document.getElementById('battle-scenarios');
    const currentTeamList = document.getElementById('current-team-list');
    const battlefield = document.getElementById('battlefield');
    const actionsList = document.getElementById('actions-list');
    const logList = document.getElementById('log-list');
    const outcomeDisplay = document.getElementById('outcome-display');

    let team = [];

    function updateTeam() {
        selectedWarriors.innerHTML = '';
        team.forEach(warrior => {
            const li = document.createElement('li');
            li.textContent = warrior.name;
            selectedWarriors.appendChild(li);
        });
        teamSize.textContent = team.length;
    }

    function updateCurrentTeam() {
        currentTeamList.innerHTML = '';
        team.forEach(warrior => {
            const li = document.createElement('li');
            li.textContent = warrior.name;
            currentTeamList.appendChild(li);
        });
    }

    function loadWarriors() {
        warriorList.innerHTML = '';
        warriors.forEach(warrior => {
            const li = document.createElement('li');
            li.textContent = `${warrior.name} - ${warrior.stats}`;
            li.addEventListener('click', () => {
                if (!team.includes(warrior)) {
                    team.push(warrior);
                    updateTeam();
                }
            });
            warriorList.appendChild(li);
        });
    }

    function loadScenarios() {
        battleScenarios.innerHTML = '';
        scenarios.forEach(scenario => {
            const li = document.createElement('li');
            li.textContent = `${scenario.name} - ${scenario.description} (Difficulty: ${scenario.difficulty})`;
            li.addEventListener('click', () => {
                startBattle(scenario);
            });
            battleScenarios.appendChild(li);
        });
    }

    function startBattle(scenario) {
        updateCurrentTeam();
        battlefield.innerHTML = `<p>Battlefield for ${scenario.name}</p>`;
        actionsList.innerHTML = '';
        team.forEach(warrior => {
            const li = document.createElement('li');
            li.textContent = `${warrior.name} - Actions: ${warrior.abilities.join(', ')}`;
            actionsList.appendChild(li);
        });
        logList.innerHTML = '<li>Battle started!</li>';
    }

    document.getElementById('start-battle-btn').addEventListener('click', () => {
        if (team.length > 0) {
            const selectedScenario = scenarios[0]; // For simplicity, select the first scenario
            startBattle(selectedScenario);
        } else {
            alert('Please assemble a team first.');
        }
    });

    document.getElementById('return-to-scenarios').addEventListener('click', () => {
        loadScenarios();
    });

    document.getElementById('assemble-new-team').addEventListener('click', () => {
        team = [];
        updateTeam();
    });

    loadWarriors();
    loadScenarios();
});
