
document.addEventListener('DOMContentLoaded', () => {
    const arenas = [];
    const configurations = [];

    document.getElementById('save-arena').addEventListener('click', () => {
        const sportType = document.getElementById('sport-type').value;
        const arenaName = document.getElementById('arena-name').value;
        const length = document.getElementById('arena-length').value;
        const width = document.getElementById('arena-width').value;
        const height = document.getElementById('arena-height').value;

        if (arenaName && length && width && height) {
            const newArena = { sportType, arenaName, dimensions: { length, width, height } };
            arenas.push(newArena);
            updateArenaSelection();
            document.getElementById('create-arena-message').innerText = 'Arena created successfully!';
        } else {
            document.getElementById('create-arena-message').innerText = 'Please fill in all fields.';
        }
    });

    document.getElementById('save-customizations').addEventListener('click', () => {
        const selectedArena = document.getElementById('select-arena').value;
        const seatingArrangement = document.getElementById('seating-arrangements').value;
        const lightingOption = document.getElementById('lighting-options').value;

        if (selectedArena && seatingArrangement && lightingOption) {
            const arena = arenas.find(arena => arena.arenaName === selectedArena);
            arena.customizations = { seatingArrangement, lightingOption };
            document.getElementById('customize-arena-preview').innerText = JSON.stringify(arena, null, 2);
        } else {
            document.getElementById('customize-arena-preview').innerText = 'Please select all options.';
        }
    });

    document.getElementById('update-arena').addEventListener('click', () => {
        const selectedArena = document.getElementById('select-arena-features').value;
        const addFeatures = Array.from(document.querySelectorAll('#add-remove-features input[type="checkbox"]:checked')).map(checkbox => checkbox.value);
        const removeFeatures = Array.from(document.querySelectorAll('#add-remove-features input[type="checkbox"]:not(:checked)')).map(checkbox => checkbox.value);

        if (selectedArena) {
            const arena = arenas.find(arena => arena.arenaName === selectedArena);
            arena.features = addFeatures.filter(feature => !removeFeatures.includes(feature));
            document.getElementById('add-remove-features-preview').innerText = JSON.stringify(arena, null, 2);
        } else {
            document.getElementById('add-remove-features-preview').innerText = 'Please select an arena.';
        }
    });

    document.getElementById('save-configuration').addEventListener('click', () => {
        const selectedArena = document.getElementById('select-arena').value;
        const arena = arenas.find(arena => arena.arenaName === selectedArena);

        if (arena) {
            configurations.push(arena);
            updateConfigurationSelection();
            document.getElementById('save-configuration-message').innerText = 'Configuration saved successfully!';
        } else {
            document.getElementById('save-configuration-message').innerText = 'Please select an arena.';
        }
    });

    document.getElementById('load-configuration-button').addEventListener('click', () => {
        const selectedConfiguration = document.getElementById('load-configuration').value;
        const configuration = configurations.find(config => config.arenaName === selectedConfiguration);

        if (configuration) {
            document.getElementById('current-configuration').innerText = JSON.stringify(configuration, null, 2);
            document.getElementById('load-configuration-message').innerText = 'Configuration loaded successfully!';
        } else {
            document.getElementById('load-configuration-message').innerText = 'Please select a configuration.';
        }
    });

    function updateArenaSelection() {
        const selectArena = document.getElementById('select-arena');
        const selectArenaFeatures = document.getElementById('select-arena-features');
        selectArena.innerHTML = '';
        selectArenaFeatures.innerHTML = '';

        arenas.forEach(arena => {
            const option = document.createElement('option');
            option.value = arena.arenaName;
            option.innerText = arena.arenaName;
            selectArena.appendChild(option);
            selectArenaFeatures.appendChild(option.cloneNode(true));
        });
    }

    function updateConfigurationSelection() {
        const loadConfiguration = document.getElementById('load-configuration');
        loadConfiguration.innerHTML = '';

        configurations.forEach(config => {
            const option = document.createElement('option');
            option.value = config.arenaName;
            option.innerText = config.arenaName;
            loadConfiguration.appendChild(option);
        });
    }
});
